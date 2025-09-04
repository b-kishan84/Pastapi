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

from fastapi import FastAPI
import uvicorn

myapp = FastAPI()

@myapp.get('/')
def index():
    return {'data': {'message': 'Welcome to the server'}}

@myapp.get('/about')
def about():
    return {'data': {'message': 'About page'}}

if __name__ == '__main__':
    # Run the server with uvicorn
    uvicorn.run(myapp, host='0.0.0.0', port=8000)
#if file name is bits and instance name is myapp then to run this then cmd for terminal is
# uvicorn bits:myapp --reload
#if i have K.PY file in my github and I rename K.PY file locally in my machine to X.PY and I want push the changes.
"""
mv K.py X.py
git add .
git commit -m "Renamed K.py to X.py"
git push origin main


"""