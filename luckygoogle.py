#! python
# luckygoogle.pl - script responsible for opening few searching result from Google Search

from bs4 import element
import requests
import sys
import webbrowser
import bs4
from pprint import pprint

print('Searching...')
res = requests.get('http://google.pl/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

with open("debug-html.html", "w") as file:
    file.write(res.text)


soup = bs4.BeautifulSoup(res.text, features="html.parser")

link_elems = soup.select('a')
link_elems = [
    a
    for a in link_elems
    if a.get('href', '/url?q=').startswith('/url?q=')
]
links = [a.get('href') for a in link_elems]
links = {
    link.split('&')[0]: link
    for link in links 
    if 'google' not in link
}
pprint(links)


unique_links = ['http://google.pl' + link for link in links.values()][:5]

for link in unique_links:
    webbrowser.open(link)

