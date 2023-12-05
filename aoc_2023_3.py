import re
from collections import defaultdict

m = open('input.txt', 'r').read().splitlines()
starmap = defaultdict(set)
total = 0
dir = ((-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1, 1), (1, 1), (1, -1))
for row, l in enumerate(m):
    matches = re.finditer("\d+", l)
    for match in matches:
        found = False
        span = match.span()        
        for ch in range(span[0], span[1]):
            for r,c in dir:                
                if row+r < 0 or row+r >= len(m) or ch+c < 0 or ch+c >= len(l):
                    continue
                if m[row+r][ch+c] == "*":
                    starmap[(row+r,ch+c)].add((row,span))                   
                if not m[row+r][ch+c].isdigit() and m[row+r][ch+c] != ".":                    
                    found = True                    
        if found:        
            total = total + int(match.group(0))
print(total)
r = 0
for k,v in starmap.items():
    if len(v) == 2:
        l = list(v)
        n1,n2 = l[0], l[1]
        r = r + int(m[n1[0]][n1[1][0]:n1[1][1]])*int(m[n2[0]][n2[1][0]:n2[1][1]])
print(r)


