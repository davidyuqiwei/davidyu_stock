source ~/.bashrc
cd `dirname $0`
cat ../url_list/* > url_list.sh
while read -r line
do
    python parse_url.py $line
    sleep 2s
done < url_list.sh
rm -rf data.txt
