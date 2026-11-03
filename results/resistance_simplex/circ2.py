import numpy as np, networkx as nx
from networkx.generators.atlas import graph_atlas_g
worst=0; worst2=0; cnt=0
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    Edeg=(A*R).sum(1)            # E[deg_T(i)] = sum_{j~i} R_ij  (unit conductances)
    lam=1-Edeg/2
    Rl=R@lam
    worst=max(worst,np.ptp(Rl))                 # circumcentre condition: R lam constant
    rho2=Rl[0]-0.5*lam@R@lam                    # rho^2 from distance formula
    s=np.ones(n)@np.linalg.solve(R,np.ones(n))
    worst2=max(worst2,abs(rho2-1/(2*s)), abs(lam.sum()-1))
    cnt+=1
print(cnt,'graphs; max spread of R*lam:',worst,'; consistency err:',worst2)
