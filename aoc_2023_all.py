import os
import importlib.util
import time as T
import matplotlib.pyplot as plt
import re

def sorter(s):
    match = re.search(r'_(\d+).py', s)
    return int(match.group(1)) if match else float('inf')

scripts_folder = os.path.dirname(__file__) + "/aoc_2023"
os.chdir(scripts_folder)

script_files = [f for f in os.listdir(scripts_folder) if f.endswith('.py')]
script_files = sorted(script_files, key=sorter)

plt.xlabel('Problem number')
plt.ylabel('Time (ms)')
plt.title('AOC 2023 solving times')

times = []
for script_file in script_files:
    script_path = os.path.join(scripts_folder, script_file)
    module_name = os.path.splitext(script_file)[0]
    
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    module = importlib.util.module_from_spec(spec)    
    spec.loader.exec_module(module)
        
    if hasattr(module, 'run') and callable(module.run):
        print(f"{module_name}")
        start = T.time()      
        module.run()        
        elapsed = (T.time()-start)*1000
        print(f'Elapsed {elapsed:.0f} ms')
        print('========================================')
        times.append(elapsed)
    else:
        print(f"Script {module_name} does not have a callable 'run' method.")

r = range(1,len(script_files)+1)
plt.xticks(r)
plt.scatter(r,times)
plt.plot(r,times)
output_image = "aoc_2023_all.png"
plt.savefig(output_image)

import subprocess
subprocess.run(['xdg-open', output_image])