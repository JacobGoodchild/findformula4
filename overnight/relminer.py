# Overnight 'universal linear identity' miner over ALL connected graphs on n vertices (n=7 atlas; n=8 built by vertex augmentation).
# Resumable: graphs cached in graphs_n.pkl, invariant table cached in inv_n.npy. Prints relations (integer null vectors) verified on every graph.
import sys, os, pickle, itertools, numpy as np, networkx as nx, sympy as sp
from networkx.generators.atlas import graph_atlas_g
n=int(sys.argv[1]); extra=int(sys.argv[2]) if len(sys.argv)>2 else 0   # extra=1 adds pairwise products of a core subset
def graphs(n):
    fn=f'graphs_{n}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    if n<=7: gs=[g for g in graph_atlas_g() if g.number_of_nodes()==n and nx.is_connected(g)]
    else:
        prev=graphs(n-1); buckets={}; gs=[]
        for g in prev:
            for r in range(1,n):
                for nb in itertools.combinations(range(n-1),r):
                    h=g.copy(); h.add_node(n-1); h.add_edges_from((n-1,v) for v in nb)
                    key=nx.weisfeiler_lehman_graph_hash(h,iterations=3)
                    lst=buckets.setdefault(key,[])
                    if not any(nx.is_isomorphic(h,x) for x in lst): lst.append(h); gs.append(h)
    pickle.dump(gs,open(fn,'wb')); return gs
def invariants(G):
    nn=G.number_of_nodes(); A=nx.to_numpy_array(G,dtype=np.int64); d=A.sum(1); m=int(d.sum()//2)
    out={'m':m}
    P=np.eye(nn,dtype=np.int64)
    for k in range(1,nn+1):
        P=P@A
        if k>=2: out[f'trA{k}']=int(np.trace(P))
    out['sd2']=int((d**2).sum()); out['sd3']=int((d**3).sum()); out['sd4']=int((d**4).sum())
    out['edge_dd']=int(sum(d[u]*d[v] for u,v in G.edges()))
    L=np.diag(d)-A
    cp=np.round(np.poly(L.astype(float))).astype(np.int64)
    for i,c in enumerate(cp[1:],1): out[f'Lcoef{i}']=int(c)
    out['tau']=int(round(np.linalg.det(L[1:,1:].astype(float))))
    # matchings
    edges=list(G.edges()); mk=[0]*(nn//2+1)
    def rec(i,used,k):
        if i==len(edges): mk[k]+=1; return
        rec(i+1,used,k); u,v=edges[i]
        if not(used>>u&1) and not(used>>v&1): rec(i+1,used|1<<u|1<<v,k+1)
    rec(0,0,0)
    for k in range(1,len(mk)): out[f'match{k}']=mk[k]
    # independent sets by size
    ik=[0]*(nn+1)
    for mask in range(1<<nn):
        ok=True
        for u,v in edges:
            if mask>>u&1 and mask>>v&1: ok=False;break
        if ok: ik[bin(mask).count('1')]+=1
    for k in range(2,nn+1): out[f'ind{k}']=ik[k]
    out['wiener']=int(sum(l for _,dd in nx.all_pairs_shortest_path_length(G) for l in dd.values())//2)
    return out
gs=graphs(n); print('graphs',len(gs),flush=True)
fn=f'inv_{n}.pkl'
if os.path.exists(fn): rows=pickle.load(open(fn,'rb'))
else:
    rows=[invariants(g) for g in gs]; pickle.dump(rows,open(fn,'wb'))
keys=list(rows[0].keys()); X=np.array([[r[k] for k in keys] for r in rows],dtype=object)
if extra:
    core=['m','sd2','tau','wiener','edge_dd']; ci=[keys.index(c) for c in core]
    for a,b in itertools.combinations_with_replacement(ci,2):
        keys.append(f'{keys[a]}*{keys[b]}'); X=np.c_[X,np.array([x[a]*x[b] for x in X],dtype=object)]
X=np.c_[np.array([1]*len(X),dtype=object),X]; keys=['1']+keys
rng=np.random.default_rng(0); samp=rng.choice(len(X),min(len(X),3*len(keys)),replace=False)
M=sp.Matrix(X[samp].tolist()); ns=M.nullspace(); print('invariants',len(keys),'rank',M.rank(),'relations',len(ns),flush=True)
good=[]
for v in ns:
    den=sp.ilcm(*[sp.fraction(x)[1] for x in v]); w=[int(x*den) for x in v]
    if all(sum(w[j]*X[i][j] for j in range(len(w)))==0 for i in range(len(X))): good.append(w)
print('verified on all',len(X),'graphs:',len(good),'relations (first 40 shown, sparse form):')
for w in good[:40]: print(' + '.join(f'{c}*{k}' for c,k in zip(w,keys) if c))
