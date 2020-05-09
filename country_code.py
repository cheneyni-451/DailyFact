from bs4 import BeautifulSoup
import requests

URL = "https://www.cia.gov/library/publications/the-world-factbook/appendix/appendix-d.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table")
body = table.tbody
rows = body.find_all('tr')

for r in rows:
    cols = r.find_all('td')
    print(cols[1].get_text())
