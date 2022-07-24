from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import os

class Driver:
    def __init__(self):
        self.driver=self.setup_webdriver()

    def setup_webdriver(self):
        os.environ['WDM_SSL_VERIFY'] = '0'
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        logging.debug("starting webdriver")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        logging.debug("got webdriver")
        return driver

    def get_webdriver(self):
        return self.driver


    def wait_for_element_id(self, thename):
        return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, thename))
        )