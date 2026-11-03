import numpy as np, networkx as nx, itertools
def meeting(P, lazy=True):
    n=len(P)
    if lazy: P=(np.eye(n)+P)/2           # avoid parity problems on bipartite graphs
    Q=np.kron(P,P)                        # two independent walkers, state (i,j)->index i*n+j
    diag=[i*n+i for i in range(n)]; idx=[s for s in range(n*n) if s not in diag]
    h=np.zeros(n*n); h[idx]=np.linalg.solve(np.eye(len(idx))-Q[np.ix_(idx,idx)],np.ones(len(idx)))
    return h.reshape(n,n),P
for name,G in [('path6',nx.path_graph(6)),('rand8',nx.gnp_random_graph(8,.4,seed=4)),('lollipop',nx.lollipop_graph(4,3))]:
    if not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); P0=A/A.sum(1)[:,None]; M,P=meeting(P0)
    w,v=np.linalg.eig(P.T); pi=np.real(v[:,np.argmin(abs(w-1))]); pi/=pi.sum()
    print(name,'sum_j pi_j M(i,j):',np.round(M@pi,4))
