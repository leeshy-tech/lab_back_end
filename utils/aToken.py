'''
token编码和解码模块
'''
import jwt

# 加密算法
headers = {
    "alg":"HS256",
    "typ":"JWT"
}
# 密钥
SECRET_KEY = "leeshy"

def token_encode(user_id) -> str:
    '''编码token'''
    if user_id:
        payload = {
            "user_id":user_id
        }
        token = jwt.encode(payload=payload, key=SECRET_KEY,algorithm='HS256',headers=headers)
        return token
    else:
        return None

def token_decode(token) -> str:
    '''解码token'''
    payload = jwt.decode(jwt=token,key=SECRET_KEY,verify=False,algorithms='HS256')
    info = payload["user_id"]
    return info