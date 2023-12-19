_paths = []

def _count(partsStr,conds):
    S = 0
    for part in partsStr:
        part = part.split(',')            
        x,m,a,s = [int(p.split('=')[1]) for p in part]
        insList = conds['in']
        while True:
            if insList == 'A':
                S += x+m+a+s
                break
            elif insList == 'R':
                break
            for ins in insList.split(','): 
                if ':' in ins:
                    expr = ins.split(':')
                    r = eval(expr[0])
                    if r:
                        insList = conds[expr[1]]
                        break
                else:
                    insList = conds[ins]
                    break
    return S
    
def _dfs(g, s, curr):        
    insList = g[s]
    
    if insList == 'A':        
        _paths.append(curr)
        return
    if insList == 'R':
        return

    for ins in insList.split(','): 
        if ':' in ins:
            expr = ins.split(':')
            _dfs(g,expr[1],curr + "," + expr[0])
            if '>' in expr[0]:
                newexpr = expr[0].replace('>','<=')
            else:
                newexpr = expr[0].replace('<','>=')
            curr = curr + "," + newexpr
        else:
            _dfs(g,ins, curr)            

def run():    
    lines = open('input19.txt', 'r').read().split('\n\n')   
    condsStr,partsStr = lines[0].split(),lines[1].replace('{','').replace('}','').split()
    conds = {}
    for condStr in condsStr:
        name,cond = condStr.split('{')
        conds[name] = cond.replace('}','')        
    conds['A'] = 'A'
    conds['R'] = 'R'

    print(_count(partsStr, conds))
    
    _dfs(conds, 'in', '')
    total = 1
    for path in _paths:
        path = path.lstrip(',').replace('(,','(')    
        simp = {l:set([i for i in range(1,4001)]) for l in "xmas"}    
        for expr in path.split(','):
            if '<=' in expr:
                expr = expr.split('<=')
                simp[expr[0]] = simp[expr[0]].intersection(set([i for i in range(1,int(expr[1])+1)]))
            elif '>=' in expr:
                expr = expr.split('>=')
                simp[expr[0]] = simp[expr[0]].intersection(set([i for i in range(int(expr[1]),4001)]))
            if '<' in expr:
                expr = expr.split('<')
                simp[expr[0]] = simp[expr[0]].intersection(set([i for i in range(1,int(expr[1]))]))
            elif '>' in expr:
                expr = expr.split('>')
                simp[expr[0]] = simp[expr[0]].intersection(set([i for i in range(int(expr[1])+1,4001)]))
        
        temp = 1
        for v in simp.values():
            temp *= len(v)
        total += temp
    print(total-1)