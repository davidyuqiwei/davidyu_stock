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

with DAG(dag_id="d_shiny_design", start_date=days_ago(2), schedule_interval="@yearly") as dag:
# t1, t2 and t3 are examples of tasks created by instantiating operators

    t_tab = BranchPythonOperator(task_id="t_tab",python_callable=lambda: "true_2")
    
    data_dfcf_fuquan=DummyOperator(task_id="data_dfcf_fuquan")
    data_all_owner=DummyOperator(task_id="data_all_owner")
    data_dazongjiaoyi=DummyOperator(task_id="data_dazongjiaoyi")
    data_dadan_realtime_ifeng = DummyOperator(task_id="data_dadan_realtime_ifeng")
    data_vol_price_distr= DummyOperator(task_id="data_vol_price_distr")
    
    
    tab_trend= DummyOperator(task_id="tab_trend")
    
    tab_dazongjiaoyi,tab_MACD,tab_turnover,tab_dadan_realtime,tab_vol_price_distr = tab(dag)
    t_tab >> data_dfcf_fuquan
    t_tab >> data_all_owner
    t_tab >> data_dazongjiaoyi
    t_tab >> data_dadan_realtime_ifeng
    t_tab >> data_vol_price_distr



    data_dazongjiaoyi >> tab_dazongjiaoyi
    data_dfcf_fuquan >> tab_trend >> tab_MACD    
    tab_trend >> tab_turnover
    data_dadan_realtime_ifeng >> tab_dadan_realtime
    data_vol_price_distr >> tab_vol_price_distr
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


