import os
## get the unique text file in the folder
def get_text(current_dir):
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    #print(current_dir)
    files = os.listdir(current_dir)
    file_in = [x for x in files if 'txt' in x][0]
    text_file = file_in
    file_name_raw = file_in.split(".")[0]
    return text_file,file_name_raw


