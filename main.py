"""from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def index():
    return 'heyy'
"""
# Jason format
"""
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def index():
    return {'data': {'name': 'Aman' }}

@app.get('/about')
def about():
    return 'about page'

"""
#how to make a server
