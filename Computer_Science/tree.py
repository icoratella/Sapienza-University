data = "rosalind_tree.txt"

# read input data
with open(data) as f:
    n = int(f.readline().strip())
    edges = [tuple(map(int, line.strip().split())) for line in f]

# initialize sets and variables
vertices = set(range(1, n+1))
tree_edges = set()
disjoint_sets = [set([v]) for v in vertices]

# iterate over edges to build disjoint sets
for u, v in edges:
    u_set, v_set = None, None
    for s in disjoint_sets:
        if u in s:
            u_set = s
        if v in s:
            v_set = s
    if u_set != v_set:
        u_set |= v_set
        disjoint_sets.remove(v_set)
        tree_edges.add((u, v))

# count remaining edges
remaining_edges = len(edges) - len(tree_edges)

# output result
print(len(disjoint_sets) - 1 + remaining_edges)