# FastAPI-K8s-Mongo-Stateful

A production-ready blueprint for a containerized **FastAPI** application using an asynchronous **MongoDB** backend, orchestrated on **Kubernetes (Minikube)** using a **StatefulSet** for data persistence.

## 🚀 Features

* **FastAPI**: High-performance Python API with auto-generated Swagger docs.
* **MongoDB (Stateful)**: Persistent storage using Kubernetes `StatefulSet` and `VolumeClaimTemplates`.
* **Secure Credentials**: Uses `python-dotenv` for local dev and `K8s Secrets` for production.
* **Headless Service**: Provides stable network identities for the database.

## 📁 Project Structure

```text
├── app/
│   ├── main.py          # FastAPI logic (Motor/Async driver)
│   └── requirements.txt  # Python dependencies
├── k8s/
│   ├── secrets.yaml     # Base64 encoded DB credentials
│   ├── mongo-db.yaml    # StatefulSet & Headless Service
│   └── fastapi-app.yaml # Deployment & NodePort Service
├── .env                 # Local environment variables
└── Dockerfile           # App containerization

```

## 🛠️ Setup & Deployment

### 1. Prepare Environment

```bash
minikube start
eval $(minikube docker-env)

```

### 2. Build Image

```bash
docker build -t fastapi-mongo-app:latest .

```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo-db.yaml
kubectl apply -f k8s/fastapi-app.yaml

```

### 4. Access the App

Get the URL for your API:

```bash
minikube service fastapi-service --url

```

* **Interactive Docs:** `http://<URL>/docs`
* **Health Check:** `http://<URL>/`

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Connectivity & DB status check |
| `POST` | `/store` | Insert JSON data into MongoDB |
| `GET` | `/fetch` | Retrieve all stored entries |

---
