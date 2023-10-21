import bcrypt

def hash_password(unhashed_password: str):
    hashed_password = bcrypt.hashpw(unhashed_password.encode(), bcrypt.gensalt(13))
    print(hash_password)
    return hashed_password

def check_password(password: str, hashed_password: str):
    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        return True
    else:
        return False
