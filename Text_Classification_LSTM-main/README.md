# Text Classification Using LSTM

## PROBLEM STAEMENT

In this project we will be building a text classifier using LSTM and wor2vec.

## DESCRIPTION OVERVIEW

Text classification  is the task of assigning a set of predefined categories to free-text. Text classifiers can be used to organize, structure, and categorize pretty much anything. For example, new articles can be organized by topics, support tickets can be organized by urgency, chat conversations can be organized by language, brand mentions can be organized by sentiment, and so on.
There are many approaches to automatic text classification, which can be grouped into three different types of systems:
- Rule-based systems
- Machine Learning based systems
- Hybrid systems

Deep learning algorithms such as Word2vec and Glove are also used in order to obtain better vector representations for words and improve the accuracy of classifiers trained with traditional machine learning algorithms.

Few typical applications of text classification technology including all of the following:
- Social media monitoring.
- Brand monitoring.
- Customer service.
- Voice of customer.

## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6 
- Pytorch 1.4 with GPU support CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Text_Classification_LSTM
```

### Step-2: Navigate to the project directory:
```bash
    cd Text_Classification_LSTM
```

### Step 3: Create a conda environment after opening the repository

```bash
    conda create -p env python=3.6 -y
```

```bash
    source activate ./env
```

### Step 4: Install the requirements
```bash
    pip install -r requirements.txt
```

### Step 5: Add the pre-trained model in your project structure. I had trained the model already.
As **data** folder is very large in size(380 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the **data** folder in your project structure.

You can download the **data** folder from [here](https://www.dropbox.com/scl/fo/4s735pff4uqnnbj45htxg/ADB-9Qrh16J0pwgIOKmfLdM?rlkey=1m4bcdbmhwzna6b2do645hw9r&st=o4olb2fa&dl=0)

### Step 6: Add the pre-trained model in your project structure. I had trained the model already.
As **models** is very large in size(1200 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the **models** folder in your project structure.

You can download the **models** folder from [here](https://www.dropbox.com/scl/fi/0tod0lgfq3xh94hkmboju/bert_tagger.h5?rlkey=df9ww7zdzqrx4jovwvreuk188&st=4d61mj4o&dl=0)


### Step-6: Run the application:
```bash
    python main.py
```

### Step-7: Prediction application:
```bash
    http://localhost:5000/
```