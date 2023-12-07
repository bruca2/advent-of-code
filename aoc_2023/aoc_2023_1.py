def run():
    lines = open('input1.txt', 'r').readlines()
    total = digitsTotal = 0
    value = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
    value.update({str(k):k for k in range(1,10)})
    for line in lines:
        digits = []
        for ch in line:
            if ch.isdigit():
                digits.append(ch)
        digitsTotal = digitsTotal + int(digits[0]+digits[-1])    
        minIdx = len(line)
        maxIdx = -1
        for k,v in value.items():
            minfind, maxfind = line.find(k), line.rfind(k)
            if minfind != -1 and minfind < minIdx:
                minIdx = minfind
                fd = v     
            if maxfind > maxIdx:
                maxIdx = maxfind
                sd = v
        total = total + fd*10 + sd
    print(digitsTotal)
    print(total)