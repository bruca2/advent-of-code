from collections import defaultdict
from collections import deque

class action:
    def __init__(self, source, pulse, sink):
        self.source = source
        self.pulse = pulse
        self.sink = sink
    def __str__(self):
        return f'{self.source} -{self.pulse}->{self.sink}'
        
def _lcm(a,b):
    ret = a*b    
    while a%b:
        a,b = b,a%b
    return ret//b

def run():    
    mods = defaultdict(list)
    types = defaultdict(str)
    mem_conj = defaultdict(lambda: defaultdict(int)) #must be dictionary of dictionary {modulename:{inputname:value}}
    mem_ff = defaultdict(int)
    q = deque()
    lines = open('input20.txt', 'r').read().splitlines()
    for line in lines:
        mod, outs = line.split(' -> ')        
        outs = [o.strip() for o in outs.split(',')]
        for out in outs:
            if out == 'rx':
                inp = mod[1:]
            if 'broadcaster' in mod:
                mods[mod].append(out)
                mem_conj[out][mod] = 0
            else:
                types[mod[1:]] = mod[0]        
                mods[mod[1:]].append(out)          
                mem_conj[out][mod[1:]] = 0
    for mod,typ in types.items():
        if typ == '%':
            del mem_conj[mod]
    conj_size = len(mem_conj[inp])    
    conj_cycles = {}
    low = high = 0    
    i = 0
    found = False
    while not found:
        i += 1
        q.appendleft(action('button', 0, 'broadcaster'))            
        while q:
            a = q.pop()
            if a.pulse == 0:
                low +=1
            else:   
                high += 1
            if a.sink == 'rx':
                for mod,v in mem_conj[inp].items():
                    if v == 1:
                        conj_cycles[mod] = i
                    if conj_size == len(conj_cycles):                                                
                        cycles = list(conj_cycles.values())
                        value = cycles[0]
                        for k in range(1,conj_size):
                            value = _lcm(value, cycles[k])
                        print(value)
                        found = True
                        break
            if found:
                break                        
            if 'broadcaster' in a.sink:
                new_pulse = a.pulse
            elif types[a.sink] == '%':
                if a.pulse == 0:
                    mem_ff[a.sink] = 0 if mem_ff[a.sink] == 1 else 1
                    new_pulse = mem_ff[a.sink]
                else:
                    continue
            else:
                mem_conj[a.sink][a.source] = a.pulse
                new_pulse = 0 if all(v == 1 for v in mem_conj[a.sink].values()) else 1
            for new_sink in mods[a.sink]:
                q.appendleft(action(a.sink, new_pulse, new_sink))
        if i == 1000:
            print(low*high)
            