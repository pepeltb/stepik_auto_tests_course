from selenium import webdriver
import time 
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")  
    browser.get(link)
    
    magical_journey = browser.find_element_by_css_selector('[type="submit"]').click()
    time.sleep(1)
    
    alert = browser.switch_to.alert
    alert.accept()    
    
    x = browser.find_element_by_id('input_value').text
    answer = calc(x) 
    
    filling_out = browser.find_element_by_id('answer').send_keys(answer)
    
    button = browser.find_element_by_css_selector("[type='submit']").click()
       



except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    
    time.sleep(10)
    alert_answer = browser.switch_to.alert
    alert_answer.accept()
    browser.close()
    browser.quit()