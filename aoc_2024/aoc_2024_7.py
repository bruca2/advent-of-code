from itertools import product

def run():
    combs_m = [{},{}]
    lines = open("input7.txt", 'r').read().split('\n')
    t1 = t2 = 0    
    for line in lines:        
        cnt = -1        
        rt, ost = line.split(':')
        b = ost.split()
        r,os = int(rt),[int(o) for o in b]      
        nos = len(os)        
        br = False                
        while cnt<1:
            if br:
                break
            cnt += 1
            if nos in combs_m[cnt]:                
                combs = combs_m[cnt][nos]
            else:                   
                combs = combs_m[cnt][nos] = [p for p in product(('+','*','|') if cnt == 1 else ('+','*'), repeat=nos-1)]
            for comb in combs:    
                res = os[0]                
                for i in range(1,nos):
                    if comb[i-1] == '+':
                        res += os[i]
                    elif comb[i-1] == '*':
                        res *= os[i]                        
                    else:
                        res = int(str(res)+b[i])                    
                if res == r:      
                    if cnt == 0:                                       
                        t1 += r                                                                                       
                    else:
                        t2 += r
                    br = True
                    break                              
    print(t1)
    print(t1+t2)    

