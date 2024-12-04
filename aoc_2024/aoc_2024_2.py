def check(ls):
    for l in ls:
        d = [l[i] - l[i+1] for i in range(len(l)-1)]        
        if all(map(lambda x: x >= 1 and x <= 3, d)) or all(map(lambda x: x >= -3 and x <= -1, d)):
            return 1
    return 0                

def run():
    lines = open('input2.txt', 'r').readlines()
    s1, s2 = 0, 0
    for line in lines:        
        r = [int(v) for v in line.split()]
        ls = []
        ls.append(r)
        s1 += check(ls)
        for i in range(len(r)):
            t = r.copy()
            del t[i]
            ls.append(t)        
        s2 += check(ls)
    
    print(s1)
    print(s2)
    