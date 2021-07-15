from selenium import webdriver
from selenium.webdriver import Chrome

class Setup:
    __slots__ = 'brownser'
    
    def __init__(self):
        self.brownser = ''
    
    def open_brownser(self):
        self.brownser = webdriver.Chrome()