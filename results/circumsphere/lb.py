import numpy as np, networkx as nx, random
random.seed(9); rng=np.random.default_rng(9)
out={k:[1e9,-1e9] for k in ('qR','q2R','cR2*','Rmax')}
for t in range(3000):
    n=random.randint(3,20); G=nx.gnp_random_graph(n,random.choice([.15,.3,.6,.9]),seed=random.randint(0,10**9))
    if not nx.is_connected(G): continue
    W=nx.to_numpy_array(G)
    if t%2: W=W*np.exp(rng.normal(0,1.2,(n,n))); W=np.triu(W,1); W=W+W.T
    L=np.diag(W.sum(1))-W; Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n
    d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp; w=2-(W*R).sum(1); rho2=(R@w)[0]/4
    E=[(a,b) for a in range(n) for b in range(a+1,n) if W[a,b]>0]
    q=np.array([W[a,b]*R[a,b] for a,b in E]); Re=np.array([R[a,b] for a,b in E])
    for k,v in (('qR',(q*Re).sum()),('q2R',(q*q*Re).sum()),('Rmax',Re.max())):
        r=4*rho2/v; out[k][0]=min(out[k][0],r); out[k][1]=max(out[k][1],r)
for k,v in out.items():
    if k!='cR2*': print(k,'range of 4rho2/value:',np.round(v,4))
