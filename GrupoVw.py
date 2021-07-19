from Setup import Setup
from selenium.webdriver.common.keys import Keys
from time import sleep


class GrupoVw:
    __slots__ = 'robot'
    
    text_list = []
    
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
        self.robot.brownser.window_handles[0]
        self.robot.brownser.find_element_by_xpath('*//a[@href="http://www.volkswagen.com.br"]').click()
        window_after = self.robot.brownser.window_handles[1]
        self.robot.brownser.switch_to.window(window_after)
        
    def extract_text_save_txt(self):
        url = r'www.volkswagen.com.br'
        text = self.robot.brownser.find_element_by_tag_name('body').text
        # print(text)
        arquivo = open('texto_{0}.txt'.format(url), 'w')
        arquivo.write(text)
    
    def save_webpage_pdf(self):
        return self.robot.brownser.execute_script('window.print();')    
    
    def filter_links(self):
        xpath = '*//a'
        for xpath in self.robot.brownser.find_elements_by_xpath(xpath):
            lista = []
            attribute = xpath.get_attribute('href')
            
            if "https://www.vw.com.br/" not in attribute:
                lista.append(attribute)
                print(lista)
            else:
                continue           
                         
  
grupo = GrupoVw()
grupo.start()
grupo.select_url('https://www.portalredevw.com.br/')
grupo.changue_frame_menu()
grupo.login('test', '1234')
grupo.exit_alert()
grupo.changue_to_frame_app()
grupo.goto_volkswagen_brasil()
grupo.extract_text_save_txt()
grupo.save_webpage_pdf()
grupo.filter_links()