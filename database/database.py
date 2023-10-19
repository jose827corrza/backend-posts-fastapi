import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# from main import db_user, db_password, db_name

sql_file_name = "../database.sqlite"
base_path = os.path.dirname(os.path.realpath(__file__))

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
# db_user = 'root'
# db_password = '123456'
# db_name = 'posts_fastapi'

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.sqlite"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(base_path, sql_file_name)}"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    echo=True, #To show in console the progress,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    # autocommit=False,
    # autoflush=False,
    bind=engine,
)

Base = declarative_base()