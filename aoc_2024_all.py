import os
import importlib.util
import time as T
import matplotlib.pyplot as plt

scripts_folder = os.path.dirname(__file__) + "/aoc_2024"
os.chdir(scripts_folder)

script_files = [f for f in os.listdir(scripts_folder) if f.endswith('.py')]

plt.xlabel('Problem number')
plt.ylabel('Time (ms)')
plt.title('AOC 2024 solving times')

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
        print(f'Elapsed {elapsed:.2f} ms')
        print('========================================')
        times.append(elapsed)
    else:
        print(f"Script {module_name} does not have a callable 'run' method.")

r = range(1,len(script_files)+1)
plt.xticks(r)
plt.scatter(r,times)
plt.plot(r,times)
output_image = "aoc_2024_all.png"
plt.savefig(output_image)

import subprocess
subprocess.run(['xdg-open', output_image])
