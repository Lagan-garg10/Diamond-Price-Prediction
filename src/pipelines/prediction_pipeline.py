import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_obj
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')
            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info('exception occured in prediction')
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                carat:float,
                depth:float,
                table:float,
                x:float,
                y:float,
                z:float,
                cut:str,
                color:str,
                clarity:str):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'color':[self.color],
                'clarity':[self.clarity],
                'cut':[self.cut]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('data gathered')
            return df
        except Exception as e:
            logging.info('error occured while gathering data')
            raise CustomException(e,sys)