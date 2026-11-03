import numpy as np
from mom import moments
rng=np.random.default_rng(5)
rows=[];ys=[]
for t in range(40):
    n=int(rng.integers(5,9)); Q=rng.random((n,n))+.02; Q/=Q.sum(1)[:,None]
    w,v=np.linalg.eig(Q.T); pi=np.real(v[:,np.argmin(abs(w-1))]); pi/=pi.sum()
    M1,M2=moments(Q); y=pi@M2@pi
    ev=np.linalg.eigvals(Q); ev=np.delete(ev,np.argmin(abs(ev-1)))
    k=[np.sum(1/(1-ev)**p).real for p in (1,2,3)]
    rows.append([1,k[0],k[0]**2,k[1],k[2]]); ys.append(y)
X=np.array(rows); y=np.array(ys)
c=np.linalg.lstsq(X,y,rcond=None)[0]; print(np.round(c,6),'maxerr',np.abs(X@c-y).max())
