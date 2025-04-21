from collections import defaultdict

def run():
    deps,lines = open("input5.txt", 'r').read().split("\n\n")  
    d = defaultdict(list)    
    for x in deps.split():
        src, tar = x.split('|')
        d[src].append(tar)
    s1, s2 = 0, 0    
    for line in lines.split():
        fine = True
        its = line.split(',')
        size = len(its)        
        for i in range(size):
            for n in range(i+1,size):
                if not (its[n] in d[its[i]]):
                    fine = False
                    break            
            if not fine:
                break
        if fine:            
            s1 += int(its[size//2])
        else:
            for i in range(size):                
                for n in range(size-1-i):
                    if its[n] in d[its[n+1]]:
                        its[n], its[n+1] = its[n+1], its[n]                                        
            s2 += int(its[size//2])

    print(s1)
    print(s2)
    