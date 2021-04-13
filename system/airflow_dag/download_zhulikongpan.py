"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
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
    'a_download_zhulikongpan', 
    default_args=default_args, 
    schedule_interval="30 06 * * *")

# t1, t2 and t3 are examples of tasks created by instantiating operators
#task_download_zhulikongpan="/home/davidyu/stock/scripts/davidyu_stock/scripts/download/zhulikongpan/run_main_zhulikongpan.sh "
task_zhulikongpan_stat1="/home/davidyu/stock/data/shiny_data/python/zhulikongpan/run_shiny_zhulikongpan.sh "

'''
task_download_zhulikongpan =  BashOperator(
    task_id='download_zhulikongpan',
    bash_command=task_download_zhulikongpan,
    dag=dag)

'''


t_zhulikongpan_stat1= BashOperator(
    task_id='zhulikongpan_stat1',
    bash_command=task_zhulikongpan_stat1,
    dag=dag)

t_zhulikongpan_stat1
