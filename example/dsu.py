
def makeSet(size):
    global parent, ranks, sizes
    parent = [i for i in range(size + 1)]
    ranks  = [0 for i in range(size + 1)]
    sizes  = [1 for i in range(size + 1)]
    

def findSet(u):
    if (u != parent[u]):
        # Path compression algo.
        # Every node points to the root
        parent[u] = findSet(parent[u])       
    return parent[u]

    """
    while (u != parent[u]):    
        # Path halving algo.
        # Every other node on the path points to its grandparent
        parent[u] = parent[parent[u]]
        u = parent[u]
        
        # Path splitting algo.
        # Every node on the path point to its grandparent
        u, parent[u] = parent[u], parent[parent[u]]
        
    return u  
    """


def unionSet_rank(u, v):
    up = findSet(u)
    vp = findSet(v)   
    
    # u, v are already in the same set
    if (up == vp):
        return
    
    # u, v are not in the same set -> merging
    if (ranks[up] < ranks[vp]):
        up, vp = vp, up
        
    parent[vp] = up
    if (ranks[up] == ranks[vp]):
        ranks[up] += 1


def unionSet_size(u, v):
    up = findSet(u)
    vp = findSet(v)   
    
    # u, v are already in the same set
    if (up == vp):
        return
    
    # u, v are not in the same set -> merging
    if (sizes[up] < sizes[vp]):
        up, vp = vp, up
        
    parent[vp] = up
    sizes[up] += sizes[vp]
    
