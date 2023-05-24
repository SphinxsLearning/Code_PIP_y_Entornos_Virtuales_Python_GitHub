import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [34, 78, -23]

@app.get("/info")
def get_list():
    return {"name": 101010}

@app.get("/cositas", response_class=HTMLResponse)
def get_list():
    return '''
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    '''

def run():
    store.get_categories()

if __name__ == "__main__":
    run()