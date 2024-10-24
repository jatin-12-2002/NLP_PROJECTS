# Text Summarization with BART-LARGE

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/TEXT_Summarization_BART_LARGE
```

### Step-2: Navigate to the project directory:
```bash
    cd TEXT_Summarization_BART_LARGE
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

### Step 6: Add the pre-trained model in your project structure. I had trained the model already.
As **model** is very large in size(600 MB), So I cannot push it into github repository directly. So, you had to update it manually in and you had to insert the model folder in your project structure.

You can download the **model** from [here](https://drive.google.com/drive/folders/18thJ3tCBd4BUTqHE9chj_Y8fQw-8Nz_G?usp=sharing)

### Step-7: Run the application:
```bash
    python run app.py
```

### Step-8: Prediction application:
```bash
    http://localhost:5000/
```