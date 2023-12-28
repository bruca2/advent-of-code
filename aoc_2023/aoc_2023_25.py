from collections import defaultdict, deque

_freq = defaultdict(int)
_dist = defaultdict(int)

def _bfs(g,s,v,d=None):   
    v.add(s)
    q = deque([(s,0)])
    while q:
        item = q.pop()
        if item[0] == d:
            return
        for conn in g[item[0]]:
            if conn not in v:
                _freq[f'{item[0]},{conn}'] += 1
                _dist[f'{s},{conn}'] = item[1]+1
                q.appendleft((conn,item[1]+1))
                v.add(conn)

def run():   
    g = defaultdict(list)
    lines = open('input25.txt', 'r').read().splitlines()
    for line in lines:
        key,values = line.split(':')
        values = values.split()
        g[key].extend(values)
        for value in values:
            g[value].append(key)
    
    #compute distance between all pairs
    for st in g.keys():
        _bfs(g,st,set())
   
    #compute edge freq (in _freq variable) for the 200 most distanced pairs (instead of all pairs)
    #200 was chosen as it's ~10% of the real input size, and it worked for the sample input
    #the heuristic is that the most distant pairs have a large probability to cross one of the bridges
    #and have a valid contribution for the frequency
    sorted_dist = sorted(tuple(_dist.items()), key=lambda x:-x[1])
    _freq.clear()
    for i in range(200):
        s,d = sorted_dist[i][0].split(',')
        _bfs(g,s,set(),d)

    #merge (s,d) and (d,s) pairs
    freqs = tuple(_freq.items())
    merged_freqs = []
    for i in range(len(freqs)):
        s,d = freqs[i][0].split(',')
        value = freqs[i][1]
        for k in range(i+1, len(freqs)):
            ks,kd = freqs[k][0].split(',')
            if ks == d and kd == s:
                value += freqs[k][1]
                break
        merged_freqs.append((f'{s},{d}',value))

    #remove bridges    
    top = sorted(merged_freqs, key=lambda x:-x[1])[:3]
    for item in top:
        s,d = item[0].split(',')
        g[s].remove(d)
        g[d].remove(s)
    
    #get size of one of the disconnected parts, starting from a random node
    #and multiply it by the remaining size
    comps = set()
    _bfs(g,list(g.keys())[0],comps)
    print(len(comps)*(len(g.keys())-len(comps)))

    