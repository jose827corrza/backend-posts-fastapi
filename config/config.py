import os

def load_variables():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    jwt_key = os.getenv('JWT_SECRET_KEY')
    return db_user, db_password, db_name, jwt_key