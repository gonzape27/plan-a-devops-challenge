# Plan A DevOps Challenge 2

## Pre-Requesites

* AWS CLI [Installation Ref. https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html]  
* kubectl [Installation Ref. https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html]

## Tools used

In order to follow the tasks asigned, i've used Cloudformation to create the needed resources for the creation of the following points:


> Create code for deploying a VPC in AWS with 2 public and 2 private subnets.

> Create code for deploying an EKS cluster in AWS, which will use the VPC created in the previous step. The cluster must have 2 nodes, using instance type `t3a.large`. The nodes must be on the private subnets only.

## Step 1 – Configure Aws Profile

**Open a terminal. Copy & paste the following** into the terminal window

```
	aws configure --profile plan-a-challenge
		AWS Access Key ID [None]: XXXXXXXXXXXXXXXXX
		AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
		Default region name [None]: us-east-2

```

## Step 2 – Create EKS Cluster 

**Open a terminal. Copy & paste the following** into the terminal window

```	
	aws cloudformation create-stack --stack-name eks-dev-cluster --template-body file://$PWD/cluster.yml --capabilities CAPABILITY_IAM --profile plan-a-challenge

```
## Step 3 – Create EKS Nodes 

**Open a terminal. Copy & paste the following** into the terminal window

```	
	aws cloudformation create-stack --stack-name eks-dev-cluster-ng-dev-Node --template-body file://$PWD/nodes.yml --capabilities CAPABILITY_IAM --profile plan-a-challenge

```
## Step 4 – Configure your kubectl profile

**Open a terminal. Copy & paste the following** into the terminal window

```
	aws eks update-kubeconfig --name eks-dev-cluster --profile plan-a-challenge

```
## Step 5 – Test the connection of the cluster

**Open a terminal. Copy & paste the following** into the terminal window

```
	kubectl get pods --all-namespaces -o wide

```

