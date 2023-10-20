from dotenv import load_dotenv
from fastapi import FastAPI



# Load the .env
load_dotenv()

# Project
from middlewares.error_handler import ErrorHandler
from database.database import Base, engine


from routes import posts, auth



# Import models before call create_call()
from models import post

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'Tweets FastAPI',
    description='API that emulates the func of X',
    version='0.0.1',
    contact={
        "name": "joseDev",
        "url": 'https://github.com/jose827corrza',
        "email": 'jose.corrzadeveloper@gmail.com'
    }
)

# Add middleware to the whole app
app.add_middleware(ErrorHandler)



app.include_router(posts.router)
app.include_router(auth.router)

@app.get('/',tags=['Home'])
def hello():
    return 'Hello Tweets!'

