import numpy as np, itertools, networkx as nx
from scipy.optimize import minimize
def hit_set(P,S):
    n=len(P); idx=[i for i in range(n) if i not in S]
    h=np.zeros(n); h[idx]=np.linalg.solve(np.eye(len(idx))-P[np.ix_(idx,idx)],np.ones(len(idx))); return h
def prep(A):
    n=len(A); P=A/A.sum(1)[:,None]; pi=A.sum(1)/A.sum()
    subs=list(itertools.combinations(range(n),2)); H=np.array([hit_set(P,S) for S in subs])
    return pi,subs,H
rng=np.random.default_rng(0); chains=[]
for _ in range(4):
    n=7; A=(rng.random((n,n))<.5).astype(float); A=np.triu(A,1); A=A+A.T
    if nx.is_connected(nx.from_numpy_array(A)): chains.append(prep(A))
def loss(x):
    a,b=x; tot=0
    for pi,subs,H in chains:
        w=np.array([(pi[j]*pi[k])**a*(pi[j]+pi[k])**b for j,k in subs]); w/=w.sum()
        f=w@H; tot+=np.ptp(f)/f.mean()
    return tot
best=min((minimize(loss,x0,method='Nelder-Mead') for x0 in [(0,0),(1,0),(0,1),(1,1),(-1,1),(2,-1)]),key=lambda r:r.fun)
print('best (a,b)=',best.x,'relative spread sum',best.fun)
