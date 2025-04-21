def walk(sr,sc,cur,height,width,g,p):
    w = {}
    wloop = set()    
    m = { '^':'>', '>':'v', 'v':'<', '<':'^'}
    dirs = {'^':(-1,0), '>': (0,1), 'v':(1,0), '<':(0,-1)}    
    while 0<=sr<height and 0<=sc<width:
        if p == 1:
            a = (sr,sc)
            if a not in w:
                w[a] = cur
        else:
            a = (sr,sc,cur)
            if a in wloop:
                return set(),-1
            wloop.add(a)
        dr, dc = dirs[cur]
        if 0<=sr+dr<height and 0<=sc+dc<width:
            if g[sr+dr][sc+dc] != '#':            
                sr,sc = sr+dr,sc+dc
            else:
                cur = m[cur]                                
        else:
            break
    return w,len(w)

def run():
    lines = open("input6.txt", 'r').read().split()    
    g = [[c for c in r] for r in lines]        
    sr,sc = 0,0
    cur = '^'
    height, width  = len(lines), len(lines[0])
    for r in range(height):
        for c in range(width):
            if lines[r][c] == cur:
                sr,sc = r,c            
    w,nsteps = walk(sr,sc,cur,height,width,g,1)
    print(nsteps)
    cnt = 0
    for r,c in w:        
        if g[r][c] == '.':
            g[r][c] = '#'
            wl,nsteps = walk(sr,sc,cur,height,width,g,0)                
            if nsteps == -1:
                cnt += 1
            g[r][c] = '.'     
            sr,sc,cur = r, c, w[(r,c)]
    print(cnt)
