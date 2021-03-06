import datetime

from selenium import webdriver


class Airport:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        self.url = None
        self.browser = webdriver.Chrome(options=chrome_options
        )
        self.tags = ['tr', 'td']
        self.head = []

    @property
    def get_data(self):
        self.browser.get(self.url)
        elements = self.browser.find_elements_by_tag_name(self.tags[0])
        for element in elements:
            element = element.find_elements_by_tag_name(self.tags[1])
            element = map(lambda x: x.text, element)
            element = [x for x in element if x]
            yield dict(zip(self.head, element))

    @property
    def save_to_txt(self):
        with open(
            f'{self._class_name()}-{datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")}.', 'w'
        ) as file:
            for data in self.get_data:
                if not data:
                    file.write(f'{data}\n')
    @classmethod
    def _class_name(cls):
        return cls.__class__.__name__


class Chopina(Airport):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.lotnisko-chopina.pl/pl/przyloty.html'
        self.head = ['flightboard', 'time', 'direction', 'flight', 'terminal', 'belt', 'status']


class Mazury(Airport):
    def __init__(self):
        super().__init__()
        self.url = 'http://mazuryairport.pl/odloty_5.html'
        self.head = ['godz', 'data', 'rejs', 'kierunek', 'linia', 'status']


class Krakow(Airport):
    def __init__(self):
        super().__init__()
        self.url = (
            'http://www.krakowairport.pl/pl/pasazer,c70/informacje-o-lotach,c71/przyloty,a178.html'
        )
        self.head = ['godz', 'data', 'rejs', 'kierunek', 'linia']
