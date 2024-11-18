import os
import sys
from ner.configuration.s3_operations import S3Operation
from ner.constants import *
from ner.entity.artifact_entity import ModelEvaluationArtifacts, ModelPusherArtifacts
from ner.entity.config_entity import ModelPusherConfig
from ner.exception import NerException
from ner.logger import logging


class ModelPusher:
    def __init__(
        self,
        model_evaluation_artifact: ModelEvaluationArtifacts,
        model_pusher_config: ModelPusherConfig,
    ) -> None:
        self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = model_pusher_config
        self.awscloud = S3Operation()


    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        try:
            logging.info("Entered the initiate_model_pusher method of Model pusher class")
            if self.model_evaluation_artifact.is_model_accepted == True:

                # Uploading the model to AWS S3 container registry
                self.awscloud.upload_file(
                    bucket_name=self.model_pusher_config.bucket_name,
                    to_filename=AWS_MODEL_NAME,
                    from_filename=os.path.join(self.model_pusher_config.upload_model_path,AWS_MODEL_NAME),
                    remove=False
                )

                logging.info("Model pushed to AWS S3 conatiner registry")

            model_pusher_artifacts = ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.bucket_name,
                trained_model_path=self.model_pusher_config.upload_model_path,
            )

            logging.info(
                "Exited the initiate_model_pusher method of Model pusher class"
            )
            return model_pusher_artifacts

        except Exception as e:
            raise NerException(e, sys) from e