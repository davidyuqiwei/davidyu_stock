from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago

# https://my.oschina.net/u/4789384/blog/4963454

# /home/davidyu/stock/data/feature_center
with DAG(dag_id="d_database", start_date=days_ago(2), schedule_interval="@yearly") as dag:
    #t_download_data = BranchPythonOperator(task_id="download_data", python_callable=lambda: "true_1")
    #t_clean_data = DummyOperator(task_id="clean_data")
    #t_to_hive = DummyOperator(task_id="to_hive")
    
    ### 1
    a_STG = BranchPythonOperator(task_id="STG",python_callable=lambda: "true_2")
    ### 2
    t_ODS =  DummyOperator(task_id="ODS")
    
    t_dw = DummyOperator(task_id="t_dw")
    t_dw_stock_trade_date = DummyOperator(task_id="t_dw_stock_trade_date")
    t_dw_stock_name = DummyOperator(task_id="t_dw_stock_name")
    
    a_STG >> t_ODS
    t_ODS >> t_dw
    t_dw >> t_dw_stock_trade_date
    t_dw  >> t_dw_stock_name
    
    t_dwb = DummyOperator(task_id="t_dwb")
    t_dfcf_fuquan =  DummyOperator(task_id="t_dfcf_fuquan")
    t_dadan_realtime = DummyOperator(task_id="t_dadan_realtime")
    t_jigoudiaoyan = DummyOperator(task_id="t_jigoudiaoyan")
    t_dadan_DFCF = DummyOperator(task_id="t_dadan_DFCF")
    t_SH_INDEX= DummyOperator(task_id="t_SH_INDEX")
    
    t_ODS >> t_dwb
    #t_dwb >> t_dfcf_fuquan
    t_dwb >> t_dadan_realtime
    t_dwb >> t_jigoudiaoyan
    
    ## dfcf_fuquan
    t_macd =  DummyOperator(task_id="t_macd")
    t_rolling_regression =  DummyOperator(task_id="t_rolling_regression")
    t_xgb_prediction =  DummyOperator(task_id="t_xgb_predicttion")
    t_dfcf_fuquan >> t_macd >> t_xgb_prediction
    t_dfcf_fuquan >> t_rolling_regression >> t_xgb_prediction

    t_dwb >> t_dadan_DFCF >> t_dw_stock_trade_date
    t_dwb >> t_SH_INDEX >> t_dw_stock_trade_date
    t_dwb >> t_dfcf_fuquan
    t_dfcf_fuquan >> t_macd
    ## 
    t_dadan_realtime_period_max = DummyOperator(task_id="t_dadan_realtime_period_max")
    t_dadan_realtime >> t_dadan_realtime_period_max
    t_dw_stock_trade_date >> t_dadan_realtime_period_max

