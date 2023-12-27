from collections import deque

def _bfs(g, st, max_level):
    st = (st,0)
    n,s,w,e = (-1,0),(1,0),(0,-1),(0,1)
    dirs = (n,s,w,e)
    q = deque([st])
    v = {st[0]:st[1]}
    plots = set()
    while q:        
        pos = q.pop()
        pos,level = pos[0],pos[1]      
        if level > max_level:
            break  
        if (level % 2 == 0 and max_level % 2 == 0) or (level % 2 == 1 and max_level % 2 == 1):
            plots.add(pos)
        for dir in dirs:
            new_pos_row,new_pos_col = pos[0]+dir[0], pos[1]+dir[1]
            if not (len(g) > new_pos_row >= 0 <= new_pos_col < len(g[0])) or g[new_pos_row][new_pos_col] == '#':
                continue
            new_pos = (new_pos_row,new_pos_col)
            if new_pos not in v:
                q.appendleft((new_pos,level+1))
                v[new_pos] = level+1
    return len(plots),v
            
def run():    
    lines = open('input21.txt', 'r').read().splitlines()
    start = None
    for irow in range(len(lines)):
        if start:
            break
        for icol in range(len(lines[0])):
            if lines[irow][icol] == 'S':
                start = (irow,icol)                
                break        
    cnt,v = _bfs(lines, start,64)
    print(cnt)
 
    _,v = _bfs(lines, start,131)
    n_steps = 26501365    
    diamond_width = (n_steps-(len(lines[0])//2))//len(lines)    
    even = odd = even_corner = odd_corner = 0
    for sq in v.values():
        if sq % 2 == 0:
            even +=1
        else:
            odd += 1
    for sq in v.values():
        if sq % 2 == 0 and sq > 65:
            even_corner +=1
        elif sq % 2 == 1 and sq > 65:
            odd_corner += 1

    #for the given n_steps the diamond_width is an even number
    #so there are (diamond_width+1)^2 "odd" tiles and diamond_width^2 "even" tiles in the diamond
    n_plots = (diamond_width+1)**2*odd + diamond_width**2*even - (diamond_width+1)*odd_corner + diamond_width*even_corner
    print(n_plots)
    