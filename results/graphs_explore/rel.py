import json, numpy as np, itertools
rows=json.load(open('rows.json'))
keys=[k for k in rows[0] if k not in('n',)]
X={k:np.array([r[k] for r in rows],float) for k in rows[0]}
n=X['n']
# exact linear relations among invariants (per fixed n) : find null vectors of [1,f1..fk]
cand=['m','tau','kf','K','W','MS','Hosoya','sumInvDeg','diam','cyc','triangles','specrad']
for nn in (5,6,7):
    idx=n==nn
    M=np.stack([np.ones(idx.sum())]+[X[k][idx] for k in cand],1)
    u,s,vt=np.linalg.svd(M)
    print(nn,'smallest sv',s[-3:])
# ratio extremes
for a,b in itertools.permutations(['kf','K','W','tau','MS','Hosoya','m'],2):
    out=[]
    for nn in (5,6,7):
        idx=(n==nn)
        r=X[a][idx]/X[b][idx]
        out.append((round(r.min(),4),round(r.max(),4)))
    print(a,'/',b,out)
