from selenium.webdriver.common.by import By
import pytest
#import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'

def test_existence_of_add_to_cart_button(browser):
    browser.get(link)
    #time.sleep(20) #для наглядной проверки убрать "#" с импорта и команды
    browser.implicitly_wait(15)
    add_to_shopping_сart_button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket") #ищем кнопку
    assert add_to_shopping_сart_button, 'Add to cart button does not exist' #проверяем наличие кнопки
    


