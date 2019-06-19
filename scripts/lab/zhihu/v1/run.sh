for i in {0..1000}
do 
    echo $i
    sed -r 's/k=[0-9]/k='$(echo $i)'/g' download_v1.py > to_download.py
    python to_download.py
    sleep 3s
done
