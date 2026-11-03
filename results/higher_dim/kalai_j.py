import numpy as np, itertools
from math import comb
def check(n,d,j):
    F=list(itertools.combinations(range(n),d)); Fi={f:i for i,f in enumerate(F)}
    S=list(itertools.combinations(range(n),d+1)); B=np.zeros((len(F),len(S)))
    for c,s in enumerate(S):
        for k in range(d+1): B[Fi[s[:k]+s[k+1:]],c]=(-1)**k
    w,V=np.linalg.eigh(B@B.T); keep=w>1e-8; Pi=B.T@(V[:,keep]/w[keep])@V[:,keep].T@B
    tau=tuple(range(j+1)); star=[c for c,s in enumerate(S) if set(tau)<=set(s)]
    K=Pi[np.ix_(star,star)]; ev=np.sort(np.linalg.eigvalsh(K))
    a=comb(n-j-2,d-j-1); b=comb(n-j-2,d-j)
    pred=np.sort(np.r_[np.ones(a),np.full(b,(j+1)/n)])
    return len(star)==a+b, np.abs(ev-pred).max()
for d,j,ns in [(2,0,[5,6,7]),(2,1,[5,6,7]),(3,0,[6,7]),(3,1,[6,7,8]),(3,2,[6,7,8]),(4,2,[7,8])]:
    for n in ns: print('d',d,'j',j,'n',n,check(n,d,j))
