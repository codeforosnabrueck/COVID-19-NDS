from datetime import datetime
import requests
import json
import pandas as pd

api_uri = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=death_rate,cases,deaths,cases_per_100k,cases_per_population,BL,BL_ID,county&returnGeometry=false&outSR=4326&f=json'
response = requests.get(api_uri)
if response.status_code != 200:
    print('Something went wrong')
    raise Exception('GET {}'.format(response.status_code))

datastore = response.json()
keys = ['BL', 'county', 'cases', 'deaths']
data = []
for row in datastore['features']:
    d = row['attributes']
    data.append([d.get(key) for key in keys])
df = pd.DataFrame(data, columns=['Bundesland', 'Kreis/Stadt', 'Fälle', 'Tote'])
df = df[df.Bundesland == 'Niedersachsen']
today = datetime.now().strftime('%m-%d-%Y')
filename = '../daily_reports/' + today + '.csv'
df.to_csv(filename, index=False)
