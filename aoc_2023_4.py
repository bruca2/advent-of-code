from collections import defaultdict

cards = open('input.txt', 'r').read().splitlines()
total = 0
d = defaultdict(int)
for card, line in enumerate(cards):
    numbers = line.split(":")[1]
    W, N = numbers.split("|")    
    d[card] += 1
    points = 0   
    matching = 0            
    W = [int(w) for w in W.split()]
    N = [int(n) for n in N.split()]
    for n in N:        
        if n in W:            
            matching += 1
            points *= 2
            if points == 0:
                points = 1          
    total += points   
    for i in range(matching):
        d[card+i+1] += d[card]
print(total)
print(sum(d.values()))





