from selenium import webdriver
from selenium.webdriver import Chrome
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Setup:
    __slots__ = 'brownser'
    
    def __init__(self):
        self.brownser = ''
    
    def open_brownser(self):
        chrome_options = webdriver.ChromeOptions()
        settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
        
        prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--kiosk-printing')
        
        self.brownser = webdriver.Chrome(chrome_options=chrome_options)
    
    def _verify_type_selector(self, selector):
        is_xpath = '/' or '//' in selector
        print(selector, ">>>", is_xpath)
        by = By.XPATH if (is_xpath) else By.CSS_SELECTOR
        return by

    def find(self, selector, by=By.CSS_SELECTOR):
        wait = WebDriverWait(self.brownser, 100)
        by = self._verify_type_selector(selector)
        return wait.until(EC.presence_of_all_elements_located((by, selector)))    
    
    def get_attribute(self, selector, attribute):
        element = self.find(selector, By.XPATH)
        return element.get_attribute(attribute)    