import sympy as sp, itertools
n=5; E=list(itertools.combinations(range(n),2)); X={e:sp.Symbol('x%d%d'%e) for e in E}
T3=list(itertools.combinations(range(n),3)); Ei={e:i for i,e in enumerate(E)}
B=sp.zeros(len(E),len(T3))
for c,(a,b,d) in enumerate(T3): B[Ei[(b,d)],c]=1; B[Ei[(a,d)],c]=-1; B[Ei[(a,b)],c]=1
rows=[i for i,e in enumerate(E) if 0 not in e]
W=sp.diag(*[X[(a,b)]*X[(a,d)]*X[(b,d)] for (a,b,d) in T3])
M=B.extract(rows,list(range(len(T3))))
P=sp.factor((M*W*M.T).det())
print(P)
