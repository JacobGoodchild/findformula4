# Exact (rational arithmetic) check of Theorems A and B on all 994 small connected graphs
# plus random integer-weighted graphs.
import sympy as sp, networkx as nx, random
from networkx.generators.atlas import graph_atlas_g
def check(Wm):
    n=Wm.shape[0]
    L=sp.diag(*[sum(Wm[i,:]) for i in range(n)])-Wm
    Lp=(L+sp.ones(n,n)/n).inv()-sp.ones(n,n)/n
    d=[Lp[i,i] for i in range(n)]
    R=sp.Matrix(n,n,lambda i,j:d[i]+d[j]-2*Lp[i,j])
    lam=sp.Matrix([1-sum(Wm[i,j]*R[i,j] for j in range(n))/2 for i in range(n)])
    assert sum(lam)==1
    Rl=R*lam
    assert all(Rl[i]==Rl[0] for i in range(n)), "A fails"          # Theorem A: circumcentre condition
    rho2=Rl[0]-(lam.T*R*lam)[0]/2                                    # circumradius^2
    kf=sum(R[i,j] for i in range(n) for j in range(i+1,n))
    dLd=sum(Wm[i,j]*(d[i]-d[j])**2 for i in range(n) for j in range(i+1,n))
    assert rho2==kf/n**2+dLd/4, "B fails"                             # Theorem B
    # also: rho2 = (n-1)/4 for trees (unit weights) handled separately
    return rho2
cnt=0
for G in graph_atlas_g():
    if G.number_of_nodes()<2 or not nx.is_connected(G): continue
    Wm=sp.Matrix(nx.to_numpy_array(G).astype(int).tolist()); check(Wm); cnt+=1
print('atlas graphs OK:',cnt)
random.seed(7)
for t in range(150):
    n=random.randint(3,8); G=nx.gnp_random_graph(n,.5,seed=random.randint(0,10**6))
    if not nx.is_connected(G): continue
    Wm=sp.zeros(n,n)
    for u,v in G.edges(): Wm[u,v]=Wm[v,u]=random.randint(1,9)
    check(Wm); cnt+=1
print('total incl. weighted OK:',cnt)
