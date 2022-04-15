'''
token生成模块
'''
import jwt

# 加密算法
headers = {
    "alg":"HS256",
    "typ":"JWT"
}
# 密钥
SECRET_KEY = "leeshy"

'''生成一个token'''
def token_encode(user_id) -> str:
    if user_id:
        payload = {
            "user_id":user_id
        }
        token = jwt.encode(payload=payload, key=SECRET_KEY,algorithm='HS256',headers=headers)
        return token
    else:
        return None

'''解码token'''
def token_decode(token) -> str:
    payload = jwt.decode(jwt=token,key=SECRET_KEY,verify=False,algorithms='HS256')
    info = payload["user_id"]
    return info