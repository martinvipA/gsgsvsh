import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

scripts.append('6139676184.py')#2023-09-27 11:46:37.383624

scripts.append('6139676184.py')#2023-09-27 10:07:09.103608

scripts.append('6139676184.py')#2023-09-27 10:07:09.103608

scripts.append('6139676184.py')#2023-09-27 09:38:27.972511

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

