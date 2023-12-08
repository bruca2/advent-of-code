from collections import defaultdict
from functools import cmp_to_key

cards = {}

def __get_type(h):
    labels = defaultdict(int)
    for c in h:
        labels[c] += 1
    if len(labels) == 1:
       return 7
    elif len(labels) == 2:
        if any(v == 4 for v in labels.values()):
            return 6
        else:
            return 5
    elif len(labels) == 3:
        if any(v == 3 for v in labels.values()):
            return 4
        else:
            return 3
    elif len(labels) == 4:
        return 2
    else:
        return 1

def __sorter(hv1,hv2):    
    if hv1[1] > hv2[1]:
        return 1
    elif hv2[1] > hv1[1]:
        return -1    
    for i in range(5):
        if hv1[0][i] == hv2[0][i]:
            continue
        return cards[hv1[0][i]]-cards[hv2[0][i]]
    return 0

def __replacements(hand):
    cnt = defaultdict(int)
    for c in hand:
        cnt[c]+=1
    if len(cnt) == 1 and hand[0] == 'J':
        return ['AAAAA'] 
    else:
        l = list(cnt.items())    
        l.sort(key=lambda x: x[1])
        return [hand.replace('J',c[0]) for c in l]
    
def run():
    global cards
    lines = open('input7.txt', 'r').read().splitlines()    
    hands = []
    bids = {}
    for line in lines:
        h, b = line.split()
        hands.append(h)
        bids[h] = int(b)

    for part in range(2):
        if part == 0:
            cards = {c:i for i,c in enumerate('23456789TJQKA')}
        else:
            cards = {c:i for i,c in enumerate('J23456789TQKA')}
        typ = []
        for h in hands:
            if part == 1 and 'J' in h:
                J = []
                reps = __replacements(h)
                for r in reps:
                    J.append((h, __get_type(r)))        
                J.sort(key=cmp_to_key(__sorter))                
                typ.append(J[-1])
            else:          
                typ.append((h,__get_type(h)))

        typ.sort(key=cmp_to_key(__sorter))        
        r = 1
        total = 0
        for t in typ:
            total += r*bids[t[0]]
            r+=1
        print(total)