#  MLOps Lab 1: Airflow + K-Means Workflow


## 🧩 Lab Overview
This lab demonstrates how to **orchestrate an end-to-end machine learning workflow** using **Apache Airflow**, from data loading and preprocessing to model training and simulated serving.  
It automates a **K-Means clustering pipeline**, showcasing key principles of **reproducibility, modularity, and scheduling** within MLOps.


## ⚙️ Tech Stack
| Category | Tools Used |
|-----------|-------------|
| Workflow Orchestration | Apache Airflow |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas |
| Model Persistence | Pickle |
| Visualization / CLI | Airflow Web UI |
| Language | Python 3.x |



## 🧠 Workflow Summary (Airflow DAG)
**DAG Name:** `Airflow_Lab1_Rithika`  
**Description:** K-Means Clustering Workflow + Model Save + Serving Simulation  

### 📊 Task Flow
1. **`load_data_task`** – Creates a small synthetic dataset.  
2. **`data_preprocessing_task`** – Performs normalization.  
3. **`build_save_model_task`** – Trains a K-Means model, finds the optimal *k* using the elbow method, and saves it as a `.pkl` file.  
4. **`serve_model_task`** – Simulates FastAPI serving (mock endpoint).  

✅ Each task uses **`PythonOperator`** and passes objects via **XCom (Pickle serialization)**.  
✅ Workflow ensures modular design, making each task independently testable and reusable.


## 🗂️ Project Structure


mlops-airflow-lab1/
│
├── dags/
│   └── airflow_lab1_dag.py           # Main DAG file (this project)
│
├── logs/                             # Airflow-generated logs
│   └── dag_processor_manager/
│
├── working_data/
│   ├── iris.csv                      # Sample dataset
│   └── model_rithika.pkl             # Saved model artifact
│
├── .gitignore                        # Excludes logs & temp files
└── README.md                         # Project documentation




## ⚡ How to Run Locally

### 1️⃣ Start Airflow Environment
```bash
docker-compose up airflow-init
docker-compose up
````

### 2️⃣ Access Airflow UI

Open your browser at → **[http://localhost:8080](http://localhost:8080)**
Login (default):

```
Username: airflow2
Password: airflow2
```

### 3️⃣ Trigger the DAG

* Go to **DAGs → Airflow_Lab1_Rithika**
* Turn the toggle **ON**
* Click ▶️ **Trigger DAG**
* Monitor tasks under the **Graph** view



## 📦 Outputs

* Trained **K-Means model** → `model_rithika.pkl`
* Airflow logs under `/logs/`
* Clean workflow orchestration verified through DAG success states



## 🎯 Key Learnings

* Building reproducible ML workflows with Airflow
* Managing data and model dependencies via **XComs**
* Automating model lifecycle steps (load → preprocess → train → serve)
* Incorporating modular, maintainable Python scripts in DAGs


```
