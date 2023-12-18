from collections import deque

def _bfs(dig,s):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    v = set([s])
    q = deque([s])
    while q:
        pos = q.pop()
        r,c = pos
        for dr,dc in dirs:
            if (r+dr,c+dc) in v or (r+dr,c+dc) in dig:
                continue
            q.appendleft((r+dr,c+dc))
            v.add((r+dr,c+dc))
    return v

def run():    
    lines = open('input18.txt', 'r').read().splitlines()     
    per = 0
    dig = set()
    row = col = 0
    dig.add((row,col))
    for line in lines:
        sr,sc = row,col
        d, s, c = line.split()
        s = int(s)
        if d == 'R':
            col += s
        elif d == 'L':
            col -= s
        elif d == 'U':
            row -= s
        else:
            row += s
        per += s
        er = row
        ec = col
        if row < sr:
            sr,er = row,sr
        if col < sc:
            sc,ec = col,sc
        for ir in range(sr, er+1):
            for ic in range(sc, ec+1):
                dig.add((ir,ic))          
    
    v = _bfs(dig,(1,2))
    
    # for row in range(15):
    #     for col in range(15):
    #         if (row,col) in dig:
    #             print('#',end='')
    #         elif (row,col) in v:
    #             print('x',end='')
    #         else:
    #             print('.',end='')
    #     print()
    print(len(v)+per)    
run()
    