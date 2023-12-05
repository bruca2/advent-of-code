from collections import defaultdict

lines = open('input.txt', 'r').readlines()
colorsLimit = {"blue":14, "red":12, "green":13}
ids = powersum = 0
for game, line in enumerate(lines,1):    
    line = line.split(":")[1]    
    ok = True
    maxColors = defaultdict(int)
    for s in line.split(";"):        
        for cubes in s.split(", "):
            number, color = cubes.split()    
            maxColors[color] = max(maxColors[color], int(number))                    
            if int(number) > colorsLimit[color]:
                ok = False
    powersum = powersum + maxColors["blue"]*maxColors["red"]*maxColors["green"]
    if ok:
        ids = ids + game
print(ids)
print(powersum)
