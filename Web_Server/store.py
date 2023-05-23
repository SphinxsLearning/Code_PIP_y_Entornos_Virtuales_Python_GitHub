import requests

api_url_categories = "https://api.escuelajs.co/api/v1/categories"

def get_categories():
    r = requests.get(api_url_categories)
    print(r.status_code)
    print(type(r.status_code))
    # Por defecto la api nos devuelve la información en formato de String.
    print(r.text)
    print(type(r.text))
    # Para transformar del formato string a una lista usamos el siguiente metodo.
    categories = r.json()
    print(categories)
    print(type(categories))