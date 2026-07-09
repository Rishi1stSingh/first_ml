import os
import sys
from src.logger import logging
from src.exception import custom_exception
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class data_ingestion_config:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    data_data_path = os.path.join('artifacts','data.csv')


class dataingestion:
    def __init__(self):
        self.ingestion_config = data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion component")
        try:
            df = pd.read_csv(r"C:\Users\singh\OneDrive\Desktop\new_ml_end_to_end\notebook\data\stud.csv")
            logging.info("read the data in df")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.data_data_path,index=False,header=True)

            logging.info("train test split initialted")
            
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise custom_exception(str(e),sys)
            pass


if __name__=='__main__':
    one = dataingestion()
    one.initiate_data_ingestion()