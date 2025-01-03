import os
import sys
from exception import CustomException
from logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

import pandas as pd

from data_transformation import DataTransformation
from model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.cvs")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
    
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('E:\ML Projects\MLProject\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            logging.info('Train test split initiated')

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            #os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    obj2=DataTransformation()
    train_arr,test_arr,_=obj2.initiate_data_transformation(train_data,test_data)

    obj3=ModelTrainer()
    print(obj3.initiate_model_trainer(train_arr,test_arr))




