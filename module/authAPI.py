import requests
import json
from dotenv import dotenv_values

class appInfo :
    def __init__(self):
        env = dotenv_values(f'API.env')
        ### 모의투자서비스
        self.APP_KEY_M = env[f'APP_KEY_M']
        self.APP_SECRET_M = env[f'APP_SECRET_M']
        self.URL_BASE_M = env[f'URL_BASE_M']
        ###실전투자서비스
        self.APP_KEY_S = env[f'APP_KEY_M']
        self.APP_SECRET_S = env[f'APP_SECRET_S']
        self.URL_BASE_S = env[f'URL_BASE_S']   

    def get_Access_Token(self,appKey ,appSecret , urlBase ):
        headers = {"content-type":"application/json"}
        body = {
            "grant_type":"client_credentials",
            "appkey":appKey, 
            "appsecret":appSecret
        }
        PATH = "oauth2/tokenP"
        URL = f"{urlBase}/{PATH}"

        # access_token(보안인증키) POST(request)
        res = requests.post(URL, headers=headers, data=json.dumps(body))
        print("access_token_expired =", res.json()['access_token_token_expired'])
        # token 값 저장
        accessToken = res.json()["access_token"]
        return accessToken


    #revoke accessToken!!!
    def revoke_Access_Token(self,appKey ,appSecret, accessToken  , urlBase ):
        headers = {"content-type":"application/json"}
        body = {
            "appkey" : appKey, 
            "appsecret" : appSecret, 
            "token" : accessToken
        }
        PATH = "/oauth2/revokeP"
        URL = f"{urlBase}/{PATH}"
        
        res = requests.post(URL,headers = headers, data = json.dumps(body))
        print(res.json()['message'])
        return res.json()['code']


    #HashKey Request!!!
    def get_Hashkey(self,datas,appKey ,appSecret , urlBase ):
        PATH = "uapi/hashkey"  # hashkey 경로
        URL = f"{urlBase}/{PATH}"
        headers = {
            'content-Type' : 'application/json',
            'appKey' : appKey,
            'appSecret' : appSecret,
        }
        res = requests.post(URL, headers=headers, data=json.dumps(datas))
        hashkey = res.json()["HASH"]  
        #토큰 발급을 제외한 대부분의 POST 요청에는 해쉬키(Hashkey) 사용이 필수

        return hashkey	