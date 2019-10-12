import time
import pytest
from pageObjects.csv_sheets.csv_getter import get_csv_data
from pageObjects.login_with_google import Welcomepage
from pageObjects.google_account_info import Googleacc
from pageObjects.driver import Driver
from pageObjects.constant import Allconstant
from pageObjects.start_using_highway import Starthiway
from pageObjects.click_on_timesheet import Timesheetclick
from pageObjects.checks_profile_and_username import Timesheetname
from pageObjects.compare_today_and_timesheet_date import Comparedates
from pageObjects.check_next_button_on_today_date import Nextbutton
from pageObjects.check_prev_button import CheckPrevbutton
import unittest


class Testtimesheet(unittest.TestCase):
    allconstants = Allconstant()

    @pytest.yield_fixture()
    def setup(self, browser_name):
        driverobject = Driver()

        self.driver = driverobject.executable_driver(browser_name)
        self.driver.implicitly_wait(15)
        self.driver.get(self.allconstants.link_of_website)
        self.driver.maximize_window()
        lp = Welcomepage(self.driver)
        lp.click_on_login_button()

        gp = Googleacc(self.driver)
        gp.set_username_enter(self.allconstants.username)
        self.driver.implicitly_wait(15)
        gp.set_password(self.allconstants.password)

        # time.sleep(10)
        start = Starthiway(self.driver)
        start.click_on_start_hiway_button()
        # time.sleep(10)

        timesheet = Timesheetclick(self.driver)
        timesheet.click_on_timesheet_button()

        yield
        self.driver.quit()

    @pytest.mark.usefixtures('setup')
    def test_match_login_username_with_timesheet_name(self):
        usernameprofile = Timesheetname(self.driver)
        usernameprofile.timesheet_name()
        assert usernameprofile.timesheet_name() == usernameprofile.profile_name()
        # assert self.only_name==self.only_profile_username

    @pytest.mark.usefixtures('setup')
    def test_today_date_and_timesheet_date_is_same(self):
        comparedates = Comparedates(self.driver)
        assert comparedates.today_date_and_timesheet_date() == comparedates.today_date()

    @pytest.mark.usefixtures('setup')
    def test_next_button_isdisable_on_today_date(self):
        nextbutton = Nextbutton(self.driver)
        nextbutton.next_button_disabled_with_today_date()

    @pytest.mark.usefixtures('setup')
    def test_prev_button_display_prev_date(self):
        prevbutton = CheckPrevbutton(self.driver)

        assert prevbutton.timesheet_prev_button_and_date() == prevbutton.prev_date_from_today()



if __name__ == '__main__':
    pytest.main()
