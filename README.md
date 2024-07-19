# Binary <=> Decimal <=> Hexadecimal Converter

### The application is written in Python using Flask framework for quick and lightweight provisioning of the HTTP API endpoint for user requests.

It includes integrated health check, usage guide and user input verification. <br>
<br>
**/.github/workflows/docker-image.yml** - Workflow for building and pushing the image to Docker Hub<br>
**/kubernetes/manifest.yml** - Configuration of automating the launching of pod instances (Deployment) and using NodePort to get external traffic (Service)<br>
**/nginx/site.conf** - Reverse proxy configuration<br>
**Dockerfile** - Instructions to build a container image<br>
**main.py** - Application code<br>
**requirements.txt** - List of applcation dependencies<br>
<br>
### The Tech Stack used:
**Github Actions** (As a CI/CD tool for build and deployment automation)<br>
**Self-hosted** (Ubuntu 22.04):<br>
  **Github Runner** configured with Github Actions<br>
  **Docker**<br>
  **Kubernetes**: **k3s** with multiple pods deployed for high availability and load balancing; **NodePort** service as the external entry point for incoming requests from nginx<br>
  **Nginx** used as a reverse proxy for incoming user connections on 8080/TCP forwarding them to NodePort's 30080/TCP<br>
