# CI/CD Pipeline

Miriam Palmetshofer | s2410455002

![badge](https://github.com/miriampalmetshofer/cicd-project-pipeline/actions/workflows/go.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=miriampalmetshofer_cicd-project-pipeline&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=miriampalmetshofer_cicd-project-pipeline)

This simple Go project is designed to demonstrate a CI/CD pipeline using GitHub Actions. 

### Run Logging Application

This project includes a simple development setup for elasticsearch, Kibana and Filebeat using Docker.
To run the logging application:
**Start Elasticsearch Kibana and Filebeat**:
   ```bash
   docker-compose up -d
   ```
Filebeat will monitor the `access.log` file in the `app-logs/` directory and send logs to Elasticsearch.
With the `/log` route you can write sample logs to the `access.log` file, which will then automatically processed by Filebeat and sent to Elasticsearch. (adding logs manually is also possible)

### Helpful commands

```bash
docker run --name mypostgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

Run a PostgreSQL container with the name `mypostgres`, 
set the password to `password`, and map port 5432 on the host to port 5432 on the container. (Assumes you have Docker installed and pulled the PostgreSQL image.)

```bash
go test -v
```

Run all tests in verbose mode.