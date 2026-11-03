# probe: is there a universal law for the variance of the UST degree sequence? Var(deg_T(i)) = sum_{e∋i} q_e - sum_{e,f∋i} T_ef^2.
import numpy as np, networkx as nx
from networkx.generators.atlas import graph_atlas_g
# test: sum_i Var(deg_T i) vs (n-1) and sum q_e^2
rows=[]
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<4 or n>7 or not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n
    E=list(G.edges()); m=len(E)
    B=np.zeros((m,n))
    for k,(a,b) in enumerate(E): B[k,a]=1;B[k,b]=-1
    T=B@Lp@B.T                      # transfer current matrix (projection)
    q=np.diag(T)
    V=0
    for i in range(n):
        inc=[k for k,(a,b) in enumerate(E) if i in (a,b)]
        # sign-corrected covariance of indicator variables: Cov(1_e,1_f) = -T_ef^2 for e!=f
        V+=sum(q[k]*(1-q[k]) for k in inc)-sum(T[k,l]**2 for k in inc for l in inc if k!=l)
    rows.append((n,m,V,q.sum(),(q**2).sum(),(q*(1-q)).sum()))
import collections
print(len(rows))
M=np.array([[r[0],r[1],r[2],r[4],r[5],1] for r in rows])
u,s,vt=np.linalg.svd(M); print('singular values tail',s[-3:]); print(np.round(vt[-1]/vt[-1][2],4))
