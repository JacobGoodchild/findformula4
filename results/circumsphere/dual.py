import numpy as np, networkx as nx, random
from scipy.spatial import Delaunay
def rho2(W):
    n=len(W); L=np.diag(W.sum(1))-W; Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n
    d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp; w=2-(W*R).sum(1); return (R@w)[0]/4
def dual_of(G):
    ok,emb=nx.check_planarity(G); faces={}; fid=0; seen=set(); face_of={}
    for u,v in emb.edges():
        if (u,v) in seen: continue
        f=emb.traverse_face(u,v,mark_half_edges=seen)
        for a,b in zip(f,f[1:]+f[:1]): face_of[(a,b)]=fid
        fid+=1
    D=np.zeros((fid,fid))
    for (a,b),f in face_of.items():
        g=face_of[(b,a)]
        if f!=g: D[f,g]+=1   # directed half-edge counted once per direction -> D[f,g] accumulates once per shared edge from f's side
    return D
rows=[]
random.seed(1)
for t in range(40):
    n=random.randint(6,14); pts=np.random.default_rng(t).random((n,2)); tri=Delaunay(pts)
    G=nx.Graph()
    for s in tri.simplices:
        for i in range(3): G.add_edge(int(s[i]),int(s[(i+1)%3]))
    # 2-connected planar triangulation of convex hull: dual has outer face too (ok)
    W=nx.to_numpy_array(G); D=dual_of(G)
    if (D.sum(1)==0).any() or not nx.is_connected(nx.from_numpy_array(D)): continue
    rows.append((G.number_of_nodes(),D.shape[0],G.number_of_edges(),rho2(W),rho2(D)))
rows=np.array(rows); print(len(rows))
M=np.c_[rows[:,0],rows[:,1],rows[:,3],rows[:,4],np.ones(len(rows))]
u,s,vt=np.linalg.svd(M); print('sv tail',s[-2:]); 
print('rho(G)/(n-1)*4 sample',rows[:3])
