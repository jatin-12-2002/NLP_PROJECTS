# Semantic Text Similarity

## PROBLEM STAEMENT

In this project we need to fing the similarity for given pair of sentences and calculate the distance between them.

## DESCRIPTION OVERVIEW

Semantic textual similarity deals with determining how similar two pieces of texts are. This can take the form of assigning a score from 1 to 5. Related tasks are paraphrase or duplicate identification.
Semantic similarity is a metric defined over a set of documents or terms, where the idea of distance between them is based on the likeness of their meaning or semantic content as opposed to similarity which can be estimated regarding their syntactical representation (e.g. their string format). These are mathematical tools used to estimate the strength of the semantic relationship between units of language, concepts or instances, through a numerical description obtained according to the comparison of information supporting their meaning or describing their nature. The term semantic similarity is often confused with semantic relatedness. Semantic relatedness includes any relation between two terms, while semantic similarity only includes "is a" relations.

For example, "car" is similar to "bus", but is also related to "road" and "driving".


## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6 
- Pytorch 1.4 with GPU support CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Semantic_Text_Similarity
```

### Step-2: Navigate to the project directory:
```bash
    cd Semantic_Text_Similarity
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

### Step 5: Install the pytorch from the link
```bash
    https://pytorch.org/get-started/locally/
```
```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Step-6: Run the application:
```bash
    python clientApp.py
```

### Step-7: Prediction application:
```bash
    http://localhost:7000/
```