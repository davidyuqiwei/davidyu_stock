cd `dirname $0`
curr_dir=`pwd`
cp -f /home/davidyu/software/Anaconda/lib/python3.7/site-packages/davidyu_cfg.py $curr_dir

cp -f ~/.bashrc $curr_dir"/system/bashrc"

echo 'has make the copy'

