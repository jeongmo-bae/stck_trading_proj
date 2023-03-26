import requests
import json
from SetAppInfo import *
from GetTokenHash import *

aid = appInfo()


accessToken = get_Access_Token(aid.APP_KEY_M, aid.APP_SECRET_M, aid.URL_BASE_M)


#DATA GET --> ACCESS_TOKEN 필요!
PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
URL = f"{aid.URL_BASE_M}/{PATH}"

headers = {"Content-Type":"application/json", 
           "authorization": f"Bearer {accessToken}",
           "appKey":aid.APP_KEY_M,
           "appSecret":aid.APP_SECRET_M,
           "tr_id":"FHKST01010100"}
params = {
    "FID_COND_MRKT_DIV_CODE":"J",
    "FID_INPUT_ISCD":"005930"
}

res = requests.get(URL, headers=headers, params=params)
print(res.json()['output'])


revoke_Access_Token(aid.APP_KEY_M, aid.APP_SECRET_M, accessToken ,aid.URL_BASE_M)