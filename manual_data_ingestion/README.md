# Manual Ingestion of Historical Logs

This is a mini project for a CI/CD course that demonstrates how to set up Elasticsearch and Kibana for log data analysis.

## Project Overview

This project provides a simple setup for:
1. Running Elasticsearch and Kibana in Docker containers
2. Parsing web server access logs
3. Sending the parsed log data to Elasticsearch
4. Visualizing and analyzing the data in Kibana

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- Python Elasticsearch client (`pip install elasticsearch`)

## Setup Instructions

### 1. Start Elasticsearch and Kibana (Filebeat)

**Note**: Filebeat is also included in the `docker-compose.yaml` file to ship logs to Elasticsearch but is not needed for this manual ingestion.

```bash
docker-compose up -d
```

This will start:
- Elasticsearch on port 9200
- Kibana on port 5601

### 2. Wait for Services to Start

Elasticsearch and Kibana may take a minute or two to fully initialize. You can check if Elasticsearch is ready by running:

```bash
curl http://localhost:9200
```

Kibana will be available at: http://localhost:5601

### 3. Send Log Data to Elasticsearch

The repository includes a Python script (`send_data.py`) that parses log files, creates an index and sends them to Elasticsearch:

```bash
python send_data.py
```

By default, the script will process the `data/access.log` file (can be downloaded from [Kaggle](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs?select=access.log). You can modify the script to use a different log file if needed.

## Project Structure

- `docker-compose.yaml` - Configuration for Elasticsearch and Kibana containers
- `send_data.py` - Python script to parse and send log data to Elasticsearch
- `data/` - Directory containing log files
  - `access.log` - Main log file (not included in the repository, can be downloaded from [Kaggle](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs?select=access.log))

## Troubleshooting

- If you encounter connection issues with Elasticsearch, ensure the container is running: `docker ps`
- If the script fails to send data, check that Elasticsearch is accessible: `curl http://localhost:9200`
- For Kibana issues, verify it's running properly: `curl http://localhost:5601`