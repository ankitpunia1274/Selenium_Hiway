from selenium import webdriver
from pageObjects.constant import Allconstant


class Driver:
    # def __init__(self):
    #   self.driver = webdriver.Chrome('/home/ankit/Desktop/Selenium-Automation/web drivers/chromedriver')

    def executable_driver(self, browser_name):

        if browser_name == 'Chrome':

            driver = webdriver.Chrome('/home/ankit/Desktop/Selenium-Automation/web drivers/chromedriver')

        elif browser_name == 'Firefox':
            driver = webdriver.Firefox(
                executable_path='/home/ankit/Desktop/Selenium-Automation/web drivers/geckodriver')
        # driver = webdriver.Chrome('/home/ankit/Desktop/Selenium-Automation/web drivers/chromedriver')
        return driver