from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

link_container=[]

def search(reference):
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    response = get(reference, headers=headers)
    return response

def organize(response,brand):
    print("\nListings for: "+brand)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('a', href=True):
        if(("anuncio" in a['href']) or ("carros-usados" in a['href'])):
            if(a['href'] not in link_container):
                if(("1-6" in a['href'])):
                    link_container.append(a['href'])
                    print("Found: "+a['href'])

# ate 2000€ / arcozelo e arredores ate +50km / motor 1.6
# combustivel (todos) pois pode ser adicionado anuncio como GPL e Gasolina
print("Options: 1- OLX / 2- CustoJusto\nOption:")
x = input()
if(x=="1"):
    print("Searching OLX...")
    organize(search("https://www.olx.pt/carros-motos-e-barcos/carros/arcozelo-porto/q-vw/?search[filter_float_price%3Ato]=2000&search[dist]=50"),"VW")
    organize(search("https://www.olx.pt/carros-motos-e-barcos/carros/arcozelo-porto/q-seat/?search[filter_float_price%3Ato]=2000&search[dist]=50"),"Seat")
    organize(search("https://www.olx.pt/carros-motos-e-barcos/carros/arcozelo-porto/q-audi/?search[filter_float_price%3Ato]=2000&search[dist]=50"),"Audi")
    organize(search("https://www.olx.pt/carros-motos-e-barcos/carros/arcozelo-porto/q-skoda/?search[filter_float_price%3Ato]=2000&search[dist]=50"),"Skoda")
    print("\n\nDone!")
elif(x=="2"):
    print("\nSearching CustoJusto Porto...")
    organize(search("https://www.custojusto.pt/porto/veiculos/carros-usados/vw?pe=3"),"VW")
    organize(search("https://www.custojusto.pt/porto/veiculos/carros-usados/seat?pe=3"),"Seat")
    organize(search("https://www.custojusto.pt/porto/veiculos/carros-usados/audi?pe=3"),"Audi")
    organize(search("https://www.custojusto.pt/porto/veiculos/carros-usados/skoda?pe=3"),"Skoda")
    print("\nSearching CustoJusto Aveiro...")
    organize(search("https://www.custojusto.pt/aveiro/veiculos/carros-usados/vw?pe=3"),"VW")
    organize(search("https://www.custojusto.pt/aveiro/veiculos/carros-usados/seat?pe=3"),"Seat")
    organize(search("https://www.custojusto.pt/aveiro/veiculos/carros-usados/audi?pe=3"),"Audi")
    organize(search("https://www.custojusto.pt/aveiro/veiculos/carros-usados/skoda?pe=3"),"Skoda")
    print("\n\nDone!")
else:
    print("Bad Option!")
