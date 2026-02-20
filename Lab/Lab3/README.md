# Lab 3 -- Docker Images, NGINX & Flask Application Deployment

## Objective

The objective of this lab was to understand Docker images, container
creation, image customization, and deployment of web applications using
Docker.

This lab focused on:

-   Running official Docker images
-   Building custom Docker images
-   Comparing image sizes
-   Deploying custom HTML using bind mounts
-   Containerizing and deploying a Flask web application

------------------------------------------------------------------------

# Part A -- Working with Official NGINX Image

In this section, we explored how Docker Hub provides ready-to-use
images.

### What We Did

-   Pulled the official NGINX image from Docker Hub
-   Ran the container with port mapping
-   Verified the running web server in the browser
-   Checked image size using docker images

### Learning Outcome

-   Understood how Docker pulls images from Docker Hub
-   Learned how port mapping works (-p host:container)
-   Observed how containers isolate services
-   Understood basic Docker container lifecycle

------------------------------------------------------------------------

# Part B -- Custom NGINX Image (Ubuntu Based)

In this section, we created our own NGINX image using Ubuntu as the base
image.

### What We Did

-   Wrote a custom Dockerfile using Ubuntu
-   Installed NGINX inside the container
-   Built the image using docker build
-   Checked and compared image size

### Learning Outcome

-   Understood how Dockerfiles work
-   Learned about base images
-   Observed that Ubuntu-based images are larger in size
-   Learned image layering concept

------------------------------------------------------------------------

# Part C -- Lightweight NGINX (Alpine Based)

To optimize image size, we built another image using Alpine Linux.

### What We Did

-   Used alpine:latest as base image
-   Installed NGINX using apk package manager
-   Built and ran the container
-   Compared image sizes with Ubuntu and official NGINX

### Learning Outcome

-   Learned why Alpine is preferred for lightweight containers
-   Understood image size optimization
-   Compared performance and size differences

------------------------------------------------------------------------

# Part D -- Deploying Custom HTML using Bind Mount

This section demonstrated how Docker can serve local files.

### What We Did

-   Created a local html directory
-   Added a custom index.html file
-   Used bind mount (-v) to connect host folder to container
-   Verified changes in browser

### Learning Outcome

-   Understood volume mounting
-   Learned difference between image data and runtime data
-   Observed real-time file reflection inside container

------------------------------------------------------------------------

# Part E -- Containerizing a Flask Web Application

In this final section, we deployed a Python Flask web application using
Docker.

### What We Did

-   Created a simple Flask app
-   Defined dependencies in requirements.txt
-   Wrote a Dockerfile using python:3.9-slim
-   Built the Docker image
-   Ran the container with port mapping (8080 → 5000)
-   Verified the application in browser

### Learning Outcome

-   Understood how to containerize backend applications
-   Learned dependency management in Docker
-   Observed how Docker ensures environment consistency
-   Understood the concept of the "It works on my machine" problem

------------------------------------------------------------------------

# Overall Concepts Covered

-   Docker Images
-   Containers
-   Dockerfile Instructions
-   Base Images
-   Image Layers
-   Port Mapping
-   Bind Mounts
-   Image Size Optimization
-   Application Containerization

------------------------------------------------------------------------

# Result

The lab successfully demonstrated:

-   Deployment of official Docker images
-   Building custom images
-   Lightweight container optimization
-   Serving custom HTML
-   Containerizing and deploying a Flask web application

All applications were successfully accessed through the browser using
mapped ports.

------------------------------------------------------------------------

# Conclusion

Lab 3 provided practical exposure to real-world Docker usage.

We learned how Docker simplifies application deployment by packaging
code, dependencies, and runtime into a portable container. This ensures
consistency across development, testing, and production environments.

The lab strengthened understanding of container-based architecture,
efficient image building, application deployment strategies, and
environment consistency using Docker.
