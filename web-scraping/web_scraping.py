import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')[3]
print(parrafo_especial.getText())

columna_lateral = sopa.select('.post-title div')
for div in columna_lateral:
    print(div.getText())
