import sys
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

def create():
    # print(str(sys.argv[1]))
    path = os.path.join('/Users/aashi/desktop/projects', sys.argv[1])
    os.mkdir(path)

    browser = webdriver.Chrome()
    browser.get('https://github.com/login')

    python_button = browser.find_element(By.XPATH, '//*[@id="login_field"]')
    python_button.send_keys('')

    button = browser.find_element(By.XPATH, '//*[@id="password"]')
    button.send_keys('')

    Button = browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]')
    Button.click()

    browser.get('https://github.com/new')

    Button = browser.find_element(By.XPATH, '//*[@id="repository_name"]')
    Button.send_keys(sys.argv[1])

    Button = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    Button.submit()
    
if __name__ == "__main__":
    create()

