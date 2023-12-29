from collections import defaultdict
import copy

def settle(settled, brick,supported):
    x1,y1,z1,x2,y2,z2 = brick[1]
    #{brick_idx: x_start,y_start,z_start,x_end,y_end,z_end
    new_z = 1
    for interval in settled:                       
        x_start,y_start,_,x_end,y_end,z_end = interval[1]      
        if z_end < new_z-1:
            break
        #intersection
        if max(x1,x_start) <= min(x2,x_end) and max(y1,y_start) <= min(y2,y_end):
            supported[brick[0]].append(interval[0])
            new_z = z_end+1
    settled.append((brick[0],[x1,y1,new_z,x2,y2,new_z+z2-z1]))

def run():   
    bricks = []    
    lines = open('input22.txt', 'r').read().splitlines()
    for line in lines:
        bricks.append([int(x) for x in line.replace('~',',').split(',')])    
    bricks = tuple((idx,brick) for idx,brick in enumerate(bricks))
    bricks = sorted(bricks,key=lambda x: x[1][2])
    supported = defaultdict(list)    
    settled = []
    for brick in bricks:
        settle(settled,brick,supported)
        settled.sort(key=lambda x: -x[1][5])
    crucial = set()
    for value_list in supported.values():    
        if len(value_list) == 1:
            crucial.add(value_list[0])
    print(len(bricks)-len(crucial))
    crucial = list(crucial)
    cnt = 0
    while crucial:
        _supported = copy.deepcopy(supported)
        disint = crucial.pop()
        to_fall = []
        to_fall.append(disint)
        while to_fall:
            next = to_fall.pop()
            for may_fall,supp in _supported.items():
                if next in supp:
                    _supported[may_fall].remove(next)
                    if len(_supported[may_fall]) == 0:                        
                        cnt += 1
                        to_fall.append(may_fall)
    print(cnt)
            




run()