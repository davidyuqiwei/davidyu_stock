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
    'ar_stock_dw', 
    default_args=default_args, 
    schedule_interval="55 22 * * *")

# t1, t2 and t3 are examples of tasks created by instantiating operators
#task_stock_index_trade_day="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/SH_index/shell/spark_SH_index_trade_date.sh "
task_clean_data="/home/davidyu/stock/scripts/davidyu_stock/scripts/download/clean_data/run_clean_data.sh "


t_clean_data= BashOperator(
    task_id='stock_clean_data',
    bash_command=task_clean_data,
    dag=dag)



"""
task_all="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/daily_report/mv_daily_report.sh "
task1_command="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dadan_DFCF/shell/to_daily_report.sh "
task2_command="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/JiGouDiaoYan/shell/to_daily_report.sh "
task_dazongjiaoyi="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dazongjiaoyi/shell/to_daily_report.sh "
task_yejiyuqi="/home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/YeJiYuQi/shell/to_daily_report.sh "
t1 = BashOperator(
    task_id='dadan_dfcf_today_rank',
    bash_command=task1_command,
    dag=dag)


t_mv_daily_report = BashOperator(
    task_id='mv_daily_report',
    bash_command=task_all,
    dag=dag)

t_jigoudiaoyan = BashOperator(
    task_id='jigoudiaoyan',
    bash_command=task2_command,
    dag=dag)

t_dazongjiaoyi = BashOperator(
    task_id='dazongjiaoyi',
    bash_command=task_dazongjiaoyi,
    dag=dag)

t_yejiyuqi = BashOperator(
    task_id='yejiyuqi',
    bash_command=task_yejiyuqi,
    dag=dag)

t_mv_daily_report.set_upstream(t1)
t_mv_daily_report.set_upstream(t_jigoudiaoyan)
#t_mv_daily_report.set_upstream(t_dazongjiaoyi)
t_yejiyuqi.set_upstream(t_dazongjiaoyi)
t_mv_daily_report.set_upstream(t_yejiyuqi)

"""

