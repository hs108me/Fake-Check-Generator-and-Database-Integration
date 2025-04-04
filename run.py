import os
import glob
import csv
import configparser
from database_class import Database

current_directory = os.getcwd()
config = configparser.ConfigParser()
config_path = os.path.join(current_directory, 'config.ini')
config.read(config_path)

DATABASE = config['database_info']['DATABASE']
USER = config['database_info']['USER']
PASSWORD = config['database_info']['PASSWORD']
HOST = config['database_info']['HOST']
PORT = int(config['database_info']['PORT'])  

files_path = os.path.join(current_directory, 'data')
files_list = glob.glob(os.path.join(files_path, '[0-9]*_[0-9].csv'))

try:
    db = Database(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    
    for file in files_list:
        with open(file, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')

            for row in reader:
                data = (row['doc_id'], row['item'], row['category'], row['amount'], row['price'], row['discount'])
                db.insert_data(data)
        os.remove(file) # delete file after adding to database

except Exception as e:
    print(f"Error: {e}")

finally:
    db.close_connection()