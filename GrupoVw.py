from Setup import Setup
from selenium.webdriver.common.keys import Keys
from time import sleep


class GrupoVw:
    __slots__ = 'robot'
    
    def __init__(self):
        self.robot = Setup()
    
    def start(self):
        self.robot.open_brownser()
    
    def select_url(self, url):
        self.robot.brownser.get(url)
        
    def changue_to_frames(self):
        iframe = self.robot.brownser.find_element_by_xpath('/html/frameset/frame[1]')
        self.robot.brownser.switch_to.frame(iframe)
        
        iframe_2 = self.robot.brownser.find_element_by_xpath('//*[@id="divframe"]')
        self.robot.brownser.switch_to.frame(iframe_2)
        
        iframe_3 = self.robot.brownser.find_element_by_xpath('//*[@id="main"]')
        self.robot.brownser.switch_to.frame(iframe_3)
        
        iframe_4 = self.robot.brownser.find_element_by_xpath('//*[@id="mainApp"]')
        self.robot.brownser.switch_to.frame(iframe_4)
        
    def changue_frame_menu(self):
        self.changue_to_frames()    
        iframe_5 = self.robot.brownser.find_element_by_xpath('//*[@id="HeaderMenu"]')
        self.robot.brownser.switch_to.frame(iframe_5)       
        
    
    def login(self, user, robot):    
        self.robot.brownser.find_element_by_xpath('//*[@id="txtCPFCNPJ"]').send_keys(user)
        sleep(1)
        self.robot.brownser.find_element_by_xpath('//*[@id="txtSenha"]').send_keys(robot)
        
        return self.robot.brownser.find_element_by_xpath('//*[@id="btnLogin"]').click()
    
    def exit_alert(self):
        alert = self.robot.brownser.switch_to.alert
        sleep(2)
        return alert.accept()
    
    def changue_to_frame_app(self):
        self.robot.brownser.switch_to.default_content()
        self.changue_to_frames()
        iframe = self.robot.brownser.find_element_by_xpath('//*[@id="App"]')
        self.robot.brownser.switch_to.frame(iframe)
              
    def goto_volkswagen_brasil(self):
        return self.robot.brownser.find_element_by_xpath('*//a[@href="http://www.volkswagen.com.br"]').click()
        
    
    
grupo = GrupoVw()
grupo.start()
grupo.select_url('https://www.portalredevw.com.br/')
grupo.changue_frame_menu()
grupo.login('test', '1234')
grupo.exit_alert()
grupo.changue_to_frame_app()
grupo.goto_volkswagen_brasil()