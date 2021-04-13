from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago

with DAG(dag_id="design_test", start_date=days_ago(2), schedule_interval="@yearly") as dag:
    #t_download_data = BranchPythonOperator(task_id="download_data", python_callable=lambda: "true_1")
    #t_clean_data = DummyOperator(task_id="clean_data")
    #t_to_hive = DummyOperator(task_id="to_hive")
    
    ### 1
    t_scrap_data = BranchPythonOperator(task_id="t_scrap_data",python_callable=lambda: "true_2")
    ### 2
    t_analysis = DummyOperator(task_id="analysis")
    t_download_main = DummyOperator(task_id="download_main")
    t_feature_center = DummyOperator(task_id="feature_center")
    
    t_to_hive= DummyOperator(task_id="to_hive_folder")
    t_clean_data= DummyOperator(task_id="clean_data_folder")
    t_downlowd_data_folder= DummyOperator(task_id="download_data_folder")
    
    a_kdj_macd= DummyOperator(task_id="kdj_macd")
    a_feature_slope= DummyOperator(task_id="feature_slope")
    a_important_owner= DummyOperator(task_id="important_owner")
    a_daily_report= DummyOperator(task_id="daily_report")
    
    
    a_feature_kdj_macd= DummyOperator(task_id="feature_kdj_macd")
    a_feature_roll_regression = DummyOperator(task_id="feature_roll_regression")
    
    a_owner_slope= DummyOperator(task_id="eg_if_HK_central_increase_vs_the_future_slope")
    a_jigoudiaoyan_slope= DummyOperator(task_id="eg_if_jigoudiaoyan_num_vs_the_future_slope")
    
    c_important_owner= DummyOperator(task_id="c_important_owner")
    c_dazongjiaoyi= DummyOperator(task_id="c_dazongjiaoyi")
    c_dadan_dfcf= DummyOperator(task_id="c_dadan_dfcf")

    
    t_scrap_data >> t_analysis
    t_scrap_data >> t_download_main >> t_downlowd_data_folder >> t_clean_data >> t_to_hive
    t_scrap_data >> t_feature_center
    
    
    t_analysis >> a_kdj_macd
    t_analysis >> a_feature_slope
    t_analysis >> a_important_owner
    t_analysis >> a_daily_report

    t_feature_center >> a_feature_kdj_macd
    t_feature_center >> a_feature_roll_regression
    
    a_feature_slope >> a_owner_slope
    a_feature_slope >> a_jigoudiaoyan_slope

    a_daily_report >> c_important_owner
    a_daily_report >> c_dazongjiaoyi
    a_daily_report >> c_dadan_dfcf


