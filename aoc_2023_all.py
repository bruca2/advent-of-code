import os
import os.path
import time as T
import aoc_2023
import matplotlib.pyplot as plt

class t:
    def startTime(self):
        self.start = T.time()        
    
    def printTime(self):
        elapsed = (T.time()-self.start)*1000
        print(f'Elapsed {elapsed:.0f} ms')
        return elapsed
    
    def plotTime(self, T):
        X = range(1,len(aoc_2023.__all__)+1)
        plt.xlabel('Problem number')
        plt.ylabel('Time (ms)')
        plt.title('AOC 2023 solving times')
        plt.scatter(X,T)
        plt.show()

days = map(aoc_2023.__dict__.get, aoc_2023.__all__)
times = []

cl = t()
cl.startTime()

for day in days:
    cd = t()
    cd.startTime()
    print(f'Day {day.__name__}')
    os.chdir(os.path.dirname(day.__file__))
    day.run()
    elapsed = cd.printTime()
    print('========================')
    times.append(elapsed)
    
print('Total:',end='')
cl.printTime()
cl.plotTime(times)
