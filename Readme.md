### Stucture

# Create project repository structure
fraud-detection-system/
├── docs/                    # Architecture docs, decisions
├── infrastructure/          # Terraform, CloudFormation
├── data-pipeline/          
│   ├── data-generator/      # Python simulation
│   ├── nifi-processors/     # NiFi configurations
│   └── spark-jobs/          # Spark streaming
├── backend-services/
│   ├── api-gateway/
│   ├── fraud-scoring-svc/
│   ├── customer-svc/
│   ├── transaction-svc/
│   └── alert-svc/
├── frontend/
│   └── customer-dashboard/  # React app
├── ml-models/
│   └── fraud-detection/     # Python notebooks
└── scripts/                 # Shell scripts