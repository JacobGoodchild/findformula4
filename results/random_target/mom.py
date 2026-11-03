import numpy as np, networkx as nx
def moments(P):
    n=len(P); M1=np.zeros((n,n)); M2=np.zeros((n,n))
    for j in range(n):
        idx=[i for i in range(n) if i!=j]
        Q=P[np.ix_(idx,idx)]; I=np.eye(n-1)
        m1=np.linalg.solve(I-Q,np.ones(n-1))
        m2=np.linalg.solve(I-Q,2*Q@m1+np.ones(n-1))   # E[T^2]=1+2E[next T]+E[next T^2]
        M1[idx,j]=m1; M2[idx,j]=m2
    return M1,M2
for name,G in [('path6',nx.path_graph(6)),('lollipop',nx.lollipop_graph(4,3)),('rand',nx.gnp_random_graph(9,.4,seed=3))]:
    if not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); d=A.sum(1); P=A/d[:,None]; pi=d/d.sum()
    M1,M2=moments(P)
    print(name,'mean (random target):',np.round(M1@pi,6))
    print('   2nd moment pi-avg:',np.round(M2@pi,4))
    # variance version
    print('   var pi-avg:',np.round((M2-M1**2)@pi,4))
