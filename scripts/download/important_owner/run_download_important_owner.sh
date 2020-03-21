source ~/.bashrc
cd `dirname $0`
while read -r line
do
    python parse_url.py $line
    sleep 2s
done < url_list.sh
rm -rf data.txt
