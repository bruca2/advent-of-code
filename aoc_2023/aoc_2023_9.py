def run():
    lines = open('input9.txt', 'r').read().splitlines()    
    total1 = total2 = 0
    for line in lines:
        pyr = [[int(n) for n in line.split()]]
        while True:
            numbers = pyr[-1]
            newline = []
            for n in range(0, len(numbers)-1):
                newline.append(numbers[n+1]-numbers[n])            
            if all(n == 0 for n in newline):
                v1, v2 = 0, 0                
                for nl in reversed(pyr):                    
                    v1 += nl[-1]                                
                    v2 = nl[0] - v2                
                total1 += v1
                total2 += v2                
                break
            else:
                pyr.append(newline)                
    print(total1)
    print(total2)

