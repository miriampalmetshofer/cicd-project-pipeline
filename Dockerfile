# Stage 1: Build the Go binary
FROM --platform=linux/arm64 golang:1.24 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy go.mod and go.sum to leverage Docker cache
COPY go.mod ./
COPY go.sum ./
RUN go mod download

# Copy the rest of the application
COPY . .

# Build the application
RUN go build -o main .
RUN chmod +x main


# Stage 2: Create a minimal image
FROM --platform=linux/arm64 debian:bullseye-slim

# Install necessary CA certs
RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

WORKDIR /root/

# Copy the binary from the builder stage
COPY --from=builder /app/main .

# Hardcoded environment variables
ENV APP_DB_USERNAME=postgres
ENV APP_DB_PASSWORD=password
ENV APP_DB_NAME=postgres

# Set environment variables for Go
ENV GO_ENV=production

# Expose the port your app listens on
EXPOSE 8010

# Run the binary
CMD ["./main"]
