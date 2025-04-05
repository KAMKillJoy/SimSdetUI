import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

close_browser = True  # Можно отключить автоматическое зарывание браузера для дебага.

options = Options()

if os.getenv('GITHUB_ACTIONS') == 'true':
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new")

if not close_browser:
    options.add_experimental_option("detach", True)


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    yield driver
    if close_browser:
        driver.quit()
