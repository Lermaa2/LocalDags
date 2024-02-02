from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import subprocess

def print_hello():
    # Ejecutar el comando 'python --version' y capturar la salida
    python_version = subprocess.run(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    python_version = python_version.stdout.strip()
    # Ejecutar el comando 'pip freeze' y capturar la salida
    installed_libraries = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    installed_libraries = installed_libraries.stdout.strip()
    final_output = f"{python_version}\tlibrerias: {installed_libraries}"
    return final_output


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
