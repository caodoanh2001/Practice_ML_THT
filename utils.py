import xlrd
import numpy as np
import pickle
import pyodbc

from sklearn.datasets import fetch_olivetti_faces
from sklearn.metrics import mean_squared_error

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor

from sklearn.tree import DecisionTreeRegressor
from sklearn.multioutput import MultiOutputRegressor

from sklearn.model_selection import train_test_split

''' Read config db '''
with open('./configs/config_db.txt') as f:
    config_db = f.read()

config_db = config_db.split('\n')
cfg_driver = config_db[0].split('Driver=')[-1]
cfg_server = config_db[1].split('Server=')[-1]
cfg_database = config_db[2].split('Database=')[-1]
cfg_trusted_connection = config_db[3].split('Trusted_Connection=')[-1]
cfg_data_table_name = config_db[4].split('DATA_Table_name=')[-1]
cfg_input_table_name = config_db[5].split('Input_Table_name=')[-1]
cfg_output_table_name = config_db[6].split('Output_Tabe_name=')[-1]

def read_data_from_excel(loc):
    '''
    Read data
    Input: Excel file path
    Ouput:
        X (np.array): numpy array contains samples for training
        Y (np.array): numpy array contains labels
    '''
    X = []
    y = []
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for row in range(1,sheet.nrows):
        X.append(sheet.row_values(row)[0:3])
        y.append(sheet.row_values(row)[3:])
    
    X = np.array(X)
    y = np.array(y)
    return X,y

def save_model(model, model_name):
    '''
    Save model
    Input: model (trained model), model_name
    Output: <model_name>.pkl
    '''
    try:
        with open(model_name, 'wb') as file:  
            pickle.dump(model, file)
        print('Save sucessfully')
    except:
        print('Sth wrong')

def load_model(model_name):
    '''
    Load model
    Input: .pkl file path
    Output: trained model.
    '''
    with open(model_name, 'rb') as file:  
        Pickled_Model = pickle.load(file)
    return Pickled_Model
    
def read_data_from_SQL():
    '''
    Read Data from SQL
    Output: X_data (np.array includes training samples)
            y_data (np.array includes labels)
    '''
    try:
        conn = pyodbc.connect('Driver={};'
                        'Server={};'
                        'Database={};'
                        'Trusted_Connection={};'.format(cfg_driver, cfg_server, cfg_database, cfg_trusted_connection))
    except Exception as e: print(e)
        

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM {}.dbo.{}'.format(cfg_database, cfg_data_table_name))

    X_data = []
    y_data = []
    for row in cursor:
        X_data.append(row[1:4])
        y_data.append(row[4:])
    return np.array(X_data), np.array(y_data)

def load_input_from_SQL():
    '''
    Read Input from SQL
    Output: X_data (np.array includes 1 input)
    '''
    try:
        conn = pyodbc.connect('Driver={};'
                        'Server={};'
                        'Database={};'
                        'Trusted_Connection={};'.format(cfg_driver, cfg_server, cfg_database, cfg_trusted_connection))
    except Exception as e: print(e)

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM {}.dbo.{}'.format(cfg_database, cfg_input_table_name))

    for row in cursor:
        return np.array(row[1:])

def save_output_to_SQL(output):
    '''
    Save output to SQL
    '''
    try:
        conn = pyodbc.connect('Driver={};'
                        'Server={};'
                        'Database={};'
                        'Trusted_Connection={};'.format(cfg_driver, cfg_server, cfg_database, cfg_trusted_connection))
    except Exception as e: print(e)

    cursor = conn.cursor()

    output = tuple([i for i in output])
    # print('INSERT INTO {}.{} VALUES {}'.format(cfg_database, cfg_output_table_name, str(output)))
    cursor.execute('INSERT INTO {}.dbo.{} VALUES {}'.format(cfg_database, cfg_output_table_name, str(output)))
    cursor.commit()