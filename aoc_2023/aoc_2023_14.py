def _damage(state):
    cnt = 0
    length = len(state)
    for irow,row in enumerate(state):                
        for col in row:            
            if col == 'O':
                cnt += length-irow
    return cnt

def _transpose(lines):
    return [''.join(c) for c in zip(*lines)]                

def _cycling(new_lines, turns = 4):    
    for _ in range(turns):
        lines = _transpose(new_lines)
        new_lines = []
        for line in lines:
            splitted = line.split('#')
            rolled = [''.join(reversed(sorted(s))) for s in splitted]
            new_lines.append('#'.join(rolled))
        if turns == 4:
            new_lines = [line[::-1] for line in new_lines]
        lines = new_lines                
    return tuple(new_lines)
        
def run():    
    lines = open('input14.txt', 'r').read().splitlines()   
    print(_damage(_transpose(_cycling(lines, 1))))
    v = set(lines)
    history = [lines]
    cycle_nr = 0
    while True:
        cycle_nr += 1
        lines = _cycling(lines)        
        if lines in v:            
            start = history.index(lines)            
            break
        v.add(lines)
        history.append(lines)    
    rem = (1000000000-start) % (cycle_nr-start) + start    
    print(_damage(history[rem]))

