def run():
    pos = []
    emptylines = {}
    emptycols = {}
    m = open('input11.txt', 'r').read().splitlines()   
    for row,line in enumerate(m):
        for col,c in enumerate(line):            
            if c == '#':
                pos.append((row,col))         
    emptylines[-1] = emptycols[-1] = 0
    for row in range(len(m)):        
        emptylines[row] = 1 if not any(c == '#' for c in m[row]) else 0
        if row > 0:
            emptylines[row] += emptylines[row-1]
    for col in range(len(m[0])):
        emptycols[col] = 1 if not any(line[col] == '#' for line in m) else 0
        if col > 0:
            emptycols[col] += emptycols[col-1]           
    total1 = total2 = 0
    for i in range(len(pos)):
        for k in range(i+1,len(pos)):
            r1,c1 = pos[i]
            r2,c2 = pos[k]
            max_r = max(r1,r2)
            min_r = r2 if r2 < max_r else r1
            max_c = max(c1,c2)          
            min_c = c2 if c2 < max_c else c1
            emptyl,emptyc = emptylines[max_r]-emptylines[min_r-1], emptycols[max_c]-emptycols[min_c-1]
            v = max_r-min_r + max_c-min_c      
            total1 += emptyl + emptyc + v
            total2 += 999999 * (emptyl + emptyc) + v
    print(total1)
    print(total2)
