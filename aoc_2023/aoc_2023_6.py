def run():
    lines = open('input6.txt', 'r').read().splitlines()
    ts = lines[0].split(":")[1].split()
    ds = lines[1].split(":")[1].split()
    times =  [int(n) for n in ts]
    distances = [int(n) for n in ds]
    times.append(int(''.join(ts)))
    distances.append(int(''.join(ds)))
    # #quadratic solve solution
    total1 = 1
    total2 = 0
    for i, time in enumerate(times):
        u1 = (-time+(time*time-4*distances[i])**(0.5))/-2
        u2 = (-time-(time*time-4*distances[i])**(0.5))/-2    
        rec = abs(int(u2)-int(u1))  
        if i != len(times)-1:
            total1 *= rec
        else:
            total2 = rec
    print(total1)
    print(total2)

    #brute force solution
    # start = T.time()
    # total1 = 1
    # total2 = 0
    # for i, time in enumerate(times):
    #     rec = 0
    #     for k in range(time):
    #         if k*(time-k) > distances[i]:
    #             rec += 1
    #     if i != len(times)-1:
    #         total1 *= rec
    #     else:
    #         total2 = rec
    # print(total1)
    # print(total2)