import pandas as pd
import argparse
import os 
parser = argparse.ArgumentParser()
parser.add_argument("-f",type=str,help="the csv need to transform to xlsx")
args = parser.parse_args()
input_file = args.f

output_file = input_file.replace("csv","xlsx")
df1 = pd.read_csv(input_file,sep="\t")
col_name = df1.columns.tolist()
new_col_name = [x.split(".")[1] for x in col_name]
df1.columns = new_col_name
os.system("rm -rf "+ output_file)
df1.to_excel(output_file,index=0,encoding="utf_8_sig")
df1.to_csv(input_file,index=0,encoding="utf_8_sig")

#os.system("chmod 777 "+output_file)

