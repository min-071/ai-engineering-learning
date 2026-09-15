# Docker for AI

Hands-on Docker exercises for building reproducible AI development environments.

## What I Built

- Created a Docker image with Python 3.12 and PyTorch
- Adapted the environment for Apple Silicon
- Used Docker Compose to run multiple services
- Connected an AI development container to Qdrant
- Used Docker volumes for persistent files and data
- Built a simple Flask API inside Docker
- Practiced Docker port mapping
- Explored Docker image sizes and layer caching

## Architecture

AI Development Container
        |
        | Docker network
        |
        v
     Qdrant
  Vector Database

## Flask API

The Flask application runs on port 5000 inside the container.

Example port mapping:

```bash
docker run --rm -it \
  -p 5001:5000 \
  -v "$(pwd):/workspace" \
  ai-dev-mac \
  python app.py

