# Class 2 – Java Docker Application
## Subfolder: java-docker

---

## Objective
To containerize a simple Java application using Docker, build images using different Dockerfiles, run containers, and push the image to Docker Hub.

---

## Project Structure

```
java-docker/
│── Hello.java
│── Dockerfile
│── second.Dockerfile
│── image1.png
│── image2.png
│── image3.png
│── image4.png
│── image5.png
│── image6.png
│── image7.png
│── image8.png
│── image9.png
│── README.md
```

---

## Step 1 – Create Java Application

### Hello.java
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Java Docker");
    }
}
```

---

## Step 2 – Create Dockerfile (Version 1)

```dockerfile
FROM eclipse-temurin:17-jdk
WORKDIR /home/app
COPY Hello.java .
RUN javac Hello.java
CMD ["java", "Hello"]
```

![Dockerfile Version 1](image1.png)

---

## Step 3 – Create second.Dockerfile (Version 2)

```dockerfile
FROM eclipse-temurin:17-jdk
WORKDIR /home/app
COPY Hello.java .
RUN javac Hello.java
CMD ["echo", "Hello from version 2"]
```

![Dockerfile Version 2](image2.png)

---

## Step 4 – Build Image Using second.Dockerfile

Command:
```
docker build -t java-app:1.1 -f second.Dockerfile .
```

![Docker Build Output](image3.png)

---

## Step 5 – Run the Container

Command:
```
docker run java-app:1.1
```

Output:
```
Hello from version 2
```

![Docker Run Output](image4.png)

---

## Step 6 – Generate Docker Hub Personal Access Token

![Docker Hub Token Page](image5.png)

---

## Step 7 – Login to Docker Hub

Command:
```
docker login -u nakul710
```

![Docker Login](image6.png)

---

## Step 8 – Tag the Image

Command:
```
docker tag java-app:1.1 nakul710/java-app:1.1
```

![Docker Tag](image7.png)

---

## Step 9 – Push Image to Docker Hub

Command:
```
docker push nakul710/java-app:1.1
```

![Docker Push](image8.png)

---

## Step 10 – Image Available on Docker Hub

![Docker Hub Repository](image9.png)

---

## Result
Successfully:
- Containerized Java application
- Built Docker image
- Ran container
- Tagged image
- Pushed image to Docker Hub
