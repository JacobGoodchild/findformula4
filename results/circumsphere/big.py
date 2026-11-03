import numpy as np, networkx as nx
def check(G,name):
    G=nx.convert_node_labels_to_integers(G); n=len(G); A=nx.to_numpy_array(G); L=np.diag(A.sum(1))-A
    Lp=np.linalg.inv(L+np.ones((n,n))/n)-np.ones((n,n))/n; d=np.diag(Lp); R=d[:,None]+d[None,:]-2*Lp
    lam=1-(A*R).sum(1)/2; Rl=R@lam; rho2=Rl[0]-lam@R@lam/2
    E=[(a,b) for a,b in G.edges()]
    en=[sum((R[i,a]-R[i,b])**2 for a,b in E)/4 for i in (0,n//2,n-1)]
    F=R.sum(1); B=R.sum()/2/n**2+sum((F[a]-F[b])**2 for a,b in E)/(4*n**2)
    print(f"{name:12s} n={n:4d} spread(R lam)={np.ptp(Rl):.1e} rho2={rho2:.5f} energy-identity err={max(abs(e-rho2) for e in en):.1e} formulaB err={abs(B-rho2):.1e} bounds ok={(n-1)/n**2-1e-9<=rho2<=(n-1)/4+1e-9}")
check(nx.grid_2d_graph(20,20),'grid20x20'); check(nx.hypercube_graph(8),'Q8')
check(nx.random_regular_graph(3,200,seed=1),'3-reg 200'); check(nx.barabasi_albert_graph(300,2,seed=2),'BA 300')
check(nx.random_labeled_tree(150,seed=3) if hasattr(nx,'random_labeled_tree') else nx.random_tree(150,seed=3),'tree 150')
