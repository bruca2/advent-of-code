import time as T
from aoc_2023 import *

class t:
    def startTime(self):
        self.start = T.time()        
    
    def printTime(self):
        print(f'Elapsed {(T.time()-self.start)*1000} ms')

cl = t()
cl.startTime()
for day in range(1,8):
    cd = t()
    cd.startTime()
    print(f'Day{day}')
    eval(f'aoc_2023_{day}.run()')
    cd.printTime()
    print('========================')
    
print('Total:',end='')
cl.printTime()
