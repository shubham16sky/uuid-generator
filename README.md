# UUID Generator API

This is a simple API to generate UUIDs, built using FastAPI. The API provides two endpoints: one to check if the service is running and another to generate UUIDs.

## Table of Contents

- [Installation](#installation)
  - [Using Docker](#using-docker)
  - [Running Locally](#running-locally)
- [Kubernetes Deployment](#kubernetes-deployment)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t uuid-generator .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 uuid-generator
    ```

### Running Locally

1. **Clone the repository:**

    ```sh
    git clone https://github.com/shubham16sky/uuid-generator.git
    cd uuid-generator-api
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    uvicorn app/main:app --reload
    ```

## Kubernetes Deployment

1. **Apply the Kubernetes manifests:**

    ```sh
    kubectl apply -f kubernetes-menifests/deployment.yaml
    kubectl apply -f kubernetes-menifests/service.yaml
    ```

2. **Verify the deployment:**

    ```sh
    kubectl get pods
    kubectl get services
    ```

## API Endpoints

- **Root Endpoint:**

  ```http
  GET /
  ```

  **Response:**

  ```json
  {
    "message": "Hey! It is up and working !"
  }
  ```

- **Generate UUID:**

  ```http
  GET /generate
  ```

  **Response:**

  ```json
  {
    "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Open a Pull Request

---

Created by [shubham16sky](https://github.com/shubham16sky)
