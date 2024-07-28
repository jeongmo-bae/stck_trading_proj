import requests
import json
from .module.utils.authAPI import *

aif = appInfo()
accessToken = aif.get_Access_Token(aif.APP_KEY_M, aif.APP_SECRET_M, aif.URL_BASE_M)

#DATA GET --> ACCESS_TOKEN 필요!
PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
URL = f"{aif.URL_BASE_M}/{PATH}"

headers = {"Content-Type":"application/json", 
           "authorization": f"Bearer {accessToken}",
           "appKey":aif.APP_KEY_M,
           "appSecret":aif.APP_SECRET_M,
           "tr_id":"FHKST01010100"}
params = {
    "FID_COND_MRKT_DIV_CODE":"J",
    "FID_INPUT_ISCD":"005930"
}

res = requests.get(URL, headers=headers, params=params)
print(res.json()['output'])


aif.revoke_Access_Token(aif.APP_KEY_M, aif.APP_SECRET_M, accessToken ,aif.URL_BASE_M)