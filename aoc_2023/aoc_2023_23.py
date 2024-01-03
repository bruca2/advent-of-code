import sys
sys.setrecursionlimit(3000)

# def _longest(g, s, top_sort):
#     row_size,col_size = len(g), len(g[0])
#     dirs = ((-1,0),(0,1),(1,0),(0,-1))   
#     dists = {(row,col):-100000 for col in range(col_size) for row in range(row_size)}
#     dists[s] = 0
#     for v in top_sort:        
#         for dir in dirs:
#             new_row, new_col = dir[0]+v[0],dir[1]+v[1]
#             if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':    
#                 dists[(new_row,new_col)] = max(dists[(new_row,new_col)],dists[v] + 1)
#     return dists

# def _dfs(g, s, v, top_sort):
#     row_size,col_size = len(g), len(g[0])
#     dirs = ((-1,0),(0,1),(1,0),(0,-1))    
#     v.add(s)    
#     if (row_size-1,col_size-2) == s:
#         top_sort.append(s)
#         return
#     for dir in dirs:
#         new_row, new_col = dir[0]+s[0],dir[1]+s[1]
#         if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':                
#             if (new_row,new_col) not in v:
#                 c = g[new_row][new_col] 
#                 if  c == '^' and dir == (1,0) or c == 'v' and dir == (-1,0) or c == '<' and dir == (0,1) or c == '>' and dir == (0,-1):
#                     continue
#                 _dfs(g,(new_row,new_col), v, top_sort)
_longest = -10000000
def _dfs(g, s, v, path):
    global _longest
    dirs = ((-1,0),(0,1),(1,0),(0,-1))    
    row_size,col_size = len(g), len(g[0])

    v.add(s)
    path.append(s)

    if s == (row_size-1,col_size-2):
        _longest = max(_longest, len(path))
    else:
        for dir in dirs:
            new_row, new_col = dir[0]+s[0],dir[1]+s[1]
            if row_size > new_row >= 0 and col_size > new_col >= 0 and g[new_row][new_col] != '#':                
                if (new_row,new_col) not in v:
                    c = g[new_row][new_col] 
                    if  c == '^' and dir == (1,0) or c == 'v' and dir == (-1,0) or c == '<' and dir == (0,1) or c == '>' and dir == (0,-1):
                        continue
                    _dfs(g,(new_row,new_col), v, path)
    path.pop()
    v.remove(s)

def run():     
    g = open('input23.txt', 'r').read().splitlines()
    
    #top_sort = []
    _dfs(g, (0,1), set(), [])
    print(_longest-1)
    #top_sort = list(reversed(top_sort))    
    #print(_longest(g, (0,1), top_sort)[(len(g)-1,len(g[0])-2)])
    #print(_longest(g, (0,1), top_sort))



run()