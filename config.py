import pymysql
import json
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'config.json')
f = open(file_path)
ConfigData = json.load(f)

def dbConnection():
    # print("=====")
    try:
        conn = pymysql.connect(
            host=ConfigData['Techpath']['Database']['Host'],
            port=int(ConfigData['Techpath']['Database']['Port']),
            user=ConfigData['Techpath']['Database']['User'],
            passwd=ConfigData['Techpath']['Database']['Password'],
            db=ConfigData['Techpath']['Database']['Database']
            )
        return conn
    except pymysql.err.InterfaceError as e:
        print(e)
        print("Database Connection Failed")
        sys.exit()