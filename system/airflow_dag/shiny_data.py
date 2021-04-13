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
    'a_shiny_data', 
    default_args=default_args, 
    schedule_interval="30 01 * * *")

# t1, t2 and t3 are examples of tasks created by instantiating operators
task_shiny_all_data="/home/davidyu/stock/data/shiny_data/shell/run_all.sh "
task_vol_price_distr="/home/davidyu/stock/data/shiny_data/shell/run_vol_price_distr.sh "

t_shiny_all_data =  BashOperator(
    task_id='shiny_run_all_data',
    bash_command=task_shiny_all_data,
    dag=dag)


t_shiny_vol_price_distr= BashOperator(
    task_id='shiny_vol_price_distr',
    bash_command=task_vol_price_distr,
    dag=dag)

t_shiny_all_data >> t_shiny_vol_price_distr
#>> t_shiny_vol_price_distr
