import os
from dotenv import dotenv_values

current_file_path = os.path.abspath(__file__)
package_top_directory = os.path.dirname(current_file_path)

class Config:
    base_dir = package_top_directory
    def __init__(self,user = 'BJM001',environments = 'dev'):
        env_api = dotenv_values(f'{Config.base_dir}/API.env')
        if environments == 'dev' : 
            self.API_KEY = env_api[f'API_KEY_M']
            self.API_SECRET = env_api[f'API_SECRET_M']
            self.API_BASE_URL = env_api[f'API_BASE_URL_M']
        else : 
            self.API_KEY = env_api[f'API_KEY_S']
            self.API_SECRET = env_api[f'API_SECRET_S']
            self.API_BASE_URL = env_api[f'API_BASE_URL_S']   

        env_db = dotenv_values(f'{Config.base_dir}/DB.env')
        self._HOST = env_db[f'HOST']
        self._MYID = env_db[f'MYID_{user}']
        self._MYPW = env_db[f'MYPW_{user}']

__all__=[
    'package_top_directory',
    'Config',
]