from collections import defaultdict

def run():    
    values = open('input15.txt', 'r').read().split(',')   
    total = 0 
    boxes = defaultdict(list)
    for v in values:               
        opidx = v.find('=')
        opidx = v.find('-') if opidx == -1 else opidx
        l = v[:opidx]
        pt1 = cv = 0
        for c in v:
            pt1 += ord(c)
            pt1 *= 17
            pt1 %= 256      
        for c in l:
            cv += ord(c)
            cv *= 17
            cv %= 256        
        total += pt1
        if v[opidx] == '=':
            for idx, lens in enumerate(boxes[cv]):
                if lens[0] == l:
                    boxes[cv][idx] = (l,int(v[opidx+1]))
                    break
            else:
                boxes[cv].append((l,int(v[opidx+1])))
        else:
             for idx, lens in enumerate(boxes[cv]):
                if lens[0] == l:
                    del boxes[cv][idx]
                    break        
        power = 0
        for boxk,boxv in boxes.items():            
            for idx,lens in enumerate(boxv,1):                
                power += (boxk+1)*idx*lens[1]

    print(total)                
    print(power)    
