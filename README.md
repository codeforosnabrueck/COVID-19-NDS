# COVID-19-NDS
Datensammlung zu Covid-19-Fällen in Niedersachsen auf kommunaler Ebene (English description see below)

Weil die Daten der niedersächsischen Ministerien und Landesbehörden teilweise sehr stark von den Zahlen abweichen, die die Kommunen (also die Städte und Landkreise) veröffentlichen, wollen wir hier als ehrenamtliches Projekt die aktuellen kommunalen Daten sammeln.

Die Struktur dieses Repos ist angelehnt an das Projekt der Johns Hopkins University: https://github.com/CSSEGISandData/COVID-19:

```
├── daily_reports
│   └── MM-DD-YYYY.csv
├── README.md
└── time_series
    ├── time_series_covid-19_nds_confirmed.csv
    └── time_series_covid-19_nds_template.csv
```

## Datensatz

### Benennung der Dateien
* Ordner **daily_reports**: MM-DD-YYYY.csv in UTC

### Datenfelder

* Kommune: Angabe des Landkreises bzw. der Stadt, aus der die Daten kommen, Quellenangabe siehe Liste unten
* Zeitangaben sind im 24-Stunden-Format UTC (Deutsche Zeit ist UTC+1)

## Datenquellen
* Ammerland: https://www.ammerland.de/Aktuelles/Topthemen/Coronavirus/, https://www.ammerland.de/Aktuelles/Presse-%C3%96ffentlichkeit/Pressemitteilungen
* Aurich: https://www.landkreis-aurich.de/aktuelles.html
* Braunschweig (Stadt): https://www.braunschweig.de/politik_verwaltung/nachrichten/corona.php
* Celle: https://www.landkreis-celle.de/informationen-und-oeffentlichkeitsarbeit/der-landkreis-informiert.html
* Cloppenburg: https://lkclp.de/aktuelles-presse/pressemitteilungen.php
* Cuxhaven: https://www.landkreis-cuxhaven.de/Corona
* Delmenhorst (Stadt): https://www.delmenhorst.de/aktuelles/pressemitteilungen-2020/index.php
* Diepholz: https://www.diepholz.de/portal/meldungen/uebersicht-0-21750.html?titel=Aktuelle+Meldungen
* Emden (Stadt): https://www.emden.de/
* Emsland: https://www.emsland.de/buerger-behoerde/aktuell/coronavirus/das-coronavirus.html
* Friesland: https://www.friesland.de/portal/meldungen/uebersicht-0-20800.html?titel=Aktuelle+Meldungen
* Gifhorn: https://www.gifhorn.de/der-landkreis/presseportal/presseinformationen/
* Goslar: https://www.landkreis-goslar.de/index.phtml?object=tx,1749.10&ModID=7&FID=94.13479.1&mNavID=1749.9&sNavID=94.35
* Göttingen: https://www.landkreisgoettingen.de/aktuelles/pressestelle/aktuelle-meldungen.html
* Grafschaft Bentheim: https://www.grafschaft-bentheim.de/
* Hameln-Pyrmont: https://www.hameln-pyrmont.de/Schnellnavigation/Startseite/Coronavirus-Sars-CoV-2-.php?object=tx,2561.5&ModID=7&FID=2749.5558.1&NavID=2561.7
* Hannover (Region): https://www.hannover.de/Leben-in-der-Region-Hannover/Verwaltungen-Kommunen/Die-Verwaltung-der-Region-Hannover/Region-Hannover
* Harburg: https://www.landkreis-harburg.de/portal/meldungen/uebersicht-0-20100.html?top=1
* Helmstedt: https://www.helmstedt.de/magazin/iarchiv.php?menuid=625&topmenu=625
* Hildesheim: https://landkreishildesheim.de/Politik-Verwaltung/Verwaltung/Presse/Pressemitteilungen
* Holzminden: https://www.landkreis-holzminden.de/portal/meldungen/uebersicht-0-25600.html?titel=Aktuelle+Meldungen
* Leer: http://www.presse-service.de/meldungen.aspx?ps_id=405&typ=0
* Lüchow-Dannenberg: https://www.luechow-dannenberg.de/home/aktuelles/pressemitteilungen.aspx
* Lüneburg: https://www.landkreis-lueneburg.de/Home-Landkreis-Lueneburg/Politik-und-Verwaltung/Aktuelles-Landkreis/Pressemitteilungen.aspx
* Nienburg/Weser: https://www.lk-nienburg.de/buergerservice/aktuelles/
* Northeim: https://www.landkreis-northeim.de/unser-landkreis/landkreis-northeim/aktuelles/
* Oldenburg (Stadt): https://www.oldenburg.de/pressemitteilungen.html
* Stadt und Landkreis Osnabrück: https://www.osnabrueck.de/coronavirus/
* Osterholz: https://www.landkreis-osterholz.de/portal/meldungen/jahresansicht.html
* Peine: https://www.landkreis-peine.de/Aktuelles-B%C3%BCrgerservice/Archiv-Pressemitteilungen
* Rotenburg (Wümme): https://www.lk-row.de/portal/seiten/coronavirus-sars-cov-2--900000145-23700.html?rubrik=1007, https://www.lk-row.de/portal/pressemitteilungen/uebersicht-0-23700.html?titel=Meldungen
* Salzgitter (Stadt): https://www.salzgitter.de/rathaus/news/presse-nachrichten.php
* Schaumburg: https://www.schaumburg.de/Aktuelles/Coronavirus
* Stade: https://www.landkreis-stade.de/portal/meldungen/coronavirus-aktuelle-lage-informationen-und-hinweise-des-gesundheitsamtes-landkreis-stade-901004416-20350.html?rubrik=901000006
* Uelzen: https://www.landkreis-uelzen.de/home/soziales-familie-und-gesundheit/gesundheit/corona-virus.aspx
* Vechta: https://www.landkreis-vechta.de/nc/service/aktuelles/veroeffentlichungen/einzelansicht/news/die-wichtigsten-infos-zum-neuartigen-coronavirus-stand-14-maerz-2020.html
* Verden: https://www.landkreis-verden.de/portal/meldungen/uebersicht-0-20600.html
* Wesermarsch: http://www.landkreis-wesermarsch.de/verwaltung-politik/pressemitteilungen.php
* Wilhelmshaven (Stadt): https://www.wilhelmshaven.de/Aktuelles/
* Wittmund: https://www.landkreis-wittmund.de/LebenArbeiten/Gesundheit/Infektionsschutz/Coronavirus.aspx
* Wolfenbüttel: https://www.lk-wolfenbuettel.de/Aktuelles/Presse/Informationen-des-Gesundheitsamtes-zum-Corona-Virus.php?object=tx,3282.5.1&ModID=7&FID=3282.10903.1&NavID=175.225&La=1&kat=175.7%2C2697.106
* Wolfsburg (Stadt): https://www.wolfsburg.de/newsroom/2020/02/26/13/41/coronavirus

## Kontakt
* osnabrueck@codefor.de

---

## English description

Because the data of the Lower Saxony ministries and state authorities sometimes differ considerably from the figures published by the municipalities (i.e. the cities and districts), we want to collect the current municipal data here as a voluntary project.

The structure of this repo is based on the project of Johns Hopkins University: https://github.com/CSSEGISandData/COVID-19. 
