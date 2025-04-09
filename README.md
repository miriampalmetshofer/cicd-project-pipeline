# CI/CD Pipeline

Miriam Palmetshofer | s2410455002

This simple Go project is designed to demonstrate a CI/CD pipeline using GitHub Actions. 

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