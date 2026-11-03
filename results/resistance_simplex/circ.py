import numpy as np, networkx as nx
from networkx.generators.atlas import graph_atlas_g
from fractions import Fraction
out={}
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    s=np.ones(n)@np.linalg.solve(R,np.ones(n))
    out.setdefault(n,[]).append((1/(2*s), G))
for n,v in out.items():
    r=np.array([x[0] for x in v]); print(n,len(v),'rho^2 min',r.min().round(5),'max',r.max().round(5))
