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
    total = 0
    for path in _paths:
        minValues = {'x':1,'m':1,'a':1,'s':1}
        maxValues = {'x':4000,'m':4000,'a':4000,'s':4000}
        path = path.lstrip(',').replace('(,','(')    
        for expr in path.split(','):                        
            if '>=' in expr:
                sp = expr.split('>=')
                minValues[sp[0]] = max(minValues[sp[0]], int(sp[1]))            
            elif '<=' in expr:
                sp = expr.split('<=')
                maxValues[sp[0]] = min(maxValues[sp[0]], int(sp[1]))
            elif '>' in expr:
                sp = expr.split('>')
                minValues[sp[0]] = max(minValues[sp[0]], int(sp[1])+1)
            elif '<' in expr:
                sp = expr.split('<')
                maxValues[sp[0]] = min(maxValues[sp[0]], int(sp[1])-1)
        temp = 1
        for l,u in zip(minValues.values(),maxValues.values()):
             temp *= u-l+1
        total += temp
    print(total)
    