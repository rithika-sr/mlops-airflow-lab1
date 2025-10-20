# --------------------------------------------------------
# Author: Rithika Sankar Rajeswari
# MLOps Lab 1 - Airflow + FastAPI Integration
# Description: Automated workflow for K-Means clustering
#              with an API-serving step for model exposure
# --------------------------------------------------------

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# ----------------------------
# Default DAG Configuration
# ----------------------------
default_args = {
    'owner': 'rithika',
    'start_date': datetime(2025, 10, 20),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Airflow_Lab1_Rithika',
    default_args=default_args,
    description='K-Means workflow + FastAPI serving step',
    schedule_interval=None,
    catchup=False,
)

# ----------------------------
# Step 1: Load Dataset
# ----------------------------
def load_data():
    df = pd.DataFrame({
        'feature1': [5, 15, 25, 35, 45, 55],
        'feature2': [2, 8, 18, 32, 38, 50]
    })
    print("✅ Data loaded successfully.")
    return df.to_dict()  # Airflow handles JSON natively

# ----------------------------
# Step 2: Preprocess Data
# ----------------------------
def data_preprocessing(data_dict):
    df = pd.DataFrame(data_dict)
    df = (df - df.mean()) / df.std()  # Simple normalization
    print("✅ Data preprocessing completed.")
    return df.to_dict()

# ----------------------------
# Step 3: Build and Save Model
# ----------------------------
def build_save_model(data_dict):
    df = pd.DataFrame(data_dict)

    # KMeans model training
    model = KMeans(n_clusters=3, random_state=42)
    model.fit(df)

    # Ensure working_data directory exists
    model_dir = '/opt/airflow/working_data'
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, 'model_rithika.pkl')
    joblib.dump(model, model_path)

    print(f"✅ Model built and saved successfully at: {model_path}")
    return model_path

# ----------------------------
# Step 4: Serve Model (Simulated FastAPI)
# ----------------------------
def serve_model_api(model_path):
    print(f"🚀 Serving model via FastAPI simulation...")
    print(f"   ➤ FastAPI endpoint: /predict")
    print(f"   ➤ Model Path: {model_path}")
    print("✅ FastAPI server simulated successfully.")
    return f"Model served from {model_path}"

# ----------------------------
# Define Airflow Tasks
# ----------------------------
load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag,
)

data_preprocessing_task = PythonOperator(
    task_id='data_preprocessing_task',
    python_callable=data_preprocessing,
    op_args=[load_data_task.output],
    dag=dag,
)

build_save_model_task = PythonOperator(
    task_id='build_save_model_task',
    python_callable=build_save_model,
    op_args=[data_preprocessing_task.output],
    dag=dag,
)

serve_model_task = PythonOperator(
    task_id='serve_model_task',
    python_callable=serve_model_api,
    op_args=[build_save_model_task.output],
    dag=dag,
)

# ----------------------------
# Task Dependencies
# ----------------------------
load_data_task >> data_preprocessing_task >> build_save_model_task >> serve_model_task

# ----------------------------
# For CLI Execution
# ----------------------------
if __name__ == "__main__":
    dag.cli()
