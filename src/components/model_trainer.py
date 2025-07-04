import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
import os
import sys

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info('splitting dependent and independent variables from train and test data')
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet(),
                'DescisionTree':DecisionTreeRegressor(),
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n================================')
            logging.info(f"Model Report:{model_report}")
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(f'Best model founded, Model name: {best_model_name}, R2 score: {best_model_score}')
            print('\n==========================')
            logging.info(f'Best model founded, Model name: {best_model_name}, R2 score: {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            logging.info('Exception occured at model training')
            raise CustomException(e,sys)