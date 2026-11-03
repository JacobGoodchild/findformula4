import numpy as np, networkx as nx
from networkx.generators.atlas import graph_atlas_g
tot=0; nonreg=[]; regnoconst=[]
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n
    d=np.diag(Lp); const=np.ptp(d)<1e-9; reg=len(set(dict(G.degree()).values()))==1
    if const:
        tot+=1
        if not reg: nonreg.append((n,sorted(dict(G.degree()).values())))
    if reg and not const: regnoconst.append(n)
print('graphs with constant resistance-farness:',tot,'| non-regular among them:',len(nonreg),nonreg[:5],'| regular but F not const:',len(regnoconst))
