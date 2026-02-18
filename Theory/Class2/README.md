# Class 2 – Docker Hands-on Projects

This class focuses on practical implementation of Docker using real-world programming examples.

In this class, we containerized applications written in:
- Java
- Python

Both projects demonstrate Docker image creation, container execution, image layering, and Docker Hub interaction.

---

## Folder Structure

```
Class-2/
│
├── java-docker/
│   ├── Dockerfile
│   ├── second.Dockerfile
│   ├── Hello.java
│   └── README.md
│
└── python-docker/
    ├── Dockerfile
    ├── nosrc.Dockerfile
    ├── app.py
    └── README.md
```

---

## Topics Covered

### 1. Java Docker Project
- Creating a simple Java application
- Writing a Dockerfile
- Building Docker images
- Running containers
- Creating alternate Dockerfile versions
- Tagging and pushing image to Docker Hub

Open documentation:
[Java Docker Project](java-docker/README.md)

---

### 2. Python Docker Project
- Creating a Python application with user input
- Installing dependencies inside Docker image
- Building and running containers interactively
- Checking image layers using `docker history`
- Creating alternate Dockerfile (without source copy)
- Using volume mounting

Open documentation:
[Python Docker Project](python-docker/README.md)

---

## Learning Outcomes

After completing Class 2, we are able to:

- Write Dockerfiles for different languages
- Build and tag Docker images
- Run containers interactively
- Analyze image layers
- Push images to Docker Hub
- Use volume mounting for dynamic execution

---
