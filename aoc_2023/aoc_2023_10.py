def dfs(g, s):
    N,S,E,W = (-1,0),(1,0),(0,1),(0,-1)
    canconn = {E:'-J7S',W:'-LFS',S:'|LJS',N:'|7FS'}
    dirs = {'|':(N,S),'-':(W,E),'L':(E,N),'J':(W,N),'7':(S,W),'F':(S,E),'.':(),'S':(N,E,S,W)}
    v = set()
    stack = [s]
    parent = {}
    while stack:
        p = stack.pop()
        if p in v:
            continue
        v.add(p)                
        for r,c in dirs[g[p[0]][p[1]]]:
            row, col = p[0]+r, p[1]+c
            if row < 0 or row >= len(g) or col < 0 or col >= len(g[0]):
                continue
            o = g[row][col]
            if o not in canconn[(r,c)]:
                continue
            if (row,col) not in v or (row,col) == s:
                stack.append((row,col))
                parent[(row,col)] = (p[0],p[1])
            if (row,col) == s and len(parent) > 4:
                next, cnt = s, 0
                path = [next]
                while next:                
                    cnt += 1
                    next = parent[next]                    
                    if next == s:                        
                        return path 
                    path.append(next)
                
def run():
    m = open('input10.txt', 'r').read().splitlines()    
    s = None
    for row in range(len(m)):
        if s: break
        for col in range(len(m[row])):
            if m[row][col] == 'S':
                s = (row,col)
                break
    path = dfs(m,s)    
    print(len(path)//2)    
    
    pathset = set(path)
     
    rowpath = []
    for irow in range(len(m)):
        l = sorted([p for p in path if p[0]==irow], key=lambda x: x[1])
        rowpath.append(l)
    
    innerc = 0   
    for ir,row in enumerate(m):
        for ic,col in enumerate(row):
            if col == '.' or (ir,ic) not in pathset:
                cnt = 0
                for t in rowpath[ir]:
                    if t[1] < ic and row[t[1]] in '|LJ':
                        cnt += 1
                if cnt % 2 != 0:
                    innerc += 1
    print(innerc)
