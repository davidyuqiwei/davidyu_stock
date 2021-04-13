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
run_time = run_time1 - timedelta(days=2)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': run_time,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'dadan_DFCF', 
    default_args=default_args, 
    schedule_interval="30 21 * * *")

# t1, t2 and t3 are examples of tasks created by instantiating operators
task1_command="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dadan_DFCF/shell/run_dadan_dfcf_weekly_dadan_cnt.sh "
task2_command="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dadan_DFCF/shell/run_dadan_dfcf_today_dadan_weekly_dadan_cnt.sh "


t1 = BashOperator(
    task_id='dadan_dfcf_weekly_dadan_cnt',
    bash_command=task1_command,
    dag=dag)


t2 = BashOperator(
    task_id='dadan_dfcf_today_dadan_weekly_dadan_cnt',
    bash_command=task2_command,
    dag=dag)

t2.set_upstream(t1)
