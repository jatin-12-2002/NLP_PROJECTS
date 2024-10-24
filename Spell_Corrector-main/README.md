# SPELLING CORRECTOR

## PROBLEM STAEMENT

In this project we will be using deep learning approaches to build a spelling corrector.

## DESCRIPTION OVERVIEW

A word needs to be checked for spelling correctness and corrected if necessary, many a time in the context of the surrounding words. A spellchecker points to spelling errors and possibly suggests alternatives. An autocorrector usually goes a step further and automatically picks the most likely word. In case of the correct word already having been typed, the same is retained.

There are different types of spelling errors.

1. Non-word Errors: These are the most common type of errors. You either miss a few keystrokes or let your fingers hurtle a bit longer. E.g., typing langage when you meant language; or hurryu when you meant hurry

2. Real Word Errors: If you have fat fingers, sometimes instead of creating a non-word, you end up creating a real word, but one you didn’t intend. E.g, typing buckled when you meant bucked. Or your fingers are a tad wonky, and you type in three when you meant there.

3. Cognitive Errors: The previous two types of errors result not from ignorance of a word or its correct spelling. Cognitive errors can occur due to those factors. The words piece and peace are homophones (sound the same). So you are not sure which one is which. Sometimes your damn sure about your spellings despite a few grammar nazis claim you’re not.

4. Short forms/Slang/Lingo: These are possibly not even spelling errors. May be u r just being kewl. Or you are trying hard to fit in everything within a text message or a tweet and must commit a spelling sin. We mention them here for the sake of completeness.


## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6 
- Keras 2.2.4 using TensorFlow GPU 1.14.0 backend CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Spell_Corrector
```

### Step-2: Navigate to the project directory:
```bash
    cd Spell_Corrector
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

### Step-5: Run the application:
```bash
    python clientApp.py
```

### Step-6: Prediction application:
```bash
    http://localhost:7000/
```