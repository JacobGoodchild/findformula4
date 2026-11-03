import sympy as sp, itertools
n=5; E=list(itertools.combinations(range(n),2)); T3=list(itertools.combinations(range(n),3)); Ei={e:i for i,e in enumerate(E)}
B=sp.zeros(len(E),len(T3))
for c,(a,b,d) in enumerate(T3): B[Ei[(b,d)],c]=1; B[Ei[(a,d)],c]=-1; B[Ei[(a,b)],c]=1
rows=[i for i,e in enumerate(E) if 0 not in e]; M=B.extract(rows,list(range(len(T3))))
def count(xs):
    W=sp.diag(*[xs[(a,b)]*xs[(a,d)]*xs[(b,d)] for (a,b,d) in T3]); return sp.factor((M*W*M.T).det())
s,t=sp.symbols('s t')
for name,xs in [('x12=s',{e:(s if e==(1,2) else 1) for e in E}),('x01=s',{e:(s if e==(0,1) else 1) for e in E}),
                ('x12=s,x34=t',{e:(s if e==(1,2) else t if e==(3,4) else 1) for e in E}),
                ('x01=s,x12=t',{e:(s if e==(0,1) else t if e==(1,2) else 1) for e in E})]:
    print(name,':',count(xs))
