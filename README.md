# 🚀 Harness Fleet Monitor: End-to-End CI/CD Project

A modern, cloud-native microservice designed to learn and test **GitHub Actions (CI)** and **Harness Continuous Delivery (CD)** end-to-end.

---

## 🏗️ Architecture & Flow

```
+-------------------+       +--------------------+       +-----------------------+
|  🐙 GitHub Repo   | ----> | 🐳 Docker Registry | ----> |   ☁️ Harness SaaS     |
|   (Source Code)   |  CI   |    (Docker Hub)    |  CD   |   (Pipeline Trigger)  |
+-------------------+       +--------------------+       +-----------+-----------+
                                                                     |
                                                                     | HTTPS (443)
                                                                     v
                                                         +-----------------------+
                                                         |  🤖 Harness Delegate  |
                                                         |   (Inside K8s Cluster)|
                                                         +-----------+-----------+
                                                                     |
                                                                     | kubectl apply
                                                                     v
                                                         +-----------------------+
                                                         |  ☸️ Kubernetes Target  |
                                                         | (Pods / Services / UI)|
                                                         +-----------------------+
```

---

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── ci-build.yaml         # GitHub Actions CI Workflow (Build & Push Docker image)
├── app/
│   ├── templates/
│   │   └── index.html            # Modern Tailwind CSS Dark-Mode UI with telemetry
│   ├── app.py                    # Flask microservice with /healthz, /api/info
│   └── requirements.txt          # Python dependencies (Flask, Gunicorn)
├── k8s/
│   ├── namespace.yaml            # Target namespace: harness-fleet
│   ├── deployment.yaml           # Deployment with Harness variables (<+artifact.image>)
│   └── service.yaml              # NodePort service exposing port 30080
├── harness/
│   └── pipeline.yaml             # Complete Harness CD Pipeline definition (Pipeline-as-Code)
├── Dockerfile                    # Minimal, secure container image
└── README.md
```

---

## 🎨 UI Features (Visual Verification of Deployments)

- **Dynamic Version Badge**: Shows `v1.0.0` or `v2.0.0`.
- **Dynamic Accent Color**: Changes color per release (e.g., `#10b981` Emerald Green vs `#f97316` Coral Orange) to visually verify Canary and Rolling updates in real time.
- **Pod Hostname**: Displays the exact pod handling the request (proves load balancing across replicas).
- **Interactive Degradation Simulator**: Button to toggle `/healthz` between HTTP 200 and HTTP 500 to test **Harness Automated Rollback**!

---

## 🚀 Quick Start Guide

### Step 1: Initialize Git and Push to Your GitHub Account
```powershell
cd C:\Users\Pavan\.gemini\antigravity\scratch\harness-lab
git init
git add .
git commit -m "feat: initial commit for harness-fleet-monitor"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/harness-fleet-monitor.git
git push -u origin main
```

### Step 2: Configure GitHub Secrets (for CI)
Go to your GitHub repo ➡️ **Settings** ➡️ **Secrets and variables** ➡️ **Actions**:
- `DOCKERHUB_USERNAME`: Your Docker Hub username.
- `DOCKERHUB_TOKEN`: Docker Hub Personal Access Token.

### Step 3: Run Harness CD Pipeline
Import or configure the pipeline in Harness using `k8s/` manifests and your Docker Hub image.
