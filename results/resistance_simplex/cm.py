import sympy as sp, networkx as nx, itertools, random
from networkx.generators.atlas import graph_atlas_g
def data(G):
    n=G.number_of_nodes(); nodes=sorted(G)
    L=sp.Matrix(nx.laplacian_matrix(G,nodelist=nodes).todense())
    Lp=(L+sp.ones(n,n)/n).inv()-sp.ones(n,n)/n
    R=sp.Matrix(n,n,lambda i,j: Lp[i,i]+Lp[j,j]-2*Lp[i,j])
    tau=L[1:,1:].det()
    CM=sp.zeros(n+1,n+1)
    for i in range(n):
        CM[0,i+1]=CM[i+1,0]=1
        for j in range(n): CM[i+1,j+1]=R[i,j]
    return n,tau,R,CM
bad=0;cnt=0
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or not nx.is_connected(G): continue
    n,tau,R,CM=data(G); cnt+=1
    # Cayley-Menger with squared distances: det CM = (-1)^n 2^(n-1) ((n-1)!)^2 vol^2 ; claim vol^2=1/((n-1)!^2 tau)
    ok = CM.det()==(-1)**n*2**(n-1)/tau
    # Bapat-type: det R
    if not ok: bad+=1
print('graphs',cnt,'CM identity failures',bad)
