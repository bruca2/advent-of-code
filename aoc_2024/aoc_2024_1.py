def run():
    lines = open('input1.txt', 'r').readlines()    
    a, b = [sorted(l) for l in zip(*(line.strip().split('   ') for line in lines))]
    print(sum([abs(int(a[i])-int(b[i])) for i in range(len(a))]))
    print(sum([abs(int(a[i])*b.count(a[i])) for i in range(len(a))]))
