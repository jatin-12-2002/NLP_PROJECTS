# Abstractive Text Summarization Using BERT-UnCased

## DESCRIPTION OVERVIEW
I have used a text generation library called Texar , Its a beautiful library with a lot of abstractions, i would say it to be 
scikit learn for text generation problems.

The main idea behind this architecture is to use the transfer learning from pretrained BERT a masked language model ,
I have replaced the Encoder part with BERT Encoder and the deocder is trained from the scratch.

One of the advantages of using Transfomer Networks is training is much faster than LSTM based models as we elimanate sequential behaviour in Transformer models.

Transformer based models generate more gramatically correct  and coherent sentences.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Text_Abstraction_BERT
```

### Step-2: Navigate to the project directory:
```bash
    cd Text_Abstraction_BERT
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

### Step 5: Add the pre-trained model in your project structure.
As **uncased_L-12_H-768_A-12** model is very large in size(450 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the models in your project structure.

You can download the **uncased_L-12_H-768_A-12** model from [here](https://www.dropbox.com/scl/fo/s37rn0v3sfg57a7tg7wk1/AJHk4L58jifXm8ckB8xP1JA?rlkey=ahfz99pjnvsw7c0ksxok09dfy&st=68jre1q0&dl=0)

OR **Directly download from the link using:**
```bash
    wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
```
```bash
    unzip uncased_L-12_H-768_A-12.zip
```

### Step 6: Place the story and summary files under data folder with the following names.
```bash
    train_story.txt
    train_summ.txt
    eval_story.txt
    eval_summ.txt

each story and summary must be in a single line (see sample text given in data folder)
```

### Step 7: Run Preprocessing. This creates two tfrecord files under the data folder.
```bash
    python preprocess.py
```

### (Optional) Step 8: Add the trained model in your project structure. I had trained the model already.
As **models** folder is very large in size(950 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the models in your project structure.

You can download the **models** folder from [here](https://www.dropbox.com/scl/fo/hgotr2sxe2iqtvu3fhqys/ALtloDxjMXD-AbmtrXhBOW4?rlkey=89vxdx4piuhnwzo32cvxgzlnf&st=rsqenouq&dl=0)


### Step-9: Run the application. Configurations for the model can be changes from config.py file:
```bash
    python main.py
```

### Step-10: Prediction application:
```bash
    http://localhost:5000/
```

### (Optional) Step-11: For Inference, Run the command:
```bash
    python inference.py
```
```bash
This code runs a flask server.
Use postman to send the POST request @http://your_ip_address:1118/results. 
with two form parameters story,summary
```