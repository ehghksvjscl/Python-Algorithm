import bcrypt
import jwt

hash_pass1 = bcrypt.hashpw(b"password", bcrypt.gensalt()).hex()
print(hash_pass1)

hashed_password = bcrypt.hashpw("password".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(hashed_password.decode())

secret = "secret"

access_token = jwt.encode({"id":"1"}, secret, algorithm="HS256").hex()
