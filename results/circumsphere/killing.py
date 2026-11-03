import numpy as np, networkx as nx
rng=np.random.default_rng(4)
for t in range(3):
    n=6; G=nx.gnp_random_graph(n,.6,seed=t+10)
    if not nx.is_connected(G): continue
    A=nx.to_numpy_array(G); kap=rng.random(n)+.1
    L=np.diag(A.sum(1))-A; Gm=np.linalg.inv(L+np.diag(kap)); d=np.diag(Gm)
    R=d[:,None]+d[None,:]-2*Gm
    lam=np.linalg.solve(R,np.ones(n)); s=lam.sum(); lam=lam/s
    p=(A*R).sum(1)
    # guess: lam_i = 1 - p_i/2 - something; look at residual and try kappa-related terms
    res=lam-(1-p/2)
    print('sum lam',lam.sum().round(4),'| lam',np.round(lam,4))
    print('  1-p/2      ',np.round(1-p/2,4)); 
    # try lam_i = a*(1 - p_i/2 - kap_i*g_i) with g_i=d_i? solve least squares for combination of [1, p, kap*d, kap, kap*sum_j R_ij]
    X=np.c_[np.ones(n),p,kap*d,kap,kap*R.sum(1),(kap*R).sum(1)]
    c,r,rk,sv=np.linalg.lstsq(X,lam,rcond=None); print('  fit resid',np.abs(X@c-lam).max().round(6),np.round(c,4))
