source ~/.bashrc
cd `dirname $0`
python download_pofa.py
rm -rf geckodriver.log
