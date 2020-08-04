source ~/.bashrc
cd `dirname $0`
folder=$1
sh combine_data.sh $folder
#python clean_data.py

