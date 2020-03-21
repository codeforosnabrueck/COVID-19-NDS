import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import dateutil.parser as dparser
from csv import writer
from csv import DictWriter

url = 'https://www.landkreisgoettingen.de/aktuelles/pressestelle/aktuelle-meldungen.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
content_wrapper = soup.find('div', {'id':'content-wrap'})
content_workspace = content_wrapper.find('div',{'class':'content-workspace'})
meldungen = content_workspace.find_all('div', {'style':'text-align:'})
data = []
key_words = ['Corona','Infiziert','positiv','getestet']
for meldung in meldungen:
    datum = meldung.find('span',{'class':'magazinedate'}).text
    titel = meldung.find('div',{'class':'magazintitle'}).text
    summary = meldung.find('p').text
    press_id = meldung.find('span',{'class':'cw-mediafile-title'}).text
    if any(x in titel for x in key_words) or any(x in press_id for x in key_words) or all(x in summary for x in key_words[:2]):
        tmp = []
        tmp.append(datum)
        info_summary = [sentence + '.' for sentence in summary.split('.') if all(x in sentence for x in key_words[:2])]
        info_titel = titel if any(x in titel for x in key_words) else None
        tmp.append(info_titel)
        tmp.append(info_summary)
        data.append(tmp)
# clean data
data = [d for d in data if (d[1] != None)]
data = pd.DataFrame(data, columns=['date', 'header', 'information'])
data.to_csv('goettingen.csv', index=False)