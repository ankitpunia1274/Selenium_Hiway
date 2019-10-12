import pytest
import unittest

from pageObjects.constant import Allconstant

from pageObjects.csv_sheets.csv_getter import get_csv_data
# from pageObjects. import OpenHighway
from pageObjects.login_with_google import Welcomepage
from pageObjects.driver import Driver
from pageObjects.google_account_info import Googleacc
from ddt import ddt, data, unpack


@ddt
class TestLogin(unittest.TestCase):
    allconstants = Allconstant()
    driver = ''

    @pytest.yield_fixture()
    def setup(self, browser_name):
        driver1 = Driver()
        self.driver = driver1.executable_driver(browser_name)
        # global driver
        self.driver.get('https://qa.hiway.hashedin.com/')
        self.driver.maximize_window()
        lp = Welcomepage(self.driver)
        lp.click_on_login_button()

        yield
        self.driver.close()

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(allconstants.csv_path_for_successful_login))
    @unpack
    def test_successful_login(self, username, password):
        login_values = Googleacc(self.driver)
        login_values.set_username_enter(username)

        login_values.set_password(password)

        ''' i tooked screenshot or correct output and my function is not proper '''
        self.driver.save_screenshot('/home/ankit/Desktop/Automation-selenium/screenshot/timesheet.png')


if __name__ == '__main__':
    pytest.main()
