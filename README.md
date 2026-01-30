# FastAPI-K8s-Mongo-Stateful

A production-ready blueprint for a containerized **FastAPI** application using an asynchronous **MongoDB** backend, orchestrated on **Kubernetes (Minikube)** with automated CI/CD and Ingress routing.

## 🚀 Features

* **FastAPI**: High-performance Python API with auto-generated Swagger docs.
* **MongoDB (Stateful)**: Persistent storage using Kubernetes `StatefulSet` and `VolumeClaimTemplates`.
* **Ingress Routing**: Domain-based access via `fastapi.local` instead of NodePort IPs.
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
│   ├── fastapi-app.yaml # Deployment (Pulls from Docker Hub)
│   └── ingress.yaml     # Ingress rules for fastapi.local
├── .env                 # Local environment variables (Ignored by Git)
├── .gitignore           # Python and Env exclusions
└── Dockerfile           # App containerization

```

## 🛠️ Setup & Deployment

### 1. CI/CD Configuration

1. Push the code to GitHub.
2. Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` to **GitHub Repo Secrets**.
3. Actions will push to `dhiraj918106/fastapi-mongo-app:latest`.

### 2. Prepare Local Cluster

```bash
minikube start
minikube addons enable ingress

```

### 3. Configure Local DNS

Add the Minikube IP to your `/etc/hosts` file so your browser recognizes the domain:

```bash
# Get Minikube IP
minikube ip

# Add to /etc/hosts (Example: 192.168.49.2 fastapi.local)
echo "$(minikube ip) fastapi.local" | sudo tee -a /etc/hosts

```

### 4. Deploy to Kubernetes

```bash
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo-db.yaml
kubectl apply -f k8s/fastapi-app.yaml
kubectl apply -f k8s/ingress.yaml

```

### 5. Access the App

Since we are using Ingress, you can access the app directly via the domain:

* **API Home:** `http://fastapi.local/`
* **Interactive Docs:** `http://fastapi.local/docs`

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Connectivity & DB status check |
| `POST` | `/store` | Insert JSON data into MongoDB |
| `GET` | `/fetch` | Retrieve all stored entries |

---
