def run():
    pos = []
    emptylines = {}
    emptycols = {}
    m = open('input11.txt', 'r').read().splitlines()   
    for row,line in enumerate(m):
        emptylines[row] = True
        for col,c in enumerate(line):            
            if c == '#':
                pos.append((row,col))                                         
                emptylines[row] = False
    for col in range(len(m[0])):
        emptycols[col] = not any(line[col] == '#' for line in m)    
    total1 = total2 = 0
    for i in range(len(pos)):
        for k in range(i+1,len(pos)):
            r1,c1 = pos[i]
            r2,c2 = pos[k]
            max_r,min_r = max(r1,r2), min(r1,r2)
            max_c,min_c = max(c1,c2), min(c1,c2)            
            for e in range(min_r+1,max_r):
                if emptylines[e]:                    
                    total1 += 1
                    total2 += 999999
            for e in range(min_c+1,max_c):
                if emptycols[e]:
                    total1 += 1
                    total2 += 999999
            v = max_r-min_r + max_c-min_c            
            total1 += v
            total2 += v
    print(total1)
    print(total2)