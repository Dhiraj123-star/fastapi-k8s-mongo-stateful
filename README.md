# FastAPI-K8s-Mongo-Stateful

A production-ready blueprint for a containerized **FastAPI** application using an asynchronous **MongoDB** backend, orchestrated on **Kubernetes (Minikube)** using **Traefik v3** as the Edge Router with SSL/TLS termination.

## 🚀 Features

* **FastAPI**: High-performance Python API with auto-generated Swagger docs.
* **Traefik Ingress**: Modern, dynamic routing with native support for TLS and Middlewares.
* **SSL/TLS Termination**: Secure HTTPS access via self-signed certificates (locally).
* **Traefik Dashboard**: Visual monitoring of routers, services, and cluster health.
* **Basic Auth Middleware**: Password-protected dashboard access.
* **MongoDB (Stateful)**: Persistent storage using Kubernetes `StatefulSet` and `VolumeClaimTemplates`.
* **Self-Healing**: Readiness and Liveness probes ensure traffic only hits healthy pods.

## 📁 Project Structure

```text
├── .github/workflows/
│   └── deploy.yml       # GitHub Actions CI/CD pipeline
├── app/
│   ├── main.py          # FastAPI logic (Motor/Async driver)
│   └── requirements.txt # Python dependencies
├── k8s/
│   ├── secrets.yaml     # DB Credentials & Basic Auth Secret
│   ├── mongo-db.yaml    # StatefulSet & Headless Service
│   ├── fastapi-app.yaml # Deployment & Service
│   ├── traefik-ui.yaml  # IngressRoute for Dashboard & Middleware
│   └── ingress.yaml     # Traefik IngressRoute for fastapi.local
├── .env                 # Local dev environment
└── Dockerfile           # App containerization

```

## 🛠️ Setup & Deployment

### 1. Prepare Local Cluster & Traefik

Disable the default Nginx addon and install Traefik via Helm:

```bash
minikube start
minikube addons disable ingress

helm repo add traefik https://traefik.github.io/charts
helm repo update
helm install traefik traefik/traefik --set="service.type=LoadBalancer"

```

### 2. Configure Local DNS & Network

On Linux, manually patch the Traefik service to bind to your Minikube IP:

```bash
# Patch the External IP
kubectl patch svc traefik -p '{"spec":{"externalIPs":["'$(minikube ip)'"]}}'

# Add to /etc/hosts
echo "$(minikube ip) fastapi.local dashboard.fastapi.local" | sudo tee -a /etc/hosts

```

### 3. Generate SSL Certificates

Create a self-signed certificate for `fastapi.local`:

```bash
openssl req -x509 -newkey rsa:4048 -keyout tls.key -out tls.crt -days 365 -nodes -subj "/CN=fastapi.local"

# Create the K8s Secret
kubectl create secret tls fastapi-tls --cert=tls.crt --key=tls.key

```

### 4. Deploy Resources

```bash
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo-db.yaml
kubectl apply -f k8s/fastapi-app.yaml
kubectl apply -f k8s/traefik-ui.yaml
kubectl apply -f k8s/ingress.yaml

```

## 📊 Monitoring & Access

* **API Home (HTTPS):** `https://fastapi.local/`
* **Interactive Docs:** `https://fastapi.local/docs`
* **Traefik Dashboard:** `http://fastapi.local/dashboard/` (Requires trailing slash)
* **User:** `admin`
* **Password:** `password123` (Set in `secrets.yaml`)



## 🧪 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Connectivity & DB status check |
| `POST` | `/store` | Insert JSON data into MongoDB |
| `GET` | `/fetch` | Retrieve all stored entries |

---

## 🛠 Troubleshooting

**404 on Dashboard?** Ensure you are using the exact URL `http://fastapi.local/dashboard/`. Traefik v3 will return a 404 if the trailing slash is missing.

**SSL Warning?** Since we are using a self-signed certificate, your browser will show a warning. Click "Advanced" -> "Proceed" to enter the site.

