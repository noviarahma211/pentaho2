from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago

# Default arguments untuk DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Inisialisasi DAG
dag = DAG(
    'example_mysql_dag',
    default_args=default_args,
    description='A simple MySQL DAG',
    schedule_interval='@daily',  # Atur jadwal eksekusi DAG, misalnya harian
)

# Operasi untuk menjalankan query MySQL
task_query_mysql = MySqlOperator(
    task_id='query_mysql_table',
    mysql_conn_id='mysql_conn',  # ID koneksi MySQL yang telah Anda konfigurasi
    sql="SELECT * FROM project_otif LIMIT 10;",
    dag=dag,
)

# Definisi dependensi antar task (jika ada)
task_query_mysql

# Anda bisa menambahkan lebih banyak task di sini

if __name__ == "__main__":
    dag.cli()
