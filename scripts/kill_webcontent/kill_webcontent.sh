source ~/.bashrc
cd `dirname $0`

ps -ef | grep "firefox -contentproc" --color=never |  awk '{print $2}' > pidfile.txt


for line in `cat pidfile.txt`
do
    `kill $line`
done


