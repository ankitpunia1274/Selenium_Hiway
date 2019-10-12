from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pageObjects.constant import Allconstant


class Googleacc:

    def __init__(self, driver):
        self.driver = driver
        self.allconstants = Allconstant()

    def set_username_enter(self, username):

        self.driver.find_element_by_id(self.allconstants.google_acc_locators.get('username_id')).send_keys(username)
        self.driver.find_element_by_id(self.allconstants.google_acc_locators['username_next_button_id']).click()

    def set_password(self, password):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, self.allconstants.google_acc_locators['password_byname'])))
        self.driver.find_element_by_name(self.allconstants.google_acc_locators['password_byname']).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.allconstants.google_acc_locators['password_next_button_id'])))
        self.driver.find_element_by_id(self.allconstants.google_acc_locators['password_next_button_id']).click()
