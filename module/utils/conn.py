import mysql.connector
from mysql.connector import Error
from ..config import Config


class MyConn(Config) :
    def __init__(self,user='BJM001',environments = 'dev') :
        Config.__init__(self,user,environments)
        
    def get_mysql_conn(self):
        try :
            connection = mysql.connector.connect(
                host=self._HOST,
                #database='',
                user=self._MYID,
                password=self._MYPW
            )
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print(f"### {self._MYID} Connected to MySQL Server version :{db_Info} ###")            
        except Error as e:
            print(f"### Error while connecting to MySQL ###\n{e}")
        
        return connection

__all__=[
    'MyConn',
]
