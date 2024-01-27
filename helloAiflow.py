from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def print_hello():
    a = !python --version
    b = !pip freeze
    print(a )
    print("librerias:", b ) 

    return 'Hello world from Airflow!'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_world', 
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator
