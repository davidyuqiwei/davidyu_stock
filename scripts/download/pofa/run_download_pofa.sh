source ~/.bashrc
cd `dirname $0`
sh wget_pofa.sh
python download_pofa.py 
rm -rf *.txt *.csv

