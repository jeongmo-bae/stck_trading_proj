import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values

class DbConn :
    def __init__(self,user='ROOT') :
        env = dotenv_values(f'DB.env')
        self._HOST = env[f'HOST']
        self._ID = env[f'UID_{user}']
        self._PW = env[f'PW_{user}']
        self.myconn = self.get_mysql_conn(self._ID,self._PW)
        
    def get_mysql_conn(self,host,user,password):
        try :
            connection = mysql.connector.connect(
                host=host,
                #database='',
                user=user,
                password=password
            )
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print(f"### {user} Connected to MySQL Server version :{db_Info} ###")            
        except Error as e:
            print(f"### Error while connecting to MySQL ###\n{e}")
        
        return connection
