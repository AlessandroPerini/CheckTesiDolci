from databaseConnection import DBConnection
from tabulate import tabulate
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn import tree
from utility import Utility


class OneHotEncoding:

    def encoder(self, data_frame):
        """

        :param data_frame: dataframe x on witch will be done the one-hot-encoding
        :return: dataframe encoded: it deletes columns with less than 5 distinct values and adds a number of columns
        equal to the distinct values deleted. in each column values will be 0 or 1.
        """
        try:
            result = pd.DataFrame()

            for column in data_frame.columns:
                temp_df = pd.DataFrame(data_frame[column])

                if data_frame[column].dtype == np.int64:
                    result = pd.concat([result, temp_df], axis=1)

                else:
                    if len(data_frame[column].unique()) <= 5:
                        result = pd.concat([result, self.one_hot_encoding(data_frame[column])], axis=1)

            return result

        except ValueError as ve:
            print(ve)
            print("Invalid dataframe")

    @staticmethod
    def one_hot_encoding(column):
        """

        :param column: column on witch will be done the encoding
        :return: the dataframe with the columns changed that have to be added to the initial database
        """

        try:
            column_names = column.unique()
            encoder = preprocessing.OneHotEncoder(categories=[column_names])
            result = pd.DataFrame(encoder.fit_transform(pd.DataFrame(column)).toarray())
            result.columns = column_names
            return result

        except ValueError as ve:
            print(ve)
            print("Invalid column")
