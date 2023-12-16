from collections import deque

def _search(beams, tiles):
    left,right,up,down = (0,-1),(0, 1),(-1,0),(1,0)
    beam_dir = {
                '\\': {right:down,left:up,down:right,up:left},
                '/': {right:up,left:down,down:left,up:right}
               }
    #m = [['.']*len(tiles[0]) for _ in range(len(tiles))]
    v = set()
    energized = set()
    while beams:
        beam = beams.pop()                
        pos,dir = beam[0], beam[1]
        row,col,rowd,cold = pos[0],pos[1],dir[0],dir[1]
        rown, coln = row+rowd,col+cold
        posn = rown, coln
        if (not len(tiles) > rown >= 0 <= coln < len(tiles[0])) or (posn,dir) in v:
            continue               
        else:                
            v.add((posn,dir))                
            energized.add(posn)
            #m[posn[0]][posn[1]] = '#'
            tile = tiles[rown][coln]
            if tile == '.':
                beams.appendleft((posn,dir))
            elif tile == '|':
                if dir == down or dir == up:
                    beams.appendleft((posn,dir))
                else:
                    beams.appendleft((posn,up))
                    beams.appendleft((posn,down))
            elif tile == '-':
                if dir == left or dir == right:
                    beams.appendleft((posn,dir))
                else:
                    beams.appendleft((posn,left))
                    beams.appendleft((posn,right))
            else:            
                beams.appendleft((posn,beam_dir[tile][(rowd,cold)]))
    # for l in m:
    #     for c in l:
    #         print(c,end='')
    #     print()
    return len(energized)

def run():    
    tiles = open('input16.txt', 'r').read().splitlines()     
    pt2 = -1
    for col in range(len(tiles[0])):
        pt2 = max(pt2,_search(deque([((-1,col),(1,0))]), tiles))
        pt2 = max(pt2,_search(deque([((len(tiles),col),(-1,0))]), tiles))
    for row in range(len(tiles)):    
        en = _search(deque([((row,-1),(0,1))]), tiles)
        if row == 0:
            pt1 = en
        pt2 = max(pt2, en)
        pt2 = max(pt2,_search(deque([((row,len(tiles[0])),(0,-1))]), tiles))
    print(pt1)
    print(pt2)
    
    