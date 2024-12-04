import re

def run():
    lines = open('input3.txt', 'r').read()

    v = 0    
    l = re.findall('mul\((\d{1,3})\,(\d{1,3})\)', lines)
    for t in l:
        v += int(t[0])*int(t[1])
    print(v)
    
    v = 0
    state = True    
    lastState = False
    while lastState != state:
        lastState = state         
        if state:
            x = lines.find("don't()")   
            l = re.findall('mul\((\d{1,3})\,(\d{1,3})\)', lines[:x] if x > -1 else lines)
            for t in l:
                v += int(t[0])*int(t[1])          
            if x > -1:                
                state = False
                lines = lines[x:]
        else:
            x = lines.find("do()")
            if x > -1:
                lines = lines[x:]
                state = True                    
    print(v)
    