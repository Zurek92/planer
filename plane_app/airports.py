urls = {
    'Chopina':'https://www.lotnisko-chopina.pl/pl/przyloty.html',
    'Mazury':'http://mazuryairport.pl/odloty_5.html',
    'Krakow':'http://www.krakowairport.pl/pl/pasazer,c70/informacje-o-lotach,c71/przyloty,a178.html',
    'Poznan':'https://www.airport-poznan.com.pl/pl/'
}

heads = {
    'Chopina':['flightboard', 'time', 'direction', 'flight','airlines','terminal', 'belt', 'status'],
    'Poznan':['GODZINA','KIERUNEK','NR REJSU','STATUS'],
}

tags = {
    'Chopina':['tr', 'td'],
    'Mazury':['tr', 'td'],
    'Krakow':['tr', 'td'],
    'Poznan':['tableData', 'li'],
}