import os
import io
import sys
import keras
import pickle
from PIL import Image
from hate.logger import logging
from hate.constants import *
from hate.exception import CustomException
from keras.utils import pad_sequences
from hate.configuration.s3_operations import S3Operation
from hate.components.data_transforamation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts


class PredictionPipeline:
    def __init__(self):
        self.bucket_name = BUCKET_NAME
        self.model_name = MODEL_NAME
        self.model_path = os.path.join("artifacts", "PredictModel")
        self.awscloud = S3Operation()
        self.data_transformation = DataTransformation(data_transformation_config= DataTransformationConfig,data_ingestion_artifacts=DataIngestionArtifacts)


    
    def get_model_from_aws(self) -> str:
        """
        Method Name :   get_model_from_aws
        Description :   This method to get best model from google cloud storage
        Output      :   best_model_path
        """
        logging.info("Entered the get_model_from_aws method of PredictionPipeline class")
        try:
            # Loading the best model from S3 bucket
            os.makedirs(self.model_path, exist_ok=True)
            best_model_path = os.path.join(self.model_path, self.model_name)
            
            self.awscloud.download_object(bucket_name=self.bucket_name, 
                                          key=self.model_name, 
                                          filename=best_model_path)
            logging.info("Exited the get_model_from_aws method of PredictionPipeline class")
            return best_model_path

        except Exception as e:
            raise CustomException(e, sys) from e
        

    
    def predict(self,best_model_path,text):
        """load image, returns cuda tensor"""
        logging.info("Running the predict function")
        try:
            best_model_path:str = self.get_model_from_aws()
            load_model=keras.models.load_model(best_model_path)
            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)
            
            text=self.data_transformation.concat_data_cleaning(text)
            text = [text]            
            print(text)
            seq = load_tokenizer.texts_to_sequences(text)
            padded = pad_sequences(seq, maxlen=300)
            print(seq)
            pred = load_model.predict(padded)
            pred
            print("pred", pred)
            if pred>0.5:

                print("hate and abusive")
                return "hate and abusive"
            else:
                print("no hate")
                return "no hate"
        except Exception as e:
            raise CustomException(e, sys) from e

    
    def run_pipeline(self,text):
        logging.info("Entered the run_pipeline method of PredictionPipeline class")
        try:

            best_model_path: str = self.get_model_from_aws() 
            predicted_text = self.predict(best_model_path,text)
            logging.info("Exited the run_pipeline method of PredictionPipeline class")
            return predicted_text
        except Exception as e:
            raise CustomException(e, sys) from e