from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
base_url = os.getenv("BASE_URL")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, path=""):
        return self.driver.get(f"{self.base_url}{path}")

    def read_element(self, element):
        return element.text

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()
