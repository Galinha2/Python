from bs4 import BeautifulSoup
import requests

def allkey(nome):
    url1 = f'https://www.allkeyshop.com/blog/catalogue/search-{nome}/'
    pagina1 = requests.get(url1)
    soup1 = BeautifulSoup(pagina1.text, 'html.parser')

    jogos = soup1.findAll('h2', class_="search-results-row-game-title")
    preços = soup1.findAll('div', class_="search-results-row-price")
    preçotot = []

    print('ALLKEYSHOP:')
    for games, prices in zip(jogos, preços):
        print(f'{games.text:<40}  {prices.text.strip()}')
        preçotot.append(float(prices.text.replace('€', '')))
        print('-'*49)
    print(f'TOTAL PREÇOS: {sum(preçotot)}€')
    print(f'NUMERO DE JOGOS: {len(jogos)}')

    print(f'TOTAL PREÇOS: {sum(preçotot)}€')
    print(f'NUMERO DE JOGOS: {len(jogos)}')