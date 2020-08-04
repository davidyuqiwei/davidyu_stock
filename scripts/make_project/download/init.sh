source ~/.bashrc
cd `dirname $0`
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"
#echo $project_path

echo $project_name
newShell="run_main_"$project_name".sh"

#mv run_download.sh "run_download_"$project_name".sh"
sed -r 's/PROJECTNAME/'$project_name'/g' run_download.sh > $newShell
sed -i 's/PROJECTNAME/'$project_name'/g' touchDIR.sh 
sed -i 's/PROJECTNAME/'$project_name'/g' ./clean_data/combine_data.sh
sed -i 's/PROJECTNAME/'$project_name'/g' to_hive/run_to_hive.sh

sh touchDIR.sh


rm -rf init.sh run_download.sh touchDIR.sh
echo "/home/davidyu/stock/scripts/davidyu_stock/scripts/make_project/download"


