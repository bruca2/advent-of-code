def _get_verts(lines,hex):
    row = col = 0
    vertices = [(row,col)]    
    per = 0    
    for line in lines:        
        if hex:
            ins = line.split()[2]
            s = int(ins[2:-2],16)       
            d = int(ins[-2:-1])
        else:
            d,s,_ = line.split()
            s = int(s)
        if d == 0 or d == 'R':
            col += s
        elif d == 2 or d == 'L':
            col -= s
        elif d == 3 or d == 'U':
            row -= s
        else:
            row += s        
        per += s
        vertices.append((row,col))
    
    max_row = max(vertices)[1]    
    s = per//2 + 1
    for idx in range(len(vertices)-1):
        s += (vertices[idx+1][1]-vertices[idx][1])*(max_row-vertices[idx+1][0])

    print(s)

def run():    
    lines = open('input18.txt', 'r').read().splitlines()     
    _get_verts(lines,False)
    _get_verts(lines,True)
        