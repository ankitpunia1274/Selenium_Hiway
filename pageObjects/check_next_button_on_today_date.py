from pageObjects.constant import Allconstant
import datetime

import time


class Nextbutton:
    next_button_xpath = '/html/body/md-content/div/div/div[2]/button[2]'
    fetch_date_of_timesheet_by_class = 'mobile-timesheet-date'

    def __init__(self, driver):
        self.driver = driver
        self.allconstants = Allconstant

    def next_button_disabled_with_today_date(self):
        todays_date = datetime.datetime.now().strftime('%b %d')

        timesheet_date = self.driver.find_element_by_class_name(self.fetch_date_of_timesheet_by_class).text
        month_and_date = timesheet_date.split(", ")[1]
        time.sleep(3)
        if todays_date == month_and_date:
            assert self.driver.find_element_by_xpath(self.next_button_xpath).get_property(
                'disabled') is True


