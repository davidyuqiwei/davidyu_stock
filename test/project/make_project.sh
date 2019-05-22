#!/usr/bin/sh
# create by davidyu
cd `dirname $0`
curr_dir=`pwd`

set -o nounset
help()
{
    cat <<- EOF
    Desc: the program is used for create folder for download, analysis
    Usage: ./make_project <download|>   <folder name>
    Author: Davidyu
    License: ...
EOF
    exit 0
}
if [ $# -lt 2 ]
 then 
   help
fi

if [ $1 = "download" ];then  
  echo "make download folder $2";
  mkdir -p $2/old
  echo -e "\n\n"
  echo "Start create folder"
  dir_path=$curr_dir/$2
  #------------------create file name --------------------#
  download_file_name="download_"$2".py"
  run_file_name="run_download_"$2".sh"
  tohve_file_name="to_hive.scala"
  #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  #---------------- create file name in the whole path -----------#
  download_file=$dir_path/$download_file_name
  run_file=$dir_path/$run_file_name
  tohive_file=$dir_path/$tohve_file_name
  #-----------------------------------------------------------#
  echo "create $2/$download_file_name"
  echo "create $2/$run_file_name"
  echo "create $2/$tohve_file_name"
  #--------------------- touch the file -----------------------#
  touch $download_file
  touch $run_file
  touch $tohive_file
  ##############################################################
  echo "create $2/"
#++++++++++++  create download file ++++++++++++++++++++++#
  cat > $download_file << EOF
import sys
import os
import pandas as pd
import time
import datetime



def download_data():

def check_data():

def process():

def main():
  sys.path.append("../..")
  dir_liutong_owner=data_dict.get("$2")
  stk_index_list=[x for x in stk_index_list if str(x).zfill(6)[0]!='3']
  k=0
  for stk in stk_index_list:
    stock_index=str(stk).zfill(6)
    try:
      process
    except:
      print(stock_index+'  not download')
      pass
if __name__ == '__main__':
  main()
EOF
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
echo -e "\n\n+++++++++++++++++++++++++++++++++++
***Before run scala, make sure create the table in hive***
++++++++++++++++++++++++++++++++++++++++++++++++\n\n"
#++++++++++++++++++++   create to hive script ++++++++++++++++++++++++++++++#
  cat > $tohive_file << EOF
System.out.println(System.getProperty("user.dir"))
val work_dir=System.getProperty("user.dir")
val data_file="file://"+work_dir+"/all.csv"

val table = "stock_dev.liutong_owner"
val sql1= s""" insert into table ++ select * from data_tr"""
println(sql1)
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

val csv_data = spark.read.csv(data_file)
csv_data.show()
csv_data.createOrReplaceTempView("data_tr")
sqlContext.sql(sql1)
EOF
#++++++++++++++++++++++ create run script ++++++++++++++++++++++++++
  cat > $run_file << EOF
#!/usr/bin/sh
cd \`dirname \$0\`
curr_dir=\`pwd\`
sep="_____"
programName={\${0##*/}  ### filename without type e.g.  test.sh  test
#echo \$programName
file_name=\${programName%.*} ## filename   'test.sh'
date_run=\`date +"%Y-%m-%d" \`
\`sh clean_dir.sh\`


python $download_file_name
if [ \$? -ne 0 ]; then
  echo "failed"\$sep\$curr_dir\$sep\$programName\$sep"python"\$date > \$script_log_path/\$file_name.log
else
  echo "succeed"\$sep\$curr_dir\$sep\$programName\$sep"python"\$date > \$script_log_path/\$file_name.log
  #nohup spark-shell  < \$curr_dir/to_hive.scala > \$curr_dir/scala.log 2>&1 &
fi

EOF
#############################################################################################


fi
