import numpy as np, itertools, collections
n=6; E=list(itertools.combinations(range(n),2)); T3=list(itertools.combinations(range(n),3))
rows=[i for i,e in enumerate(E) if 0 not in e]            # cobase candidate: edges avoiding vertex 0
Ei={e:i for i,e in enumerate(E)}
B=np.zeros((len(E),len(T3)))
for c,(a,b,d) in enumerate(T3): B[Ei[(b,d)],c]=1; B[Ei[(a,d)],c]=-1; B[Ei[(a,b)],c]=1
Bs=B[rows]                                                  # 10 x 20
cnt=collections.Counter(); tot=0
for T in itertools.combinations(range(len(T3)),len(rows)):
    d=round(abs(np.linalg.det(Bs[:,T])))
    cnt[d]+=1; tot+=d*d
print('sum det^2 =',tot,' expected n^C(n-2,2)=',n**6)
print('distribution of |H1(T)| (0 = not Q-acyclic):',dict(sorted(cnt.items())))
