

# project repository structure

```

    fraud-detection-platform/
    ├── docker-compose/           # Local development setup
    │   ├── docker-compose.yml    # All services locally
    │   └── init-scripts/         # DB initialization
    ├── data-simulator/           # Python transaction generator
    │   ├── src/
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── ingestion/                # NiFi flows
    │   └── nifi-templates/
    ├── streaming/                # Spark jobs
    │   ├── fraud-detection/
    │   └── aggregations/
    ├── services/                 # Spring Boot microservices
    │   ├── customer-service/
    │   ├── transaction-service/
    │   ├── alert-service/
    │   ├── fraud-scoring-service/
    │   └── api-gateway/
    ├── frontend/                 # React app
    │   └── customer-dashboard/
    ├── ml-model/                 # Python ML stuff
    │   ├── notebooks/
    │   └── model-serving/
    ├── infrastructure/           # AWS deployment
    │   ├── terraform/            # If you want to learn IaC
    │   └── kubernetes/           # K8s manifests
    └── scripts/                  # Shell scripts for automation
        ├── setup-local.sh
        └── deploy-aws.sh

```

