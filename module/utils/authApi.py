import requests
import json
from ..config import Config

class AppInfo(Config) :
    def __init__(self,user='BJM001',environments = 'dev') :
        Config.__init__(self,user,environments)
        
#    def __all__(self):
#        return ['get_Access_Token','revoke_Access_Token','get_Hashkey',]
    
    def get_Access_Token(self):
        headers = {"content-type":"application/json"}
        body = {
            "grant_type":"client_credentials",
            "appkey":self.API_KEY, 
            "appsecret":self.API_SECRET
        }
        PATH = "oauth2/tokenP"
        URL = f"{self.API_BASE_URL}/{PATH}"

        # access_token(보안인증키) POST(request)
        res = requests.post(URL, headers=headers, data=json.dumps(body))
        print("access_token_expired =", res.json()['access_token_token_expired'])
        # token 값 저장
        accessToken = res.json()["access_token"]
        return accessToken


    #revoke accessToken!!!
    def revoke_Access_Token(self, accessToken ):
        headers = {"content-type":"application/json"}
        body = {
            "appkey" : self.API_KEY, 
            "appsecret" : self.API_SECRET, 
            "token" : accessToken
        }
        PATH = "/oauth2/revokeP"
        URL = f"{self.API_BASE_URL}/{PATH}"
        
        res = requests.post(URL,headers = headers, data = json.dumps(body))
        print(res.json()['message'])
        return res.json()['code']


    #HashKey Request!!!
    def get_Hashkey(self,datas):
        PATH = "uapi/hashkey"  # hashkey 경로
        URL = f"{self.API_BASE_URL}/{PATH}"
        headers = {
            'content-Type' : 'application/json',
            'appKey' : self.API_KEY,
            'appSecret' :  self.API_SECRET,
        }
        res = requests.post(URL, headers=headers, data=json.dumps(datas))
        hashkey = res.json()["HASH"]  
        #토큰 발급을 제외한 대부분의 POST 요청에는 해쉬키(Hashkey) 사용이 필수

        return hashkey	
    

__all__=[
    'AppInfo',
]