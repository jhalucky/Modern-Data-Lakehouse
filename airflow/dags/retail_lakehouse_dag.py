from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner" : "Lucky",
    "retries": 2
}

with DAG(
    dag_id="retail_lakehouse_pipeline",
    default_args=default_args,
    start_date=datetime(2026,7,16),
    schedule="@daily",
    catchup=False,
    tags=["Retail","Lakehouse"]
) as dag:
    
    bronze = BashOperator(
        task_id="bronze_pipeline",
        bash_command="""
        cd /opt/airflow/project && 
        python -m src.bronze.bronze_pipeline
        """
    )

    silver = BashOperator(
        task_id="silver_pipeline",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.silver.silver_pipeline
        """
    )

    gold = BashOperator(
        task_id="gold_pipeline",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.gold.gold_pipeline
        """
    )

    publish = BashOperator(
        task_id="publish_pipeline",
        bash_command="""
        cd /opt/airflow/project &&
        python -m src.published.publsih_pipeline
       """
    )

    bronze >> silver >> gold >> publish