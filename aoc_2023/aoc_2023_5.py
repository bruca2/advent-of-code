def __getMin(seeds, maps):
    for m in maps:
        v = []
        while seeds:
            s, e = seeds.pop()
            for rd, rs, rr in m:
                news = max(rs, s)
                newe = min(rs+rr, e)
                if news < newe:
                    v.append((news-rs+rd, newe-rs+rd))
                    if news > s:
                        seeds.append((s,news))
                    if newe < e:
                        seeds.append((newe,e))
                    break
            else:
                v.append((s,e))
        seeds = v
    print(min(seeds)[0])

def run():
    lines = open('input5.txt', 'r').read().splitlines()
    seeds1 = []
    seeds2 = []
    maps = []
    for line in lines:
        if line.startswith("seeds"):
            numbers = list(map(int, line.split(":")[1].split()))
            seeds1.extend((n,n+1) for n in numbers)
            seeds2.extend((numbers[n],numbers[n]+numbers[n+1]) for n in range(0,len(numbers),2))
        else:
            if line != "" and line[0].isdigit():
                cm.append([int(number) for number in line.split()])
            elif line != "":
                cm = []
                maps.append(cm)
    __getMin(seeds1, maps)
    __getMin(seeds2, maps)


