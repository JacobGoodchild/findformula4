import numpy as np, networkx as nx
G=nx.gnp_random_graph(9,.45,seed=5)
while not nx.is_connected(G): G=nx.gnp_random_graph(9,.45,seed=np.random.randint(10**6))
n=9; A=nx.to_numpy_array(G); d=A.sum(1); m=d.sum()/2; L=np.diag(d)-A
Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; dg=np.diag(Lp); R=dg[:,None]+dg[None,:]-2*Lp
P=A/d[:,None]; H=np.zeros((n,n))
for j in range(n):
    idx=[i for i in range(n) if i!=j]; H[idx,j]=np.linalg.solve(np.eye(n-1)-P[np.ix_(idx,idx)],np.ones(n-1))
E=[(a,b) for a in range(n) for b in range(a+1,n) if A[a,b]]
f=lambda M,axis: [sum((M[a,i]-M[b,i])**2 if axis==0 else (M[i,a]-M[i,b])**2 for a,b in E) for i in range(n)]
print('R energy      ',np.round(f(R,0),6))
print('H(.,i) energy ',np.round(f(H,0),4))
print('H(i,.) energy ',np.round(f(H,1),4))
