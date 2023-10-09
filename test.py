import pymysql

# Connect to the database
connection = pymysql.connect(host='202.176.1.189',
                             user='remote',
                             password='techpath',
                             database='Resource_Assets'
                             )

print(connection)