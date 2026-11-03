import networkx as nx, itertools
from networkx.generators.trees import random_labeled_tree
# sum over all labelled trees on n vertices of Wiener index, via Prufer enumeration
def prufer_trees(n):
    for seq in itertools.product(range(n),repeat=n-2):
        yield nx.from_prufer_sequence(list(seq))
out=[]
for n in range(2,9):
    if n==2: out.append(1); continue
    s=0
    for T in prufer_trees(n):
        s+=sum(l for _,d in nx.all_pairs_shortest_path_length(T) for l in d.values())//2
    out.append(s)
print(out)
