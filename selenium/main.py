from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

options = FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()), options=options
)

driver.get("https://google.com")

title = driver.title
assert title == "Google"

driver.implicitly_wait(0.5)

search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.NAME, value="btnK")

search_box.send_keys("Selenium\n")
search_button.click()

search_box = driver.find_element(by=By.NAME, value="q")
value = search_box.get_attribute("value")
assert value == "Selenium"

driver.quit()
