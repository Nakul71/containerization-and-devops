#  Theory - Containerization and DevOps

This folder contains **class-wise theory notes** for the subject  
**Containerization and DevOps**.

The notes include both **conceptual understanding** and **command-level explanations** wherever required.

---

##  Class-wise Notes

###  Class 1 - Docker Basics (Hands-on)
Topics covered:
- Docker introduction
- Docker architecture overview
- Basic Docker commands
- Image and container lifecycle

[Open Class 1 Notes](Class1/README.md)

---

### Class 2 - Application Containerization (Java & Python)

Topics covered:
- Writing Dockerfiles for different languages
- Building Docker images using custom Dockerfiles
- Running containers interactively
- Installing dependencies inside images
- Using alternate Dockerfiles
- Tagging and pushing images to Docker Hub
- Inspecting image layers using `docker history`
- Volume mounting for dynamic execution

[Open Class 2 Notes](Class2/README.md)

---

### Class 3 - Docker Engine API via Unix Socket (Hands-on)

Topics covered:
- Docker daemon and REST API
- Understanding `/var/run/docker.sock`
- Accessing Docker Engine using curl
- Pulling images via API
- Creating containers using HTTP requests
- Starting and stopping containers via API
- Inspecting container metadata

[Open Class 3 Notes](Class3/README.md)

---

### Class 4 - Multistage Docker Build (Hands-on)

Topics covered:
- Single-stage Docker build using Ubuntu and GCC
- Building a C application inside a Docker container
- Understanding Docker image layers
- Introduction to Multistage builds
- Using `AS builder` stage
- Using `FROM scratch` for minimal images
- Copying artifacts using `COPY --from=builder`
- Comparing image sizes (Single vs Multistage)
- Optimizing images for production environments

[Open Class 4 Notes](Class4/README.md)

---

### Class 5 - Docker Volumes and Bind Mounts (Hands-on)

Topics covered:
- Introduction to Docker data persistence
- Creating and listing Docker volumes
- Mounting named volumes inside containers
- Data persistence after container removal
- Bind mounts using host directories
- Comparing bind mounts vs named volumes

[Open Class 5 Notes](Class5/README.md)

---

### Class 6 - Docker Networking (Hands-on)

Topics covered:
- Default Docker networks (bridge, host, none)
- Inspecting bridge network configuration
- Creating custom bridge network
- Running containers in custom networks
- Container-to-container communication using ping
- Host network mode
- Checking open ports using `ss`

[Open Class 6 Notes](Class6/README.md)

---

### Class 7 - Docker Advanced Commands (Hands-on)

[Open Class 7 Notes](Class7/README.md)

---

### Class 8 - Docker Compose (Hands-on)

- [Open Class 8 Part 1 Notes](Class8/Part1/README_Class8_Docker_Compose_Lab.md)
- [Open Class 8 Part 2 Notes](Class8/Part2/README.md)

---

### Class 9 - Docker Compose and Reverse Proxy (Hands-on)

- [Open Class 9 Part 1 Notes](Class9/Part1/README.md)
- [Open Class 9 Part 2 Notes](Class9/Part2/README.md)