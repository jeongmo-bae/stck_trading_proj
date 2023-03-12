import requests
import json
from GetTokenHash import get_Access_Token ,get_Hashkey 

 
### 모의투자서비스
APP_KEY = ""
APP_SECRET = ""
URL_BASE = "https://openapivts.koreainvestment.com:29443" 


###실전투자서비스
#APP_KEY = 
#APP_SECRET = 
#URL_BASE = "https://openapi.koreainvestment.com:9443"   


accessToken = get_Access_Token(APP_KEY,APP_SECRET,URL_BASE)


#DATA GET --> ACCESS_TOKEN 필요!
PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
URL = f"{URL_BASE}/{PATH}"

headers = {"Content-Type":"application/json", 
           "authorization": f"Bearer {accessToken}",
           "appKey":APP_KEY,
           "appSecret":APP_SECRET,
           "tr_id":"FHKST01010100"}
params = {
    "FID_COND_MRKT_DIV_CODE":"J",
    "FID_INPUT_ISCD":"005930"
}

res = requests.get(URL, headers=headers, params=params)
print(res.json()['output'])