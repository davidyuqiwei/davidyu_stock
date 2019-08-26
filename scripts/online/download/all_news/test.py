import os
script_dir = os.path.split(os.path.realpath(__file__))[0]
os_str = "rm -rf %s/*.log" %script_dir
print(os_str)
os.system(os_str)
