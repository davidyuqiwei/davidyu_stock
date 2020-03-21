while read -r line
do
    python parse_url.py $line
done < url_list.sh
