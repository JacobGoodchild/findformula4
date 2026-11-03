import numpy as np, networkx as nx, random
def rho2(G):
    n=G.number_of_nodes(); A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    w=2-(A*R).sum(1); return (R@w)[0]/4, w, n
viol=[]
random.seed(1)
tests=[]
for n in range(8,41,4):
    tests+= [('path',nx.path_graph(n)),('cycle',nx.cycle_graph(n)),('complete',nx.complete_graph(n)),('star',nx.star_graph(n-1)),
             ('grid',nx.grid_2d_graph(4,n//4)),('barbell',nx.barbell_graph(n//2-1,2)),('wheel',nx.wheel_graph(n)),
             ('hypercube-ish',nx.convert_node_labels_to_integers(nx.hypercube_graph(3))) ]
    for _ in range(30):
        G=nx.gnp_random_graph(n,random.choice([.1,.2,.4,.7]),seed=random.randint(0,10**6))
        if nx.is_connected(G): tests.append(('gnp',G))
    for _ in range(10):
        tests.append(('tree',nx.random_labeled_tree(n,seed=random.randint(0,10**6)) if hasattr(nx,'random_labeled_tree') else nx.random_tree(n,seed=random.randint(0,10**6))))
mn=1e9;mx=-1e9;cnt=0
for name,G in tests:
    r,w,n=rho2(G); cnt+=1
    lo,hi=(n-1)/n**2,(n-1)/4
    if r<lo-1e-9 or r>hi+1e-9: viol.append((name,n,r,lo,hi))
    if name in('path','cycle','complete','star','grid','wheel','barbell') and n in(8,20,40): print(name,n,'rho2=',round(r,4),'range',round(lo,4),round(hi,4),'min w',round(w.min(),3))
print(cnt,'graphs, violations:',viol[:5])
