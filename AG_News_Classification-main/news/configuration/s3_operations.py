import os
import sys
from io import StringIO
from typing import List, Union
from news.constants import *
import boto3
import pickle
import botocore
from news.exception import CustomException
from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket
from pandas import DataFrame, read_csv
from news.logger import logging



class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")

    
    def download_object(self,key, bucket_name, filename):
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            # Attempt to download the file
            bucket.download_file(Key=key, Filename=filename)
            logging.info(f"Downloaded file {key} from S3 bucket {bucket_name} to {filename}")
        except botocore.exceptions.ClientError as e:
            # If the file is not found in S3 (404 error)
            if e.response['Error']['Code'] == '404':
                logging.info(f"File {key} not found in bucket {bucket_name}. Proceeding without download.")
            else:
                # Re-raise the exception if it's a different error
                raise
    

    def download_folder(self, folder_key: str, bucket_name: str, local_dir: str) -> None:
        """
        Downloads all files within a specified S3 "folder" to a local directory.

        :param folder_key: Prefix in the S3 bucket that acts as the folder path.
        :param bucket_name: Name of the S3 bucket.
        :param local_dir: Local directory where the files should be downloaded.
        """
        try:
            bucket = self.get_bucket(bucket_name)
            objects = list(bucket.objects.filter(Prefix=folder_key))
            
            # Check if the folder exists in S3 (if no objects are found)
            if not objects:
                logging.info(f"Folder {folder_key} not found in bucket {bucket_name}. Proceeding without download.")
                return
            
            # Download each object in the folder
            for obj in objects:
                if obj.key.endswith("/"):  # Skip folders
                    continue
                # Get the relative path for the file in the folder structure
                relative_path = os.path.relpath(obj.key, folder_key)
                local_file_path = os.path.join(local_dir, relative_path)
                
                # Create local directories if they don't exist
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                
                # Download the file from S3 to the local directory
                bucket.download_file(obj.key, local_file_path)
                logging.info(f"Downloaded {obj.key} to {local_file_path}")

        except Exception as e:
            raise CustomException(e, sys) from e
    

    @staticmethod
    def read_object(
        object_name: str, decode: bool = True, make_readable: bool = False
    ) -> Union[StringIO, str]:

        """
        Method Name :   read_object

        Description :   This method reads the object_name object with kwargs
        
        Output      :   The column name is renamed 
        """
        logging.info("Entered the read_object method of S3Operations class")
        try:
            func = (
                lambda: object_name.get()["Body"].read().decode()
                if decode is True
                else object_name.get()["Body"].read()
            )

            conv_func = lambda: StringIO(func()) if make_readable is True else func()
            logging.info("Exited the read_object method of S3Operations class")
            return conv_func()

        except Exception as e:
            raise CustomException(e, sys) from e

    def get_bucket(self, bucket_name: str) -> Bucket:

        """
        Method Name :   get_bucket

        Description :   This method gets the bucket object based on the bucket_name
        
        Output      :   Bucket object is returned based on the bucket name
        """
        logging.info("Entered the get_bucket method of S3Operations class")
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            logging.info("Exited the get_bucket method of S3Operations class")
            return bucket

        except Exception as e:
            raise CustomException(e, sys) from e


    def is_model_present(self, bucket_name: str, s3_model_key: str) -> bool:

        """
        Method Name :   is_model_present

        Description :   This method validates whether model is present in the s3 bucket or not.
        
        Output      :   True or False
        """
        try:
            bucket = self.get_bucket(bucket_name)
            file_objects = [
                file_object
                for file_object in bucket.objects.filter(Prefix=s3_model_key)
            ]
            if len(file_objects) > 0:
                return True
            else:
                return False

        except Exception as e:
            raise CustomException(e, sys) from e


    def get_file_object(
        self, filename: str, bucket_name: str
    ) -> Union[List[object], object]:
        """
        Method Name :   get_file_object

        Description :   This method gets the file object from bucket_name bucket based on filename 
        
        Output      :   list of objects or object is returned based on filename

        """
        logging.info("Entered the get_file_object method of S3Operations class")
        try:
            bucket = self.get_bucket(bucket_name)
            lst_objs = [object for object in bucket.objects.filter(Prefix=filename)]
            func = lambda x: x[0] if len(x) == 1 else x
            file_objs = func(lst_objs)
            logging.info("Exited the get_file_object method of S3Operations class")
            return file_objs

        except Exception as e:
            raise CustomException(e, sys) from e


    def load_model(
        self, model_name: str, bucket_name: str, model_dir: str = None
    ) -> object:

        """
        Method Name :   load_model

        Description :   This method loads the model_name from bucket_name bucket with kwargs
        
        Output      :   list of objects or object is returned based on filename
        """
        logging.info("Entered the load_model method of S3Operations class")

        try:
            func = (
                lambda: model_name
                if model_dir is None
                else model_dir + "/" + model_name
            )
            model_file = func()
            f_obj = self.get_file_object(model_file, bucket_name)
            model_obj = self.read_object(f_obj, decode=False)
            model = pickle.loads(model_obj)
            logging.info("Exited the load_model method of S3Operations class")
            return model

        except Exception as e:
            raise CustomException(e, sys) from e


    def create_folder(self, folder_name: str, bucket_name: str) -> None:

        """
        Method Name :   create_folder

        Description :   This method creates a folder_name folder in bucket_name bucket
        
        Output      :   Folder is created in s3 bucket
        """
        logging.info("Entered the create_folder method of S3Operations class")

        try:
            self.s3_resource.Object(bucket_name, folder_name).load()

        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                folder_obj = folder_name + "/"
                self.s3_client.put_object(Bucket=bucket_name, Key=folder_obj)
            else:
                pass
            logging.info("Exited the create_folder method of S3Operations class")


    def check_folder_exists(self, folder_key, bucket_name):
        """
        Check if a folder exists in the specified S3 bucket.
        """
        try:
            logging.info(f"Checking if folder '{folder_key}' exists in bucket '{bucket_name}'")
            response = self.s3_client.list_objects_v2(
                Bucket=bucket_name,
                Prefix=folder_key
            )
            exists = 'Contents' in response
            logging.info(f"Folder '{folder_key}' exists: {exists}")
            return exists
        except Exception as e:
            raise CustomException(e, sys) from e
    
    
    def upload_file(
        self,
        from_filename: str,
        to_filename: str,
        bucket_name: str,
        remove: bool = True,
    ) -> None:

        """
        Method Name :   upload_file

        Description :   This method uploads the from_filename file to bucket_name bucket with to_filename as bucket filename
        
        Output      :   Folder is created in s3 bucket
        """
        logging.info("Entered the upload_file method of S3Operations class")
        try:
            logging.info(
                f"Uploading {from_filename} file to {to_filename} file in {bucket_name} bucket"
            )

            self.s3_resource.meta.client.upload_file(
                from_filename, bucket_name, to_filename
            )
            logging.info(
                f"Uploaded {from_filename} file to {to_filename} file in {bucket_name} bucket"
            )

            if remove is True:
                os.remove(from_filename)
                logging.info(f"Remove is set to {remove}, deleted the file")
            else:
                logging.info(f"Remove is set to {remove}, not deleted the file")
            logging.info("Exited the upload_file method of S3Operations class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def upload_folder(self, folder_name: str, bucket_name: str, bucket_folder_name: str) -> None:
        """
        Uploads the entire folder to S3, preserving the directory structure.

        :param folder_name: Path to the local folder to upload.
        :param bucket_name: Name of the S3 bucket.
        :param bucket_folder_name: Path in the bucket where the folder will be uploaded.
        """
        logging.info("Entered the upload_folder method of S3Operations class")
        try:
            for root, _, files in os.walk(folder_name):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    # Compute the relative path for the file
                    relative_path = os.path.relpath(local_file_path, folder_name)
                    # Form the destination path in S3
                    s3_file_path = os.path.join(bucket_folder_name, relative_path).replace("\\", "/")  # Ensure S3-compatible paths
                    # Upload the file
                    self.upload_file(
                        from_filename=local_file_path,
                        to_filename=s3_file_path,
                        bucket_name=bucket_name,
                        remove=False,
                    )
            logging.info(f"Successfully uploaded folder {folder_name} to {bucket_name}/{bucket_folder_name}")
        except Exception as e:
            raise CustomException(e, sys) from e


    def upload_df_as_csv(
        self,
        data_frame: DataFrame,
        local_filename: str,
        bucket_filename: str,
        bucket_name: str,
    ) -> None:

        """
        Method Name :   upload_df_as_csv

        Description :   This method uploads the dataframe to bucket_filename csv file in bucket_name bucket 
        
        Output      :   Folder is created in s3 bucket
        """
        logging.info("Entered the upload_df_as_csv method of S3Operations class")
        try:
            data_frame.to_csv(local_filename, index=None, header=True)
            self.upload_file(local_filename, bucket_filename, bucket_name)
            logging.info("Exited the upload_df_as_csv method of S3Operations class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def get_df_from_object(self, object_: object) -> DataFrame:

        """
        Method Name :   get_df_from_object

        Description :   This method gets the dataframe from the object_name object 
        
        Output      :   Folder is created in s3 bucket
        """
        logging.info("Entered the get_df_from_object method of S3Operations class")

        try:
            content = self.read_object(object_, make_readable=True)
            df = read_csv(content, na_values="na")
            logging.info("Exited the get_df_from_object method of S3Operations class")
            return df

        except Exception as e:
            raise CustomException(e, sys) from e

    def read_csv(self, filename: str, bucket_name: str) -> DataFrame:

        """
        Method Name :   get_df_from_object

        Description :   This method gets the dataframe from the object_name object 
        
        Output      :   Folder is created in s3 bucket

        """
        logging.info("Entered the read_csv method of S3Operations class")
        try:
            csv_obj = self.get_file_object(filename, bucket_name)
            df = self.get_df_from_object(csv_obj)
            logging.info("Exited the read_csv method of S3Operations class")
            return df

        except Exception as e:
            raise CustomException(e, sys) from e