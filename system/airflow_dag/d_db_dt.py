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
from airflow.utils.dates import days_ago
from design_shiny_sub.tab import *

with DAG(dag_id="d_db_dt", start_date=days_ago(2), schedule_interval="@yearly") as dag:
# t1, t2 and t3 are examples of tasks created by instantiating operators

    t_data = BranchPythonOperator(task_id="stock_dt",python_callable=lambda: "true_2")
    
    data_datetime=DummyOperator(task_id="datetime_table")
    #dws_dadan_realtime_t0 = DummyOperator(task_id="daily_onetrade_max")
    #dws_dadan_realtime_t0_sum = DummyOperator(task_id="daily_sum")
    #dws_dadan_realtime_t01 = DummyOperator(task_id="period_max_5_30_days_max")

    #dws_dadan_realtime_t11 = DummyOperator(task_id="minute_sum")
    #dws_dadan_realtime_t12 = DummyOperator(task_id="max_per_minute")


    #data_all_owner=DummyOperator(task_id="data_all_owner")
    #data_dazongjiaoyi=DummyOperator(task_id="data_dazongjiaoyi")
    #data_dadan_realtime_ifeng = DummyOperator(task_id="data_dadan_realtime_ifeng")
    #data_vol_price_distr= DummyOperator(task_id="data_vol_price_distr")
    
    
    
    t_data >> data_datetime
    #data_dadan_realtime >> dws_dadan_realtime_t0 >> dws_dadan_realtime_t01
    #data_dadan_realtime >> dws_dadan_realtime_t0_sum 
    #tab_dazongjiaoyi=DummyOperator(task_id="tab_dazongjiaoyi")



'''
t_tab = BashOperator(
    task_id='tab',
    bash_command=a1,
    dag=dag)

data_dfcf_fuqan= SubDagOperator(
    task_id='data_dfcf_fuquan',
    subdag=subdag(DAG_NAME, 'dfcf_fuquan', default_args),
    dag=dag,
)

'''


##t_tab >> data_dfcf_fuquan  


