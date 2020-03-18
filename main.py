import requests as r
import json as js
import base64
def base64_decode(code):
    decode=base64.b64decode(code).decode("utf-8")
    return decode
username=input("Please input your username: ")
mojang_api='https://api.mojang.com/users/profiles/minecraft/'
url=mojang_api+str(username)
try:
    api_callback=r.get(url,timeout=60)
    if(api_callback.status_code!=200):
        print("Please make sure that the username you input is correct!")
        exit()
except:
    print('Error, please check your network connection!')
    exit()
callback_text=api_callback.text
data=js.loads(callback_text)
sessionserver='https://sessionserver.mojang.com/session/minecraft/profile/'
url=sessionserver+data['id']
try:
    callback=r.get(url,timeout=60)
except:
    print('Error, please check your network connection!')
    exit()
callback_text=callback.text
callback_data=js.loads(callback_text)
try:
    properties=callback_data['properties']
except:
    print('KeyError, please check your network connection!')
    exit()
value=properties[0]['value']
result=base64_decode(value)
textures=js.loads(result)['textures']
skin=textures['SKIN']
skin_url=skin['url']
print('The skin URL of {} is {}'.format(username,skin_url))