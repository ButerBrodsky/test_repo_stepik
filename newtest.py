from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(f):
    return str(math.log(abs(12*math.sin(int(f)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.implicitly_wait(15)
    browser.get(link)
    book = browser.find_element(By.ID, 'book')
    #ждем пока значение будет принимать значение такое
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
    )
    book.click()

    f = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(int(f))
    browser.find_element(By.ID, "answer").send_keys(y)
    #ждем пока кнопка станет нажимаемая
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    browser.switch_to.alert
    #скролл чтобы кнопку можно было нажать
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(3)

finally:
    browser.quit()
