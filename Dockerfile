# Start from the official Golang base image
FROM golang:1.24.1 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod ./
COPY go.sum ./

# Download all dependencies
RUN go mod download

# Copy the rest of the application's source code
COPY . .

# Build the Go app
RUN go build -o main .

# Use a minimal base image for the final container
FROM debian:bullseye-slim

# Create a working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/main .

# Set the entry point for the container
ENTRYPOINT ["./main"]

# Expose the port the app runs on
EXPOSE 8010
