from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.constant import Allconstant


class Starthiway:
    # locators of elements in first page
    #start_highway = 'btn'

    def __init__(self, driver):
        self.driver = driver

    def click_on_start_hiway_button(self):
        allconstants=Allconstant()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, allconstants.start_highway))).click()
