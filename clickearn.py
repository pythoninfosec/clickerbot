from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
import time

def bot():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
        chrome_options.add_argument('--user-agent=%s' %user_agent)
        chrome = webdriver.Chrome(chrome_options=chrome_options)

        #chrome.set_page_load_timeout(30)
        chrome.get("LINK YOUR PAGE / TIKLANACAK ADRES")
        time.sleep(5)
        

        #submit_button = chrome.find_elements_by_xpath('//*[@id="btd"]')[0]
        #submit_button.click()
        #button = chrome.find_element_by_xpath("//*[@id='skip']")
        #button.click()
        chrome.execute_script("window.stop()")
        try:  
            #button = chrome.find_element_by_xpath("//*[@id='btd']")
            #button.click()
           # try:
            
            timeout = 5
            
            #chrome.find_element_by_xpath('//*[@id="btd"]').click()
            chrome.find_element_by_xpath('//*[@id="btd"]').click()
            #element_name = EC.presence_of_element_located((By.XPATH, '//*[@id="btd"]'))
            #WebDriverWait(chrome, timeout).until(element_name).click
            
            #btn = WebDriverWait(chrome,0).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btd"]')))
            #time.sleep(1)
            #btn.click()
            time.sleep(3)
            chrome.quit()
            
           # submit_button = chrome.find_elements_by_xpath('//*[@id="btd"]')[0]
            #wait = WebDriverWait(chrome,28) 
            #submit_button.click()
        except (NoSuchElementException,TimeoutException):
            #print ("Belirtilen Surede Link Yok")
            chrome.quit()
            pass
            #   time.sleep(10)
             #finally:
            #  chrome.quit()
                
           # btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btd"]')))
            #btn.click()
                # button = chrome.find_element_by_xpath("//*[@id='btd']")[5]
            #button.click()
            #time.sleep(5)
           # chrome.quit()
        #except NotImplementedError:
           # print ( "Link Hatasi" )
           # chrome.quit()

#USER AGENT
ua = UserAgent()
a = ua.random
user_agent = ua.random


proxy_adet = sum(1 for line in open('proxy.txt'))
print ("Proxy Adeti: %s" %proxy_adet)
tikadet = input("Adet Belirtiniz: ")
tikbaslangic = 0
while tikbaslangic < tikadet:
    tikbaslangic = tikbaslangic +1
    proxy_read = open("proxy.txt").read().splitlines() 
    proxy_id =  tikbaslangic
    PROXY = proxy_read[proxy_id]
    PROXY = PROXY
    print ("**************************************************")
    print ("Tiklama Adeti: %s" %tikbaslangic)
    print (PROXY)
    print (user_agent)
    print ("**************************************************")
    bot()
