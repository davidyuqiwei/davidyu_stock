import os


## get the unique text file in the folder

def get_uni_textfile(current_dir=None):
    if current_dir is None:
        current_dir = "./"
    files = os.listdir(current_dir)
    file_in = [x for x in files if 'txt' in x][0]
    return_data = {'text_file_name': file_in, 'text_raw_name': file_in.split(".")[0]}
    return return_data
