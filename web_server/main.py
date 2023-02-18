import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse 

app =FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

'''
@app.get('/contact')
def get_list():
    return {'name': 'platzi'}
'''
#para retornar HTML
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return"""
    <h1>JUAN DIEGO</h1>
    <p>este es mi primer servidor</p>
    """




def run():
    store.get_categories()

if __name__ =='__main__':
    run()

#----------

    