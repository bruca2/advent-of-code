def _canfix(l1,l2):
    diffs = 0
    for idx in range(len(l1)):
        if l1[idx] != l2[idx]:
            diffs += 1            
            if diffs > 1:    
                return False
    return True

def _find(block,smudge = False):
    cnt = 0
    found = False                
    for i in range(len(block)-1):                                    
        smudgeFixed = False
        ii,jj = i,i+1
        while ii >= 0 and jj < len(block):
            if block[ii] != block [jj]:
                if smudge and _canfix(block[ii], block[jj]) and not smudgeFixed:
                    smudgeFixed = True
                else:
                    break
            ii-=1
            jj+=1
        else:
            if not smudge or (smudge and smudgeFixed):
                found = True
                cnt = i+1      
            else:
                found = False
        if found: break
    return cnt

def run():
    blocks = open('input13.txt', 'r').read().split('\n\n')
    n_blocks = [block.splitlines() for block in blocks]        
    tr_blocks = [[''.join(x) for x in zip(*block)] for block in n_blocks]    
    total1 = total2 = 00
    for i in range(len(n_blocks)):
        hor = _find(n_blocks[i])
        ver = _find(tr_blocks[i])
        total1 += hor*100 + ver
        hor = _find(n_blocks[i], True)
        ver = _find(tr_blocks[i], True)
        total2 += hor*100 + ver
    print(total1)
    print(total2)




