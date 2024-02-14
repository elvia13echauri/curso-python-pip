import store
from fastapi import FastAPI #importar la app
from fastapi.responses import HTMLResponse

#instanciamiento de la app
app = FastAPI()

#Recurso
@app.get('/') #adornador
def getList():
    return [1,2,3]

@app.get('/contact',response_class = HTMLResponse)
def getList():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Soy un parrafo</p>
    """

def run():
    store.getCategories()

if __name__ == '__main__':
    run()

