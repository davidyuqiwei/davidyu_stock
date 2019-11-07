import os 

def make_dir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
