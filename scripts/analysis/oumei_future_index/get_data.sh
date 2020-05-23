cd /home/davidyu/stock/data/oumei_future_index
find -iname *txt | xargs cat | grep "," > a.log
