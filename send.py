import os 
import shutil
import subprocess
#os.chdir('states')
src='represent_2.py'
src=os.path.abspath(src)
p=os.listdir()
print(p)

for i in p:
    if i==src or i=='send.py' or i=='represent.py' or i=='represent_2.py': continue
    else:
        dest=f'{i}'
        os.chdir(dest)
        subprocess.call(['python',src])
        os.chdir("..")
        
    