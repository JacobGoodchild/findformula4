import numpy as np
rng=np.random.default_rng(0)
worst=1e9; arg=None
for t in range(20000):
    n=int(rng.integers(3,9))
    r=np.sort(rng.normal(size=n)*rng.choice([.3,1,3])) if t%2 else np.sort(np.cumsum(rng.exponential(size=n)**rng.choice([1,3])))
    c=np.sort(np.roots(np.polyder(np.poly(r))).real)
    g=np.diff(r).min(); h=np.diff(c).min()
    if h/g<worst: worst=h/g; arg=(n,r)
print('min over trials of mingap(p\')/mingap(p) =',worst, arg)
# structured: n equally spaced roots
for n in range(3,9):
    r=np.arange(n,dtype=float); c=np.sort(np.roots(np.polyder(np.poly(r))).real); print(n,np.diff(c).min())
