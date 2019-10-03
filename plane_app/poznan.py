from selenium import webdriver

import datetime 

from airports import urls as url
from airports import tags as tag
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
    def get_data_poznan(self):
        self.browser.get(self.url)
        elements = self.browser.find_elements_by_class_name('tableData')
        for element in elements:
            element = element.find_elements_by_tag_name('li')
            element = map(lambda x: x.get_attribute('innerHTML'), element)
            element = [x for x in element if x]
            element = [x[:-6] for x in element if x]
            yield dict(zip(self.head, element))   
        self.browser.close() 
            
    def make_dict_poznan(self):
        data_set = []
        for x in self.get_data_poznan:
            data_set.append(x)
        return data_set[1:]

    @property
    def save_to_txt_poznan(self):
        with open(f'{self._class_name()}-{datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")}.','w') as file:
            # self.get_data changed to self.make_dict
            for data in self.make_dict_poznan():
                if data != {}:
                    file.write(f'{data}\n')
 
    def _class_name(self):
        return self.__class__.__name__

class Poznan(Airport):
    
    def __init__(self):
        super().__init__()
        self.url = url.get(self._class_name())  
        self.head = head.get(self._class_name())

if __name__ == '__main__':
    Poznan().save_to_txt_poznan
