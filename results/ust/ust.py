import networkx as nx, numpy as np, itertools, json
from networkx.generators.atlas import graph_atlas_g
def trees(G):
    edges=list(G.edges()); n=G.number_of_nodes()
    # enumerate spanning trees by recursion (contraction-free simple): use itertools on combos for small graphs
    out=[]
    for comb in itertools.combinations(range(len(edges)),n-1):
        uf=list(range(n))
        def f(x):
            while uf[x]!=x: uf[x]=uf[uf[x]]; x=uf[x]
            return x
        ok=True
        for i in comb:
            a,b=f(edges[i][0]),f(edges[i][1])
            if a==b: ok=False;break
            uf[a]=b
        if ok: out.append(comb)
    return edges,out
rows=[]
for G in graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or n>6 or not nx.is_connected(G): continue
    edges,T=trees(G)
    EW=0.0
    for comb in T:
        H=nx.Graph([edges[i] for i in comb]); 
        EW+=sum(l for _,d in nx.all_pairs_shortest_path_length(H) for l in d.values())/2
    EW/=len(T)
    nodes=sorted(G); A=nx.to_numpy_array(G,nodelist=nodes); d=A.sum(1); L=np.diag(d)-A
    Lp=np.linalg.pinv(L); dg=np.diag(Lp); R=dg[:,None]+dg[None,:]-2*Lp
    kf=R.sum()/2
    W=sum(l for _,dd in nx.all_pairs_shortest_path_length(G) for l in dd.values())/2
    rows.append(dict(n=n,m=len(edges),tau=len(T),EW=EW,kf=kf,W=W,
        sumRe_deg=float(sum(R[u,v]*(d[u]+d[v]) for u,v in edges)),
        kfdeg=float(sum(R[i,j]*d[i]*d[j] for i in range(n) for j in range(i+1,n)))))
json.dump(rows,open('rows.json','w')); print(len(rows))
rows=json.load(open('rows.json'))
for nn in (4,5,6):
    S=[r for r in rows if r['n']==nn]
    M=np.array([[r['EW'],1,r['kf'],r['W'],r['m'],r['sumRe_deg'],r['kfdeg']] for r in S])
    u,s,vt=np.linalg.svd(M); print(nn,s[-3:]); print(np.round(vt[-1]/vt[-1][0],4))
