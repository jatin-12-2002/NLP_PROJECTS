# Language Identification Using Deep Convolutional Recurrent Neural Networks

This repository contains the code for the paper "Language Identification Using Deep Convolutional Recurrent Neural Networks", which will be presented at the 24th International Conference on Neural Information Processing (ICONIP 2017).

## Structure of the Repository

- **/data**
  - Scripts to download training data from Voxforge, European Parliament Speech Repository and YouTube. For usage details see the README in that folder.
- **/keras**
  - All the code for setting up and training various models with Keras/Tensorflow.
  - Includes training and prediction script. See `train.py` and `predict.py`.
  - Configure your learning parameters in `config.yaml`.
  - More below
- **/tools**
  - Some handy scripts to clean filenames, normalize audio files and other stuff.
- **/web-server**
  - A demo project for language identification. A small web server with a REST interface for classification and a small web frontend to upload audio files. For more information see README in that folder.

## Requirements

You can install all python requirements with `pip install -r requirements.txt` in the respective folders. You will additionally need to install the following software:
- youtube_dl
- sox

## Models

The repository contains a model for 4 languages (English, German, French, Spanish) and a model for 6 languages (English, German, French, Spanish, Chinese, Russian). You can find these models in the folder `web-server/model`.


#### Training & Prediction

To start a training run, go into the `keras` directory, set all the desired properties and hyperparameters in the config.yaml file and train with Keras:
```
python train.py --config <config.yaml>
```

To predict a single audio file run:
```
python predict.py --model <path/to/model> --input <path/to/speech.mp3>
```
Audio files can be in any format understood by SoX. The pretrained model files need to be caomptible with Keras v1.

To evaluate a trained model you can run:
```
python evaluate.py --model <path/to/model> --config <config.yaml> --testset True
```

You can also create a visualisation of the clusters the model is able to produce by using our `tsne.py` script:
```
python tsne.py --model <path/to/model> --config <config.yaml>
```
In case you are interested in creating a visualization of what kind of patterns excite certain layers the most, you can create such a visualization with the following command:
```
python visualize_conv.py --model <path/to/model>
```

#### Labels
```
0 English,
1 German,
2 French,
3 Spanish,
4 Mandarin Chinese,
5 Russian
```

## PROBLEM STAEMENT

In this project we will be doing language identification over six international lanuages i.e English, German, French, Espanol, Chinese and Russian. Here the user need to give recordings of the specific language as input and finnaly the input language will be predicted.

## DESCRIPTION OVERVIEW

Language  recognization is an important task in the field of natural language processing. Here the user will provide speech recordings of a specific language and then using deep learning approaches we will try to predict the spoken input language.

## TECHNOLOGY USED
Here we will be using:
- Anaconda Python 3.6 
- Keras 2.2.4 using TensorFlow GPU 1.14.0 backend CUDA 10 with CuDNN 10.

## INSTALLATION
Installation of this project is pretty easy. Please do follow the following steps to create a virtual environment and then install the necessary packages in the following environment.

### Step-1: Clone the repository to your local machine:
```bash
    git clone https://github.com/jatin-12-2002/Language_Identification
```

### Step-2: Navigate to the project directory:
```bash
    cd Language_Identification
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

### Step 5: Install the sox using following command:
```bash
    sudo apt-get update
```
```bash
    sudo apt-get install sox
```

### Step-6: Run the application:
```bash
    python clientApp.py
```

### Step-7: Prediction application:
```bash
    http://localhost:5000/
```

## Common Errors and it's solutions:

### Error-1 : 
### model_config = json.loads(model_config.decode('utf-8'))
### AttributeError: 'str' object has no attribute 'decode' 

### Solution-1 :
```bash
  Go to /env/lib/python3.6/site-packages/keras/models.py
  Replace the model_config = json.loads(model_config.decode('utf-8'))
  with model_config = json.loads(model_config)
```