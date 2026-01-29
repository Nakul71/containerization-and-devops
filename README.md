# 🧪 Lab Experiment 1 -- Comparison of Virtual Machines and Containers

## 🎯 Objective

-   Understand differences between Virtual Machines and Containers.
-   Install and configure VM using VirtualBox and Vagrant.
-   Install and configure Containers using Docker on WSL.
-   Deploy Nginx web server in both environments.
-   Observe system resource utilization.

## 🧰 Tools Used

-   VirtualBox
-   Vagrant
-   Ubuntu
-   WSL
-   Docker
-   Nginx
-   VS Code

------------------------------------------------------------------------

## 🖥️ Part A -- Virtual Machine Setup

### Step 1 -- Download VirtualBox

![Step1](1.png)

### Step 2 -- Install Vagrant

![Step2](2.png)

### Step 3 -- Initialize Vagrant

``` bash
vagrant init hashicorp/bionic64
```

![Step3](3.png)

### Step 4 -- Start VM

``` bash
vagrant up
```

![Step4](4.png)

### Step 5 -- VM Created

![Step5](5.png)

### Step 6 -- VM Running

![Step6](6.png)

### Step 7 -- SSH into VM

``` bash
vagrant ssh
```

![Step7](7.png)

### Step 8 -- Start Nginx in VM

``` bash
sudo systemctl start nginx
```

![Step8](8.png)

### Step 9 -- Verify Nginx

``` bash
curl localhost
```

![Step9](9.png)

### Step 10 -- Virtualization Enabled

![Step10](10.png)

------------------------------------------------------------------------

## 🐳 Part B -- Docker Container Setup

### Step 11 -- Open WSL

![Step11](11.png)

### Step 12 -- Run Docker Nginx

``` bash
docker run -d -p 8080:80 --name nginx-container nginx
```

![Step12](12.png)

### Step 13 -- Verify Container Output

``` bash
curl localhost:8080
```

![Step13](13.png)

### Step 14 -- Monitor using htop

``` bash
htop
```

![Step14](14.png)

### Step 15 -- Check Memory

``` bash
free -h
```

![Step15](15.png)

### Step 16 -- System Analyze

``` bash
systemd-analyze
```

![Step16](16.png)

### Step 17 -- Docker Stats

``` bash
docker stats
```

![Step17](17.png)

------------------------------------------------------------------------

## ✅ Result

Successfully compared VM and Container performance.

## 👨‍💻 Author

Nakul Yadav
