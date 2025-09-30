import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

MAX_WAIT = 5


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):

        try:
            self.browser = webdriver.Firefox()
        except Exception as e:
            # Next 2 lines are needed to specify the path to your geckodriver
            geckodriver_path = "/snap/bin/geckodriver"
            driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

            self.browser = webdriver.Firefox(service=driver_service)

        if test_server := os.environ.get("TEST_SERVER"):
            self.live_server_url = f"http://{test_server}"

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)
    
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)

