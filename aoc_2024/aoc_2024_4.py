def run():
    lines = open('input4.txt', 'r').read().split()  
    h,w = len(lines),len(lines[0])
    dirs = ( (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1) )
    ser, sec, swr, swc = 1,1,1,-1
    cmbs = ('MASMAS','MASSAM','SAMMAS','SAMSAM')
    cnt1, cnt2 = 0, 0
    for r in range(h):
        for c in range(w):
            for dr,dc in dirs:                
                if 0 <= r+3*dr < h and 0 <= c+3*dc < w:
                    if lines[r][c] == 'X' and lines[r+dr][c+dc] == 'M' and lines[r+2*dr][c+2*dc] == 'A' and lines[r+3*dr][c+3*dc] == 'S':
                        cnt1 += 1
            if 0 <= r+2*ser < h and 0 <= c+2*sec < w and 0 <= r+2*swr < h and 0 <= c+2*swc+2 < w:
                for cmb in cmbs:
                    if lines[r][c] == cmb[0] and lines[r+ser][c+sec] == cmb[1] and lines[r+2*ser][c+2*sec] == cmb[2] and lines[r][c+2] == cmb[3] and lines[r+swr][c+swc+2] == cmb[4] and lines[r+2*swr][c+2*swc+2] == cmb[5]:
                        cnt2 += 1                
    print(cnt1)
    print(cnt2)
