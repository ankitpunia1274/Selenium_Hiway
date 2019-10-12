from pageObjects.constant import Allconstant
class Welcomepage:
    #login_button_link_text = 'LOGIN USING GOOGLE'

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_button(self):
        allconstants=Allconstant()
        self.driver.find_element_by_link_text(allconstants.login_button_link_text).click()