import networkx as nx, numpy as np, itertools
from networkx.generators.atlas import graph_atlas_g
from fractions import Fraction
import sympy as sp

def invariants(G):
    n=G.number_of_nodes(); m=G.number_of_edges()
    L=sp.Matrix(nx.laplacian_matrix(G,nodelist=sorted(G)).todense())
    A=sp.Matrix(nx.to_numpy_array(G,nodelist=sorted(G)).astype(int))
    deg=[G.degree(v) for v in sorted(G)]
    Lp=(L+sp.ones(n,n)/n).inv()-sp.ones(n,n)/n   # pseudoinverse
    R=lambda i,j: Lp[i,i]+Lp[j,j]-2*Lp[i,j]
    kf=sum(R(i,j) for i in range(n) for j in range(i+1,n))
    trees=sp.Matrix(L[1:,1:]).det()
    tr_pinv=Lp.trace()
    # Kemeny constant: sum over nonzero eigenvalues of normalized Laplacian of 1/lambda
    D=sp.diag(*deg); Dm=sp.diag(*[sp.Integer(1)/d for d in deg])
    N=(sp.eye(n)-sp.sqrt(1)*0)  # placeholder
    return dict(n=n,m=m,trees=int(trees),kf=kf,trpinv=tr_pinv,
                degsq=sum(d*d for d in deg), tri=int((A**3).trace()/6))
if __name__=="__main__":
    rows=[]
    for G in graph_atlas_g():
        if G.number_of_nodes()<3 or not nx.is_connected(G): continue
        rows.append((G,invariants(G)))
    print(len(rows))
    # Test: is kf*trees integer? and relation kf = n*trpinv
    ok=all(r['kf']==r['n']*r['trpinv'] for _,r in rows); print("kf=n*tr(L+) :",ok)
    ok=all((r['kf']*r['trees']).q==1 for _,r in rows); print("kf*trees integer:",ok)
