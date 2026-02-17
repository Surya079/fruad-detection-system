

# project repository structure

```
fraud-detection-system/
├── docker-compose/
│   ├── local/
│   └── monitoring/
├── services/
│   ├── transaction-simulator/     # Python/Shell
│   ├── data-ingestion/            # NiFi flows
│   ├── streaming-processor/       # Spark
│   ├── customer-service/          # Spring Boot
│   ├── fraud-scoring-service/     # Spring Boot + ML
│   ├── alert-service/             # Spring Boot
│   └── api-gateway/               # Spring Cloud Gateway
├── frontend/
│   └── customer-dashboard/        # React
├── ml-model/
│   ├── notebooks/
│   └── training/
├── infrastructure/
│   ├── terraform/                  # AWS IaC
│   └── k8s/                        # K8s manifests
└── docs/
    ├── architecture/
    └── api-specs/

```

