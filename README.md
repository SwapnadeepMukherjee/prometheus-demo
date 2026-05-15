# Prometheus + FastAPI Monitoring Demo

A complete demonstration of real-time API health monitoring and observability using **Prometheus**, **Grafana**, **FastAPI**, and **Node Exporter**. This project showcases how to instrument a FastAPI application with Prometheus metrics and visualize them through Grafana dashboards.

## 🎯 Overview

This repository contains a production-ready monitoring stack that includes:

- **FastAPI Application**: An async web service with simulated workloads and error scenarios
- **Prometheus**: Time-series database for metrics collection
- **Grafana**: Visualization and dashboarding platform
- **Node Exporter**: System-level metrics collection
- **Docker & Docker Compose**: Complete containerized deployment

Perfect for learning observability, monitoring, and metrics-driven development!

## ✨ Features

- **Automatic Metrics Collection**: Built-in Prometheus instrumentation for FastAPI endpoints
- **Custom Endpoints**: Root, heavy workload, and error simulation endpoints
- **System Monitoring**: Node Exporter for host-level metrics
- **Docker Compose Stack**: One-command deployment of entire monitoring stack
- **Chaos Load Generator**: Python script to simulate realistic traffic patterns
- **Health Dashboards**: Grafana integration for visual insights

## 📋 Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development)
- Basic understanding of Prometheus and metrics collection

## 🚀 Project Structure

### Using Docker Compose (Recommended)

```

prometheus-demo/
├── app/                          # FastAPI application
│   ├── main.py                  # Main application with endpoints
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile              # Container image for the app
│   └── __pycache__/            # Python cache
├── prometheus/                   # Prometheus configuration
│   └── prometheus.yml           # Scrape configs and global settings
├── prometheus_data/             # Prometheus data storage
├── scripts/                      # Utility scripts
│   └── chaos_load.py            # Load generator for testing
├── Dockerfile                    # Main Dockerfile
├── docker-compose.yml           # Complete stack orchestration
├── .gitattributes              # Git configuration
└── README.md                    # This file

```

## 🔧 API Endpoints:

### FastAPI Application:

| Endpoint | Method | Description | Behavior |
|----------|--------|-------------|----------|
| `/` | GET | Health check | Returns success message |
| `/heavy` | GET | Simulate heavy workload | Async operation with 0.1-0.8s delay |
| `/error` | GET | Simulate errors | Returns HTTP 500 error |
| `/metrics` | GET | Prometheus metrics | Exposes all collected metrics |

### Monitoring & Observability Endpoints:

| Service | URL | Purpose |
|---------|-----|---------|
| Prometheus | http://localhost:9090 | Metrics database & query interface |
| Grafana | http://localhost:3000 | Visualization dashboards |
| Node Exporter | http://localhost:9100/metrics | System metrics |

## 📊 Prometheus Configuration:

The ```prometheus/prometheus.yml``` file defines:

- Global Settings: 15-second scrape intervals
- Prometheus Self-Monitoring: Scrapes Prometheus metrics
- Node Exporter: Collects system-level metrics
- FastAPI Application (commented out): Can be enabled for app metrics

## 🐳 Docker Compose Services

### Service Breakdown

**prometheus-init** (busybox)
- Initializes Prometheus data directory permissions
- Runs once during startup

**prometheus**
- Main metrics database
- Port: 9090
- Depends on prometheus-init

**node_exporter**
- System metrics collection
- Port: 9100
- Auto-restart on failure

**grafana**
- Metrics visualization
- Port: 3000
- Auto-restart on failure

**fastapi-app** (Optional)
- Currently commented out in compose file
- Uncomment to include the FastAPI app in the stack

## 📦 Dependencies

### Python (FastAPI App)
- **fastapi**: Modern async web framework
- **uvicorn**: ASGI server
- **prometheus-fastapi-instrumentator**: Auto-instrumentation for metrics
- **prometheus_client**: Prometheus client library
- **pytest**: Testing framework

### External (Docker)
- **prometheus**: Latest stable
- **grafana**: Latest stable
- **prom/node-exporter**: Latest stable
- **python:3.13-slim**: Lightweight Python base image

## 🎓 Learning Outcomes

By exploring this repository, you'll learn:

1. **Instrumenting Applications**: How to add monitoring to FastAPI apps
2. **Prometheus Setup**: Time-series database configuration
3. **Metrics Collection**: Understanding scrape configs and targets
4. **Container Orchestration**: Docker Compose for multi-service apps
5. **Grafana Integration**: Setting up dashboards for visualization
6. **PromQL Queries**: Writing queries for metrics analysis
7. **Chaos Engineering**: Load testing and failure simulation

## 🤝 Contributing

This is an educational/demo project. Feel free to fork, modify, and use it for learning purposes!

## 📝 License

This project is provided as-is for educational purposes. Check the repository for license details.

## 👤 Author

**Swapnadeep Mukherjee**  
GitHub: [@SwapnadeepMukherjee](https://github.com/SwapnadeepMukherjee)

---

**Happy monitoring! 🚀📊**
