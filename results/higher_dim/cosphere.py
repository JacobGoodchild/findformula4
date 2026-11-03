# Do the 'resistance points' of (d-1)-faces of a 2-complex lie on a common sphere? (graph case: always, by Theorem A)
import numpy as np, itertools
def test(tris,n,name):
    E=sorted({tuple(sorted(p)) for t in tris for p in itertools.combinations(t,2)}); Ei={e:i for i,e in enumerate(E)}
    B=np.zeros((len(E),len(tris)))
    for c,(a,b,d) in enumerate(tris): B[Ei[(b,d)],c]=1; B[Ei[(a,d)],c]=-1; B[Ei[(a,b)],c]=1
    Lu=B@B.T; w,V=np.linalg.eigh(Lu); keep=w>1e-9; Lp=(V[:,keep]/w[keep])@V[:,keep].T
    d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    # cospherical iff exists lambda, sum=1, R lambda = const*1 (least squares)
    m=len(E); A=np.r_[np.c_[R,-np.ones(m)],np.r_[np.ones(m),0][None,:]]; b=np.r_[np.zeros(m),1]
    sol,res,rk,sv=np.linalg.lstsq(A,b,rcond=None); err=np.abs(A@sol-b).max()
    print(f"{name:14s} edges={m} rank(del2)={keep.sum()} cospherical residual={err:.2e}")
tet=list(itertools.combinations(range(4),3)); test(tet,4,'tetra boundary')
octa=[(0,2,4),(0,2,5),(0,3,4),(0,3,5),(1,2,4),(1,2,5),(1,3,4),(1,3,5)]; test([tuple(sorted(t)) for t in octa],6,'octahedron')
rng=np.random.default_rng(1)
allt=list(itertools.combinations(range(6),3))
for k in range(3):
    sel=[allt[i] for i in rng.choice(len(allt),12,replace=False)]; test(sel,6,f'random12 #{k}')
