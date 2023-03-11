import requests
import json

#Access_Token Request!!! 
def get_Access_Token(appKey ,appSecret , urlBase ):
        headers = {"content-type":"application/json"}
        body = {"grant_type":"client_credentials",
                "appkey":appKey, 
                "appsecret":appSecret}
        PATH = "oauth2/tokenP"
        URL = f"{urlBase}/{PATH}"

        # access_token(보안인증키) POST(request)
        res = requests.post(URL, headers=headers, data=json.dumps(body))
        print("access_token_token_expired =", res.json()['access_token_token_expired'])
        # token 값 저장
        ACCESS_TOKEN = res.json()["access_token"]
        return ACCESS_TOKEN
    
    
#HashKey Request!!!
def get_Hashkey(datas,appKey ,appSecret , urlBase ):
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