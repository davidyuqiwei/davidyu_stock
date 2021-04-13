"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import airflow
from airflow.example_dags.subdags.subdag import subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.operators.python_operator import BranchPythonOperator
now = datetime.now()
run_time1 = now - timedelta( hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond )
run_time = run_time1 - timedelta(days=1)
DAG_NAME = "a_shiny_design"
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
    DAG_NAME, 
    default_args=default_args, 
    schedule_interval="0 0 1 1 *")
a1="aa.sh "
# t1, t2 and t3 are examples of tasks created by instantiating operators

t_analysis = BashOperator(
    task_id='clean_data',
    bash_command=a1,
    dag=dag)


t_scrap_data = BashOperator(
    task_id='scrap_data',
    bash_command=a1,
    dag=dag)

t_run_main_PROJECTNAME= BashOperator(
    task_id='run_main_PROJECTNAME',
    bash_command=a1,
    dag=dag)
t_clean_data= BashOperator(
    task_id='clean_data',
    bash_command=a1,
    dag=dag)
t_download_data= BashOperator(
    task_id='download_data',
    bash_command=a1,
    dag=dag)
t_to_hive= BashOperator(
    task_id='to_hive',
    bash_command=a1,
    dag=dag)
feature_analysis= SubDagOperator(
    task_id='feature_analysis',
    subdag=subdag(DAG_NAME, 'feature_analysis', default_args),
    dag=dag,
)
feature_slope = SubDagOperator(
    task_id='feature_slope',
    subdag=subdag(DAG_NAME, 'feature_slope', default_args),
    dag=dag,
)
kdj_rsi= SubDagOperator(
    task_id='kdj_rsi_stockstats',
    subdag=subdag(DAG_NAME, 'kdj_rsi_stockstats', default_args),
    dag=dag,
)
download_main= DummyOperator(task_id='run_main_PROJECTNAME')
to_hive= DummyOperator(task_id='to_hive')
#t_mv_daily_report.set_upstream(t_dazongjiaoyi)
t_clean_data.set_upstream(t_download_data)
t_to_hive.set_upstream(t_clean_data)
t_scrap_data.set_upstream(t_to_hive)
t_analysis.set_upstream(t_scrap_data)
feature_analysis.set_upstream(t_analysis)
feature_slope.set_upstream(t_analysis)
kdj_rsi.set_upstream(t_analysis)
#download_main.set_upstream(t_scrap_data)
t_scrap_data >> download_main >> to_hive


