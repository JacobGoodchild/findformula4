import numpy as np, itertools
def run(n):
    V=range(n); E=list(itertools.combinations(V,2)); Ei={e:i for i,e in enumerate(E)}
    T=list(itertools.combinations(V,3)); B=np.zeros((len(E),len(T)))
    for j,(a,b,c) in enumerate(T):
        B[Ei[(b,c)],j]=1; B[Ei[(a,c)],j]=-1; B[Ei[(a,b)],j]=1
    Pi=B.T@np.linalg.pinv(B@B.T)@B           # projector onto row space of B (determinantal kernel)
    q=np.diag(Pi); rank=np.linalg.matrix_rank(B)
    e0=Ei[(0,1)]; S=[j for j,t in enumerate(T) if (0 in t and 1 in t)]
    K=Pi[np.ix_(S,S)]
    # generating function of number of selected triangles in S: det(I-(1-z)K) ; coefficients of z^k
    zs=np.linspace(-1,1,len(S)+1)
    vals=[np.linalg.det(np.eye(len(S))-(1-z)*K) for z in zs]
    coef=np.polyfit(zs,vals,len(S))[::-1]
    return rank,q[0],coef[:4]
for n in range(4,11):
    r,q,c=run(n); print(n,'rank',r,'q',round(q,5),'P(deg=0,1,2,3) of an edge:',np.round(c,5))
