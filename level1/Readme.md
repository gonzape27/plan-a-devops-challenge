# Plan A Challenge 1

## Pre-Requesites

* Python 3.8.10 with Flask module 
* Docker [Install Ref: https://docs.docker.com/get-docker/
* kubectl [Installation Ref. https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html]

## About the project

It's simple application coded in Python with Flask as web server. We have functions.py file which contains the code which executes and 
returns all the data requested for the project.

The functions.py it's imported into server.py which then triggers the fuctions to return the data in json using jsonify from Flask.

Dockerfile:

The Dockerfile it's included on this project, using an Python 3.8.10 alphine version to ensure that the image uses the least possible elements to keep the disk and image size
as low as possible.

Inside the Dockefile we create a specific user to ensure that the application will run as non-root.

To push to your Dockerhub account you need the following commands:

```
	 docker login
	 docker build -t <name>:<your-tag> -f Dockerfile . 
	 docker tag <name>:<your-tag> <your-repo>/<name>:<your-tag>
	 docker push <your-repo>/<name>:<your-tag>
```

## Notes
	*Remember that the template files are related with the personal repository gonzape27. If you want to use your own build, you should change this.
	
## Step 1 – Create kubernets namespaces

**Open a terminal. Copy & paste the following** into the terminal window


```
	 kubectl create namespace plan-a-level-1-namespace

```

## Step 2 – Create Deployment template

**Open a terminal. Copy & paste the following** into the terminal window

```	
	 kubectl apply -f plan-a-level-1-app-deployment.yaml

```
## Step 3 – Create Service template 

**Open a terminal. Copy & paste the following** into the terminal window

```	
	kubectl apply -f plan-a-level-1-app-service.yaml

```
## Step 4 – Check the application result

**Open a terminal. Copy & paste the following** into the terminal window

```
	curl $(kubectl -n plan-a-level-1-namespace describe service plan-a-level-1-app | grep -i "LoadBalancer Ingress" | cut -d ":" -f2)

```