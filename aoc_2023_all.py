import os
import os.path
import time as T
import aoc_2023

class t:
    def startTime(self):
        self.start = T.time()        
    
    def printTime(self):
        print(f'Elapsed {(T.time()-self.start)*1000:.0f} ms')

days = map(aoc_2023.__dict__.get, aoc_2023.__all__)

cl = t()
cl.startTime()

for day in days:
    cd = t()
    cd.startTime()
    print(f'Day {day.__name__}')
    os.chdir(os.path.dirname(day.__file__))
    day.run()
    cd.printTime()
    print('========================')
    
print('Total:',end='')
cl.printTime()
