import sys
import os
def parse_url_list(input_in):
    try:
        name = input_in.split(";")[0]
        url = input_in.split(";")[1]
        #print("name++++"+name)
        #print("url+++++"+url)
        cmd_out = "sh wget_important_owner_to_df.sh '%s' '%s' "%(url,name)
        #print("cmd ++++++++++++++++"+cmd_out)
        #os.system(cmd_out)
        return cmd_out
    except:
        print("url error")
        sys.exit(2)
input_in = sys.argv[1]
cmd_out = parse_url_list(input_in)
os.system(cmd_out)
