# Exact check of Theorem C: for EVERY vertex i, 4*rho^2 = sum_{ab in E} c_ab (R_ia - R_ib)^2 ; and rho^2 <= (1/4) sum_E c R^2 <= (1/4) sum_E q R
import sympy as sp, networkx as nx, random
from networkx.generators.atlas import graph_atlas_g
def run(Wm):
    n=Wm.shape[0]
    L=sp.diag(*[sum(Wm[i,:]) for i in range(n)])-Wm
    Lp=(L+sp.ones(n,n)/n).inv()-sp.ones(n,n)/n
    d=[Lp[i,i] for i in range(n)]
    R=sp.Matrix(n,n,lambda i,j:d[i]+d[j]-2*Lp[i,j])
    w=[2-sum(Wm[i,j]*R[i,j] for j in range(n)) for i in range(n)]
    rho2=(R*sp.Matrix(w))[0]/4
    E=[(a,b) for a in range(n) for b in range(a+1,n) if Wm[a,b]!=0]
    for i in range(n):
        assert 4*rho2==sum(Wm[a,b]*(R[i,a]-R[i,b])**2 for a,b in E), "C fails"
    ub1=sum(Wm[a,b]*R[a,b]**2 for a,b in E)/4; ub2=sum(R[a,b] for a,b in E)/4
    assert rho2<=ub1<=ub2
    tree=len(E)==n-1
    assert (rho2==ub2)==tree, "equality case"
    return 1
if __name__=="__main__":
    cnt=0
    for G in graph_atlas_g():
        if G.number_of_nodes()<2 or not nx.is_connected(G): continue
        run(sp.Matrix(nx.to_numpy_array(G).astype(int).tolist())); cnt+=1
    random.seed(11)
    for t in range(120):
        n=random.randint(3,8); G=nx.gnp_random_graph(n,.5,seed=random.randint(0,10**6))
        if not nx.is_connected(G): continue
        Wm=sp.zeros(n,n)
        for u,v in G.edges(): Wm[u,v]=Wm[v,u]=random.randint(1,9)
        run(Wm); cnt+=1
    print('Theorem C + bound chain + equality-iff-tree OK on',cnt,'graphs')
