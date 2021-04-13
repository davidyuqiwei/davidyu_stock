"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""

"""
达安基因,多个概念领涨股_食品安全_高校北京,2021-01-13
华泰证券，含GDR概念，2021-01-13
中公教育,macd连续低位,2021-01-14
鲁抗医药, macd<0,rsi<25,2020-01-20
002481,人造肉, 2021-01-28
002191,es_电子烟_keyword,2021-02-02
300014,es_电子烟_keyword,2021-02-02
000800,一起解放_多家机构调研_qf2重仓,2021-02-17








----------------------------------------------------------------------
----------------------------------------------------------------------
https://www.investopedia.com/
"""


from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import airflow
now = datetime.now()
run_time1 = now - timedelta( hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond )
run_time = run_time1 - timedelta(days=1)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': run_time,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'a_select_stock', 
    default_args=default_args, 
    schedule_interval="30 01 * * *")

tt_task_stock_index_trade_day="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/SH_index/shell/spark_SH_index_trade_date.s "
t_stock_index_trade_day= BashOperator(
    task_id='stock_index_trade_day',
    bash_command=tt_task_stock_index_trade_day,
    dag=dag)
