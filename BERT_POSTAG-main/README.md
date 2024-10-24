# Parts of Speech Tagging using BERT

## PROBLEM STAEMENT

In this project we will be performing one of the most famous task in the field of natural language processing i,e Parts of Speech Tagging using BERT.

## DESCRIPTION OVERVIEW

Part-Of-Speech tagging (POS tagging) is also called grammatical tagging or word-category disambiguation. It is the corpus linguistics of corpus Text data processing techniques for marking meaning and context.

Part-of-speech tagging can be done manually or by a specific algorithm. Using machine learning methods to implement part-of-speech tagging is the research content of Natural Language Processing (NLP). Common part-of-speech tagging algorithms include Hidden Markov Model (HMM), Conditional Random Fields (CRFs), and so on.

Part-of-speech tagging is mainly used in the field of text mining and NLP. It is a preprocessing step for various types of text-based machine learning tasks, such as semantic analysis and coreference resolution.


1. CC Coordinating conjunction
2. CD  Cardinal number
3. DT  Determiner
4. EX Existential there
5. FW Foreign word
6. IN Preposition or subordinating conjunction
7. JJ  Adjective
8. JJR  Adjective, comparative
9. JJS  Adjective, superlative
10. LS  List item marker
11. MD  Modal
12. NN  Noun, singular or mass
13. NNS  Noun, plural
14. NNP  Proper noun, singular
15. NNPS  Proper noun, plural
16. PDT  Predeterminer
17. POS  Possessive ending
18. PRP  Personal pronoun
19. PRP$  Possessive pronoun
20. RB  Adverb
21. RBR  Adverb, comparative
22. RBS  Adverb, superlative
23. RP  Particle
24. SYM  Symbol
25. TO  to
26. UH  Interjection
27. VB Verb, base form
28. VBD  Verb, past tense
29. VBG  Verb, gerund or present participle
30. VBN  Verb, past participle
31. VBP  Verb, non-3rd person singular present
32. VBZ  Verb, 3rd person singular present
33. WDT  Wh-determiner
34. WP  Wh-pronoun
35. WP$  Possessive wh-pronoun
36. WRB  Wh-adverb

## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6 
- Pytorch 1.4 with GPU support CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/BERT_POSTAG
```

### Step-2: Navigate to the project directory:
```bash
    cd BERT_POSTAG
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
As **bert_tagger.h5** and **bert_Postagger.h5** is very large in size(850 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the models in your project structure.

You can download the **bert_tagger.h5** from [here](https://www.dropbox.com/scl/fi/0tod0lgfq3xh94hkmboju/bert_tagger.h5?rlkey=df9ww7zdzqrx4jovwvreuk188&st=4d61mj4o&dl=0)

You can download the **bert_Postagger.h5** from [here](https://www.dropbox.com/scl/fi/29k115bc2f17ykko6sc1y/bert_Postagger.h5?rlkey=zdxqp57y6t3axtoiiwcw0g578&st=r7j5ssms&dl=0)


### Step-6: Run the application:
```bash
    python clientApp.py
```

### Step-7: Prediction application:
```bash
    http://localhost:5000/
```