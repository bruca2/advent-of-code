from heapq import heappush, heappop

#node (distance to source, row, col, rowdir, coldir, straight steps)
def _sp(graph, source, dest_pos, min_steps, max_steps):    
    opp = {(0,1):(0,-1), (1,0):(-1,0),(0,-1):(0,1),(-1,0):(1,0)}
    pq = []
    v = set()
    heappush(pq, source)
    while pq:
        candir = set([(0,1),(1,0),(0,-1),(-1,0)])
        node = heappop(pq)                
        
        dist, row, col, rowdir, coldir, steps = node        
        if row == dest_pos[0] and col == dest_pos[1] and steps >= min_steps:
            return dist
        if (row, col, rowdir, coldir, steps) in v:
            continue
        v.add((row, col, rowdir, coldir, steps))
        
        if rowdir != 0 or coldir != 0:
            candir.remove(opp[(rowdir,coldir)])
        if steps == max_steps:            
            candir.remove((rowdir,coldir)) 
        if steps > 0 and steps < min_steps:
            candir = set([(rowdir,coldir)])
        for rd,cd in candir:
            new_pos_r,new_pos_c = row+rd,col+cd
            if not (len(graph) > new_pos_r >= 0 <= new_pos_c < len(graph[0])):
                continue
            new_steps = 1
            if rowdir == rd and coldir == cd:
                new_steps = steps + 1
            cost = graph[new_pos_r][new_pos_c]
            heappush(pq, (cost+dist,new_pos_r,new_pos_c,rd,cd,new_steps))
    
def run():    
    lines = open('input17.txt', 'r').read().splitlines()     
    graph = [[int(c) for c in row] for row in lines]
    print(_sp(graph, (0, 0, 0, 0, 0, 0), (len(graph)-1, len(graph[0])-1),1,3))
    print(_sp(graph, (0, 0, 0, 0, 0, 0), (len(graph)-1, len(graph[0])-1),4,10))
    