from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pageObjects.constant import Allconstant
from pageObjects.checks_profile_and_username import Timesheetname


class Timesheetclick:
    # locators of elements in first page
    timesheet_click_xpath = "//a/span[contains(text(), 'TimeSheet')]"


    def __init__(self, driver):
        self.driver = driver
        #self.allconstants=Allconstant

    def click_on_timesheet_button(self):
        #allconstants=Allconstant
        time.sleep(3)  # it is used to give time for clicking on
                        # timesheet beacause if we dont use it gives undefined page

        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.timesheet_click_xpath))).click()
