import requests
import json
from GetTokenHash import get_Access_Token ,get_Hashkey 

 
### 모의투자서비스
APP_KEY = "PS5vi6HpFnvggaAkpT7wy6WgRAjbqt8l8sYP"
APP_SECRET = "dcgOW+38Vm++oeTFzf+nMXs9muqdrFHiIcAPhI6W5+TpT3BYpiwlQO2isQc4L8Ca6491xSZrUdQBf3Ae1xp+1KT8wFxdp63tC4SyUs4TYQl5u4RcH2PwDHrWxG7T/hfG7PfHITsWtvkw0ZXN4kJKj1Vl2C3Q19EEmEZ99tS434th6YoPBWQ="
URL_BASE = "https://openapivts.koreainvestment.com:29443" 


###실전투자서비스
#APP_KEY = PSR13iksWOgZI4g4Xs88htPaW0c5ewqNhUfB
#APP_SECRET = ES9U9rnwkJ2/NxDHP6j1zZj32kz1C9fNxACGH+iII3/X68otmrf+jI/W2ybzRV0H7+Jv2eVzMkyz38dW59ycAJy/PryPzRcO7lu8Ar6gF5/3Erxe4ghGIekYJl21w2pYpPYDH3phpouiIHuSDdarlAz/Vplmx5CBQLka6ZjEwOMCig57g5M=
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