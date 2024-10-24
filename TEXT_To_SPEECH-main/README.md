# TEXT to SPEECH

## PROBLEM STAEMENT
In this project our goal is to acheive the problem of converting textual data into speech data.

## DESCRIPTION OVERVIEW
As we know, some people have difficulty reading large amounts of text due to dyslexia and other learning disabilities. Some people have basic literary levels. They often get frustrated trying to browse the internet because so much of it is in text form or on other hand some people prefer to listen or watch a news article (or something like this) instead of reading. So to solve all these problems a concept comes into mind that is ”text to speech”.

Text-to-speech (TTS) technology reads aloud digital text. It can take words on computers, smartphones, tablets and convert them into audio.

We will be using Google Text to Speech commonly known as the gTTS API. It is very easy to use the library which converts the text entered, into an audio file which can be saved as a mp3 file. It supports several languages and the speech can be delivered in any one of the two available audio speeds, fast or slow.


## TECHNOLOGY USED

### Anaconda 
### Python 3.6 
### GTTS

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/TEXT_To_SPEECH
```

### Step-2: Navigate to the project directory:
```bash
    cd TEXT_To_SPEECH
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
    http://localhost:5000/
```