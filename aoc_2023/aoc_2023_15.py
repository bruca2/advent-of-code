from collections import defaultdict

def HASH(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256     
    return h

def run():    
    values = open('input15.txt', 'r').read().split(',')   
    pt1 = pt2 = 0 
    for v in values:
        pt1 += HASH(v)
    
    boxes = [[] for _ in range(256)]
    lenses = defaultdict(int)    
    for v in values:
        if '=' in v:            
            label = v[:-2]             
            h = HASH(label)
            if label in lenses:                
                lenses[label] = int(v[-1])
            else:
                boxes[h].append(label)                
                lenses[label] = int(v[-1])
        else:            
            label = v[:-1]             
            h = HASH(label)
            if label in lenses:
                del lenses[label]
                boxes[h].remove(label)
        
    for box_num in range(len(boxes)):
        box = boxes[box_num]
        for idx, lens in enumerate(box):
            pt2 += (box_num+1)*(idx+1)*lenses[lens]
    
    print(pt1)                
    print(pt2)
