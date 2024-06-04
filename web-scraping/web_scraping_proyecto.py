import bs4
import requests

# Crear una url sin tener número de páginas
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de Títulos con cuatro o cinco estrellas
titulos_rating_alto = []

# Iterar páginas
for pagina in range(1, 51):
    # Crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar en los libros
    for libro in libros:
        # Chequear que tenga cuatro o cinco estrellas
        if len(libro.select('.star-rating.Four')) > 0 or len(libro.select('.star-rating.Five')) > 0:
            # Guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

    # Imprimir la lista en cónsola
    for titulo in titulos_rating_alto:
        print(titulo)
