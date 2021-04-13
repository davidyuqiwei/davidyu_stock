cd `dirname $0`
curr_dir=`pwd`
cp -f /home/davidyu/software/Anaconda/lib/python3.7/site-packages/davidyu_cfg.py $curr_dir

cp -f ~/.bashrc $curr_dir"/system/bashrc"

cp -f ~/crontab_david.sh $curr_dir"/system"

cp -f /usr/davidyu/airflow/dags/*.py $curr_dir"/system/airflow_dag"
echo 'has make the copy'

cp -f -r /home/davidyu/stock/data/shiny_data/shell /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/shiny_data/shell
cp -f -r /home/davidyu/stock/data/shiny_data/sql /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/shiny_data/sql


## copy R shiny
cd /home/davidyu/stock/data/shiny_data/davidyu_stock
cp -f -r *.sh *.r $stock_script"/R_run/davidyu_stock"
cd /home/davidyu/stock/data/shiny_data/app/v1/
cp -f -r *.r *.R *.js* *.py $stock_script"/R_run/app/v1"

