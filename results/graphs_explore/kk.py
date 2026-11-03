import numpy as np, networkx as nx, random
def KF(G):
    n=G.number_of_nodes(); A=nx.to_numpy_array(G); d=A.sum(1); L=np.diag(d)-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; dg=np.diag(Lp); R=dg[:,None]+dg[None,:]-2*Lp
    K=(d[:,None]*d[None,:]*R).sum()/(4*d.sum()/2)   # (1/4m) sum_{ij} d_i d_j R_ij, 4m=2*sum d
    K=(d[:,None]*d[None,:]*R).sum()/(2*d.sum())
    return K,R.sum()/2
random.seed(5); res={}
for n in (6,8,10,12):
    best=(9,None)
    star=nx.star_graph(n-1); K,kf=KF(star); s=K/kf
    for t in range(3000):
        G=nx.gnp_random_graph(n,random.choice([.15,.3,.6]),seed=random.randint(0,10**9))
        if not nx.is_connected(G): continue
        K,kf=KF(G); 
        if K/kf<best[0]: best=(K/kf,G.number_of_edges())
    for T in [nx.random_labeled_tree(n,seed=1) if hasattr(nx,'random_labeled_tree') else nx.random_tree(n,seed=1), nx.path_graph(n)]:
        K,kf=KF(T); best=min(best,(K/kf,'tree'))
    print(n,'star K/kf=',round(s,5),'formula (2n-3)/(2(n-1)^2)=',round((2*n-3)/(2*(n-1)**2),5),'| min found elsewhere',round(best[0],5),best[1])
