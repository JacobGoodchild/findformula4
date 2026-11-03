import numpy as np, networkx as nx, random
def stuff(W):
    n=len(W); L=np.diag(W.sum(1))-W
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n
    d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    w=2-(W*R).sum(1); rho2=(R@w)[0]/4
    return rho2,R
random.seed(3); rng=np.random.default_rng(3)
worst=-1e9; cnt=0; eqtree=[]
for t in range(4000):
    n=random.randint(3,25); G=nx.gnp_random_graph(n,random.choice([.1,.2,.3,.5,.8]),seed=random.randint(0,10**9))
    if not nx.is_connected(G): continue
    W=nx.to_numpy_array(G)
    if t%2: W=W*np.exp(rng.normal(0,1.5,(n,n))); W=np.triu(W,1); W=W+W.T
    rho2,R=stuff(W); sumRe=sum(R[i,j] for i in range(n) for j in range(i+1,n) if W[i,j]>0)
    ratio=rho2/(sumRe/4); worst=max(worst,ratio); cnt+=1
    if G.number_of_edges()==n-1: eqtree.append(abs(ratio-1))
print(cnt,'graphs; max rho2/(sum_e R_e /4) =',worst,'; tree max |ratio-1| =',max(eqtree) if eqtree else None)
