import numpy as np, networkx as nx
from mom import moments
def feats(P):
    n=len(P)
    w,v=np.linalg.eig(P.T); pi=np.real(v[:,np.argmin(abs(w-1))]); pi/=pi.sum()
    M1,M2=moments(P)
    g=M2@pi                    # sum_j pi_j E_i[T_j^2]
    r=pi@M1                    # r_j = sum_i pi_i H_ij  (=K, constant) ; instead use reverse:
    rev=(M1*pi[None,:]).sum(0) # placeholder
    back=np.array([sum(pi[j]*M1[j,i] for j in range(n) if j!=i) for i in range(n)])  # sum_j pi_j H_ji
    fwd=M1@pi
    cols={'1':np.ones(n),'back':back,'1/pi':1/pi,'sum pi_j H_ij^2? no':None}
    return pi,M1,M2,g,back
def test(P,extra):
    pi,M1,M2,g,back=feats(P); n=len(P)
    X=np.stack([np.ones(n),back,1/pi]+[e(pi,M1,M2) for e in extra],1)
    c,res,rk,sv=np.linalg.lstsq(X,g,rcond=None)
    return np.abs(X@c-g).max(), c
rng=np.random.default_rng(1)
extras={'none':[],
 'sum_j pi_j H_ji^2':[lambda pi,M1,M2: np.array([sum(pi[j]*M1[j,i]**2 for j in range(len(pi)) if j!=i) for i in range(len(pi))])],
 'H_ij weighted (M1@(pi*..))':[lambda pi,M1,M2: M1@(pi**2)],
 'sum_j pi_j^2 ...':[lambda pi,M1,M2: M1.T@pi],}
for trial in range(3):
    n=7
    A=(rng.random((n,n))<.5).astype(float); np.fill_diagonal(A,0); A=np.maximum(A,A.T)
    if not nx.is_connected(nx.from_numpy_array(A)): continue
    P=A/A.sum(1)[:,None]
    for k,e in extras.items(): print('undirected',k,test(P,e)[0])
    # non-reversible chain
    Q=rng.random((n,n))+.05; Q/=Q.sum(1)[:,None]
    for k,e in extras.items(): print('nonrev',k,test(Q,e)[0])
