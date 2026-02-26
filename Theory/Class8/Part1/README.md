# Docker Compose Lab -- Class 8

## docker-compose.yml

``` yaml
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    container_name: my-nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    environment:
      - NGINX_HOST=localhost
    restart: unless-stopped
```

------------------------------------------------------------------------

## Step 1
### Command Used

``` bash
docker compose up -d
```

![Step 1](image2.png)


------------------------------------------------------------------------

## Step 2

### Command Used
``` bash
docker compose up -d
```
![Step 2](image3.png)




------------------------------------------------------------------------

## Step 3
### Command Used

``` bash
docker ps
```
![Step 3](image4.png)





------------------------------------------------------------------------

## Step 4
### Command Used

``` bash
docker compose down
```

![Step 4](image5.png)


------------------------------------------------------------------------

## Step 5
### Command Used

``` bash
docker ps
```

![Step 5](image6.png)



------------------------------------------------------------------------

## Step 6

### Command Used

``` bash
docker compose up
```
![Step 6](image7.png)



------------------------------------------------------------------------

## Step 7
### Command Used

``` bash
docker compose down
```
![Step 7](image8.png)



------------------------------------------------------------------------

## Step 8
### Command Used
``` bash
docker compose logs -f
```
![Step 8](image9.png)


------------------------------------------------------------------------

## Step 9

### Command Used

Access in browser: http://localhost:8080

![Step 9](image10.png)



------------------------------------------------------------------------

## Step 10

### Command Used

``` bash
docker compose ps
```

![Step 10](image11.png)



------------------------------------------------------------------------
