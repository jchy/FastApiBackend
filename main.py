from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {'data':{'name':'Jaswant Chaudhary'}}

@app.get('/about')
def about():
    return {'data':{'company': 'sourcewiz'}}