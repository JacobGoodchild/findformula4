import sympy as sp, networkx as nx, random, sys
sys.path.insert(0,'.')
from exact_C import run
random.seed(2024); ok=0
for t in range(60):
    n=random.randint(9,12); G=nx.gnp_random_graph(n,random.choice([.25,.4,.6]),seed=random.randint(0,10**9))
    if not nx.is_connected(G): continue
    Wm=sp.zeros(n,n)
    for u,v in G.edges(): Wm[u,v]=Wm[v,u]=random.randint(1,20)
    run(Wm); ok+=1; print(ok,n,flush=True)
print('big exact OK',ok)
