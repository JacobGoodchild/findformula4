import networkx as nx, numpy as np, itertools, json
from networkx.generators.atlas import graph_atlas_g
def inv(G):
    nodes=sorted(G); n=len(nodes); A=nx.to_numpy_array(G,nodelist=nodes)
    d=A.sum(1); L=np.diag(d)-A
    ev=np.linalg.eigvalsh(L); lam=ev[1:]
    Lp=np.linalg.pinv(L); dg=np.diag(Lp)
    R=dg[:,None]+dg[None,:]-2*Lp
    two_m=d.sum()
    # hitting times H(i,j)= m*(R_ij) + (sum_k d_k (R_ik - R_jk)... ) use formula
    Hh=0.5*(two_m*R + (R@d)[:,None]*1.0*0)  # unused
    # Kemeny constant via normalized Laplacian
    Dh=np.diag(d**-0.5); NL=Dh@L@Dh; nl=np.linalg.eigvalsh(NL)[1:]
    K=(1/nl).sum()
    kf=R.sum()/2
    tau=np.exp(np.log(lam).sum())/n
    # Wiener
    W=sum(l for _,dd in nx.all_pairs_shortest_path_length(G) for l in dd.values())/2
    # independence polynomial at 1 (Merrifield-Simmons) brute
    ms=0
    for mask in range(1<<n):
        ok=True
        for u,v in G.edges():
            if mask>>u&1 and mask>>v&1: ok=False;break
        ms+=ok
    # perfect-ish: matchings count (Hosoya)
    ho=0
    edges=list(G.edges())
    def rec(i,used):
        nonlocal ho
        if i==len(edges): ho+=1; return
        rec(i+1,used)
        u,v=edges[i]
        if not(used>>u&1) and not(used>>v&1): rec(i+1,used|1<<u|1<<v)
    rec(0,0)
    return dict(n=n,m=len(edges),tau=tau,kf=kf,K=K,W=W,MS=ms,Hosoya=ho,
                trL=ev.sum(),lam2=lam[0],lamn=lam[-1],
                sumInvDeg=(1/d).sum(),diam=nx.diameter(G),
                cyc=len(edges)-n+1,
                triangles=sum(nx.triangles(G).values())/3,
                specrad=np.linalg.eigvalsh(A)[-1])
rows=[]
for G in graph_atlas_g():
    if G.number_of_nodes()>=3 and nx.is_connected(G): rows.append(inv(G))
json.dump(rows,open('rows.json','w'))
print(len(rows))
