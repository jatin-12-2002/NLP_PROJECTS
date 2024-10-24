# Name Entity Recognition using BERT

## PROBLEM STAEMENT

In this project we will be prforming one of the most famous task in the field of natural language processing i,e Name Entity Recognition.

## DESCRIPTION OVERVIEW

Named EntitiesRecognition (NER) is a basic task of Natural Language Processing (NLP). The purpose is to identify named entities such as person names, place names, and organization names in the corpus. Due to the increasing number of these named entities, it is usually impossible to exhaustively list them in the dictionary, and their constituent methods have some regularities. Therefore, the recognition of these words is usually included in the task of morphological processing (such as Chinese segmentation). Independent processing, called named entity recognition. 

Named entity recognition technology is an indispensable part of many natural language processing technologies such as information extraction, information retrieval, machine translation, and question answering systems.

Named entities are the research subjects for named entity recognition. Generally, named entities include 3 categories (entity, time, and number) and 7 categories (person, place, institution, time, date, currency, and percentage). Judging whether a named entity is correctly identified includes two aspects: whether the boundary of the entity is correct; and whether the type of the entity is correctly labeled. 

The main types of errors include correct text, which may be of the wrong type; conversely, text boundaries are incorrect, and the main entity words and part-of-speech tokens it contains may be correct.


## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6
- Pytorch 1.4 with GPU support CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/NER_BERT
```

### Step-2: Navigate to the project directory:
```bash
    cd NER_BERT
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
As **pytorch_model.bin** is very large in size(420 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the **pytorch_model.bin** in the **out_base** folder.

You can download the **pytorch_model.bin** from [here](https://www.dropbox.com/scl/fi/arbjwnrhr5frzwzwnok3s/pytorch_model.bin?rlkey=kzc9raj05yo2oqskxbr0yb5dh&st=lq4gf5uj&dl=0)


### Step-6: Run the application:
```bash
    python clientApp.py
```

### Step-7: Prediction application:
```bash
    http://localhost:5000/
```