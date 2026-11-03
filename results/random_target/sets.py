import numpy as np, itertools, networkx as nx
def hit_set(P,S):
    n=len(P); idx=[i for i in range(n) if i not in S]
    h=np.zeros(n); h[idx]=np.linalg.solve(np.eye(len(idx))-P[np.ix_(idx,idx)],np.ones(len(idx))); return h
def run(P,name):
    n=len(P); w,v=np.linalg.eig(P.T); pi=np.real(v[:,np.argmin(abs(w-1))]); pi/=pi.sum()
    subs=[S for S in itertools.combinations(range(n),2)]
    H=np.array([hit_set(P,S) for S in subs])  # |subs| x n
    for lab,wt in [('pi_j pi_k',[pi[a]*pi[b] for a,b in subs]),('pi_j+pi_k',[pi[a]+pi[b] for a,b in subs]),('1',[1]*len(subs))]:
        f=np.array(wt)@H; print(name,lab,'spread over start:',round(np.ptp(f),4))
    # nullspace of differences: weights w with sum_S w_S (H[S,i]-H[S,0])=0 for all i
    D=(H[:,1:]-H[:,[0]]).T   # (n-1) x |subs|
    u,s,vt=np.linalg.svd(D); null=vt[len(s):]
    print(name,'null dim',null.shape[0],'of',len(subs))
    # is there a nonneg w in nullspace? LP
    from scipy.optimize import linprog
    res=linprog(np.zeros(len(subs)),A_eq=np.vstack([D,np.ones(len(subs))]),b_eq=np.r_[np.zeros(n-1),1],bounds=(0,None))
    print(' positive solution exists:',res.status==0)
rng=np.random.default_rng(2)
n=6
A=(rng.random((n,n))<.6).astype(float); np.fill_diagonal(A,0); A=np.maximum(A,A.T)
run(A/A.sum(1)[:,None],'undirected')
