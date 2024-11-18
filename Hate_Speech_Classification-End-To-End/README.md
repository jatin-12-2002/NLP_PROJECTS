# Hate Speech Classification

## Dataset

The dataset used in this project consists of labeled text for **Hate Speech Classification**, where each word in the text is tagged with its corresponding entity label. The dataset follows the typical format with tokens and corresponding labels for various entity types such as **no hate** and **hate and abusive**.

You can either download an existing dataset or use your custom data by formatting it to match the token-label format as required. Here is the Dataset [Link](data/dataset.zip).

You can download the dataset from Kaggle also using this [Link](https://www.kaggle.com/datasets/suchindrakumar057/hate-speech-and-offensive-language-dataset/data).

## Installation

The Code is written in Python 3.8.19. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

## Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/jatin-12-2002/Hate_Speech_Classification
```
### Step 2- Create a conda environment after opening the repository
```bash
conda create -p env python=3.8 -y
```
```bash
source activate ./env
```
### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Create AWS IAM user with following Permissions Enabled

* **AdministratorAccess**
* **AmazonEC2ContainerRegistryFullAccess**
* **AmazonEC2FullAccess**


### Step 5 - Configure your AWS
```bash
aws configure
```

### Step 6 - Enter your AWS Credentials of IAM User
```bash
AWS_SECRET_ACCESS_KEY = ""
AWS_ACCESS_KEY_ID = ""
AWS_REGION = "us-east-1"
AWS_FOLDER = Press Enter and move on
```

### Step 7 - Prepare your Dataset zip file named archive.zip
Your Zip file should contain following folders and files in this order:
```bash
dataset.zip
│
├── imbalanced_data.csv
│
├── raw_data.csv
```

* **Here is my Datset Zip: [LINK](data/dataset.zip)**

### Step 8 - Upload the Dataset zip file to your S3 Bucket
```bash
aws s3 cp path/to/your/archive.zip s3://your-bucket-name/dataset.zip
```

### Step 9 (Optional)- Add best.pt model in model folder
Follow this Step if you don't want to train model for 30 epochs as It will take a long time to complete training. I had already trained model named as **model.h5** for 30 epochs. You need to insert the **tokenizer.pickle** in your project structure.

You can download the **model.h5** from [here](best_model/model.h5)

You can download the **tokenizer.pickle** from [here](best_model/tokenizer.pickle)


### Step 10 - Upload the model.h5 model in your S3 Bucket
```bash
aws s3 cp path/to/your/model.h5 s3://your-bucket-name/model.h5
```

### Step 9 - Run the application server
```bash
python app.py
```

### Step 10 - Prediction application
```bash
http://localhost:8080/

```

### Step 11 - If model is not trained and not present in your S3 bucket
```bash
Run the training Pipeline by clicking on train button in FastAPI UI
```


## AWS Deployment Steps
### Step 1 - Login to AWS console.

### Step 2 - Create IAM user for deployment with following Permissions Enabled

* **AdministratorAccess**
* **AmazonEC2ContainerRegistryFullAccess**
* **AmazonEC2FullAccess**

### Important Points:
1. **EC2 access** : It is virtual machine

2. **ECR**: Elastic Container registry to save your docker image in aws


### Description: About the deployment in the Backend

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

### Step 3 - Create ECR repo to store/save docker image
```bash
Save your ECR URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/hatedemo
```

### Step 4 - Create EC2 machine (Ubuntu)
```bash
Use t2.large or greater size instances only as it is a Computer Vision project
```

### Step 5 - Connect EC2 Instance and Install docker in EC2 Machine:

### Run all the commands given in the **circleci_setup_template.sh** file, in the EC2 Instance Command Line.

### Step 6 - Configure EC2 as self-hosted runner in CircleCI:
```bash
CircleCI-->Self-hosted Runner--> Choose Yes, agree all the terms
```

### Step 7 - Setup CicleCI secrets of your Project:
```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_REGISTRY_ID = "Your AWS account:ID"
```

### Step 8 - Add Inbound Rules in EC2 Instance
```bash
Select your EC2 Instance--> Security groups--> Add Inbound Rules--> Custom TCP(8080 and 0.0.0.0)--> save
```

### Step 9 - Run the Public Port of EC2 Instance
```bash
Public_Address:8080
```