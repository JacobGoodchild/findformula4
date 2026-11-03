import numpy as np, itertools
from math import comb
def check(n,d):
    F=list(itertools.combinations(range(n),d)); Fi={f:i for i,f in enumerate(F)}   # (d-1)-faces have d vertices
    S=list(itertools.combinations(range(n),d+1))                                    # d-faces
    B=np.zeros((len(F),len(S)))
    for j,s in enumerate(S):
        for k in range(d+1):
            B[Fi[s[:k]+s[k+1:]],j]=(-1)**k
    w,V=np.linalg.eigh(B@B.T); keep=w>1e-8; Pi=B.T@(V[:,keep]/w[keep])@V[:,keep].T@B
    assert abs(np.trace(Pi)-comb(n-1,d))<1e-8
    tau=tuple(range(d)); star=[j for j,s in enumerate(S) if set(tau)<=set(s)]
    K=Pi[np.ix_(star,star)]
    zs=np.linspace(-1,1,len(star)+1); vals=[np.linalg.det(np.eye(len(star))-(1-z)*K) for z in zs]
    coef=np.polyfit(zs,vals,len(star))[::-1]
    pred=np.array([comb(n-d-1,k)*(d/n)**k*(1-d/n)**(n-d-1-k) for k in range(n-d)])   # P(deg-1=k)
    got=coef[1:]                                                                       # P(deg=k+1)
    return np.abs(got-pred).max(), np.abs(coef[0])
for d,ns in [(1,[4,6,8]),(2,[5,6,7,8]),(3,[6,7,8])]:
    for n in ns: print('d=',d,'n=',n,'max |P - Bin(n-d-1,d/n)| =',"%.1e"%check(n,d)[0])
