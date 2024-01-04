from collections import defaultdict
import sys
sys.setrecursionlimit(3000)

def _longest(g, s, top_sort):
    row_size,col_size = len(g), len(g[0])
    dirs = ((-1,0),(0,1),(1,0),(0,-1))   
    dists = {(row,col):-100000 for col in range(col_size) for row in range(row_size)}
    dists[s] = 0
    for v in top_sort:        
        for dir in dirs:
            new_row, new_col = dir[0]+v[0],dir[1]+v[1]
            if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':    
                dists[(new_row,new_col)] = max(dists[(new_row,new_col)],dists[v] + 1)
    return dists

def _dfs(g, s, v, top_sort):
    row_size,col_size = len(g), len(g[0])
    dirs = ((-1,0),(0,1),(1,0),(0,-1))    
    v.add(s)    
    if (row_size-1,col_size-2) == s:
        top_sort.append(s)
        return
    for dir in dirs:
        new_row, new_col = dir[0]+s[0],dir[1]+s[1]
        if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':                
            if (new_row,new_col) not in v:
                c = g[new_row][new_col] 
                if  c == '^' and dir == (1,0) or c == 'v' and dir == (-1,0) or c == '<' and dir == (0,1) or c == '>' and dir == (0,-1):
                    continue
                _dfs(g,(new_row,new_col), v, top_sort)
    top_sort.append(s)

def _adj(g, n):
    row_size,col_size = len(g), len(g[0])
    dirs = ((-1,0),(0,1),(1,0),(0,-1))
    for dir in dirs:
        new_row, new_col = dir[0]+n[0],dir[1]+n[1]
        if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':                
            yield (new_row,new_col)

def _get_nodes(g):
    branches = []
    for irow in range(len(g)):
        for icol in range(len(g[0])):
            if g[irow][icol] != '#':
                if len(list(_adj(g,(irow,icol)))) > 2:
                    branches.append((irow,icol))
    branches.extend([(len(g)-1,len(g[0])-2),(0,1)])
    return branches
    
def _make_graph_util(g, source, node, v, new_g, nodes, level = 0):
    if node in nodes:
        return level,node[0],node[1]
    v.add(node)    
    for adj in _adj(g, node):        
        if adj not in v:
            value = _make_graph_util(g, source, adj, v, new_g, nodes, level + 1)
            if value:
                dist,row,col = value
                new_g[source].append(((row,col), dist))
    
def _make_graph(g, nodes, new_g):
    for node in nodes:        
        tmp_nodes = nodes[:]
        tmp_nodes.remove(node)
        _make_graph_util(g, node, node, set(), new_g, tmp_nodes)

def _get_all_paths(new_g, s, e, v = set(), path_length = 0, max_length = -1):        
    if s == e:
        return path_length        
    v.add(s)
    for adj,dist in new_g[s]:
        if adj not in v:  
            max_length = max(max_length, _get_all_paths(new_g, adj, e, v, path_length+dist,max_length))                   
    v.remove(s)
    return max_length  
        
def run():     
    g = open('input23.txt', 'r').read().splitlines()
    
    #part 1
    #for part1 we can see by the input that the maze is just a DAG
    #we can compute a longest path in O(n) time by doing a topsort first
    #and then finding the longest path following that order
    top_sort = []
    _dfs(g, (0,1), set(), top_sort)
    top_sort = list(reversed(top_sort))    
    print(_longest(g, (0,1), top_sort)[(len(g)-1,len(g[0])-2)])

    #part 2
    #no longer a DAG, so this is NP-hard
    #compact the graph using only the branching nodes
    #and brute force on that graph
    new_g = defaultdict(list)
    _make_graph(g, _get_nodes(g), new_g)
    print(_get_all_paths(new_g, (0,1), (len(g)-1,len(g[0])-2)))
    
