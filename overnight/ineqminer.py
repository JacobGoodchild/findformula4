# For each pair of positive graph invariants (f,g), over ALL connected graphs on n=5..8 vertices, find the extremal ratio f/g and classify the
# extremal graph (K_n / star / path / cycle / other). Report pairs whose min (or max) is attained by the SAME named family for every n.
# Waits for inv_8.pkl (made by relminer.py 8). Output: candidates/ineq.txt  (candidate sharp inequalities; NOT verified/known-checked).
import pickle, os, sys, numpy as np, networkx as nx, itertools
os.makedirs('candidates',exist_ok=True)
for n in (5,6,7,8):
    for need in (f'graphs_{n}.pkl',f'inv_{n}.pkl'):
        if not os.path.exists(need) and n<8: sys.exit(f'missing {need}: run relminer.py {n} first')
if not os.path.exists('inv_8.pkl'): sys.exit('waiting for inv_8.pkl')
def cls(G):
    n=G.number_of_nodes(); m=G.number_of_edges(); ds=sorted(dict(G.degree()).values())
    if m==n*(n-1)//2: return 'complete'
    if m==n-1 and ds[-1]==n-1: return 'star'
    if m==n-1 and ds[-1]==2: return 'path'
    if m==n and ds[0]==ds[-1]==2: return 'cycle'
    if m==n-1: return 'other-tree'
    return 'other'
data={}
for n in (5,6,7,8):
    gs=pickle.load(open(f'graphs_{n}.pkl','rb')); rows=pickle.load(open(f'inv_{n}.pkl','rb'))
    data[n]=(gs,rows)
common=set.intersection(*[set(data[n][1][0]) for n in data])
keys=[k for k in data[8][1][0] if k in common and all(r[k]>0 for n in data for r in data[n][1]) and not k.startswith('Lcoef')]
res=[]
for f,g in itertools.permutations(keys,2):
    sig={}
    for n,(gs,rows) in data.items():
        r=np.array([x[f]/x[g] for x in rows]); i0,i1=r.argmin(),r.argmax()
        sig[n]=((r[i0],cls(gs[i0])),(r[i1],cls(gs[i1])))
    for side,name in ((0,'min'),(1,'max')):
        cl={sig[n][side][1] for n in sig}
        if len(cl)==1 and list(cl)[0]!='other':
            res.append((f,g,name,list(cl)[0],[round(float(sig[n][side][0]),5) for n in sorted(sig)]))
with open('candidates/ineq.txt','w') as fo:
    fo.write(f'{len(res)} candidate sharp inequalities (extremal family constant for n=5..8). Format: f/g  min|max  family  values(n=5..8)\n')
    for r in res: fo.write(f'{r[0]}/{r[1]} {r[2]} {r[3]} {r[4]}\n')
print(len(res),'candidates written')
