import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
r = requests.get(URL)

teams = []
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table', attrs={'class': 'clasament_general white-shadow'})
for row in table.findAll('tr', attrs={'class': 'echipa_row'}):
    echipa = row.find('td', attrs={'class': 'echipa'}).text
    pozitie = row.find('td', attrs={'class': 'poz'}).text
    teams.append({
        'nume-echipa': echipa,
        'pozitie-clasament': pozitie
    })

print(teams)
