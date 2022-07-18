from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

def get_webdriver():
    os.environ['WDM_SSL_VERIFY'] = '0'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    return driver

def wait_for_element_id(thedriver, thename):
    return WebDriverWait(thedriver, 10).until(
            EC.visibility_of_element_located((By.ID, thename))
        )