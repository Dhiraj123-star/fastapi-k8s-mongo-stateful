# FastAPI-K8s-Mongo-Stateful

A production-ready blueprint for a containerized **FastAPI** application using an asynchronous **MongoDB** backend, orchestrated on **Kubernetes (Minikube)**.

## 🚀 Features

* **FastAPI**: High-performance Python API with auto-generated Swagger docs.
* **MongoDB (Stateful)**: Persistent storage using Kubernetes `StatefulSet` and `VolumeClaimTemplates`.
* **Secure Credentials**: Uses `python-dotenv` for local dev and **K8s Secrets** for cluster environments.
* **Automated CI/CD**: GitHub Actions workflow to build and push images to **Docker Hub**.
* **Headless Service**: Provides stable network identities for the database.

## 📁 Project Structure

```text
├── .github/workflows/
│   └── deploy.yml       # GitHub Actions CI/CD pipeline
├── app/
│   ├── main.py          # FastAPI logic (Motor/Async driver)
│   └── requirements.txt  # Python dependencies
├── k8s/
│   ├── secrets.yaml     # Base64 encoded DB credentials
│   ├── mongo-db.yaml    # StatefulSet & Headless Service
│   └── fastapi-app.yaml # Deployment (Pulls from Docker Hub)
├── .env                 # Local environment variables (Ignored by Git)
├── .gitignore           # Python and Env exclusions
└── Dockerfile           # App containerization

```

## 🛠️ Setup & Deployment

### 1. CI/CD Configuration

1. Push the code to your GitHub repository.
2. Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` to your **GitHub Repo Secrets**.
3. GitHub Actions will automatically build and push the image to `dhiraj918106/fastapi-mongo-app:latest`.

### 2. Prepare Local Cluster

```bash
minikube start

```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo-db.yaml
kubectl apply -f k8s/fastapi-app.yaml

```

### 4. Access the App

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
