from selenium import webdriver

import datetime 

from airports import urls as url
from airports import heads as head

class Airport:
    
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
 
        self.url = None
        self.browser = webdriver.Chrome(executable_path='/home/bart/PythonProjects/flight/chrome/chromedriver',options= options)
        self.tags = []
        self.head = []
 
    @property
    def get_data_katowice(self):
        self.browser.get(self.url)
        elements = self.browser.find_elements_by_class_name('timetable__row')
        for element in elements:
            element = element.find_elements_by_class_name('timetable__col')
            element = map(lambda x: x.text, element)
            element = [x for x in element if x]
            yield dict(zip(self.head, element))  
        self.browser.close() 
            
    def make_dict_katowice(self):
        data_set = []
        for x in self.get_data_katowice:
            data_set.append(x)
        return data_set

    @property
    def save_to_txt_katowice(self):
        with open(f'{self._class_name()}-{datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")}.','w') as file:
            for data in self.make_dict_katowice():
                if data != {}:
                    file.write(f'{data}\n')
 
    def _class_name(self):
        return self.__class__.__name__

class Katowice(Airport):
    
    def __init__(self):
        super().__init__()
        self.url = 'https://www.katowice-airport.com/pl/dla-pasazera/tablica-lotow-online'  
        self.head = ['PRZYLOT','KIERUNEK','LINIA','NR LOTU','STATUS']

if __name__ == '__main__':
    Katowice().save_to_txt_katowice
