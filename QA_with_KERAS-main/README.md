# Question-Answering using KERAS

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/QA_with_KERAS
```

### Step-2: Navigate to the project directory:
```bash
    cd QA_with_KERAS
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

### (Optional) Step 6 : Train the model 
```bash
    python trainQnAModel.py
```

### Step-7: Run the application:
```bash
    python main.py
```

### Step-8: Prediction application:
```bash
    http://localhost:7000/
```
