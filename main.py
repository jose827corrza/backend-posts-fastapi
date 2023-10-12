from fastapi import FastAPI

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


@app.get('/',tags=['Home'],)
def hello():
    return 'Hello Tweets!'