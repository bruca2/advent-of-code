def __mmc(a,b):
    ret = a*b    
    while a%b:
        a, b = b, a % b
    return ret//b
        
def run():
    A = []
    lines = open('input8.txt', 'r').read().splitlines()    
    steps = lines[0]
    m = {}
    for line in lines[2:]:
        s, d = line.split(' = ')        
        if s[2] == 'A':
            A.append(s)
        a, b = d.replace('(','').replace(')','').strip().split(', ')
        m[s] = (a,b)
        
    steps2 = 1
    for e in A:
        current = e
        step = 0
        cnt = 0        
        while current[2] != 'Z':
            cnt += 1
            if steps[step] == 'L':
                current = m[current][0]
            else:
                current = m[current][1]
            step = (step + 1) % len(steps)        
        steps2 = __mmc(steps2, cnt)
        if e == 'AAA' and current == 'ZZZ':
            steps1 = cnt
    print(steps1)
    print(steps2)

    #check loops
    # for e in A:
    #     current = e
    #     step = 0        
    #     print(current, end=' ')
    #     firstZ = (None,None)
    #     while True:             
    #         cnt = 0      
    #         while cnt == 0 or current[2] != 'Z':
    #             cnt += 1
    #             current = m[current][0 if steps[step] == 'L' else 1]
    #             step = (step+1)%len(steps)
    #         print((current,step,cnt), end=' ')
    #         if firstZ == (None,None):
    #             firstZ = (current,step)
    #         elif (current,step) == firstZ:
    #             print()                
    #             break
    