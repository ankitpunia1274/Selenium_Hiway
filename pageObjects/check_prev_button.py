from datetime import date, timedelta
from pageObjects.constant import Allconstant

class CheckPrevbutton:
    prev_button_xpath = '/html/body/md-content/div/div/div[2]/button[1]'

    def __init__(self, driver):
        self.driver = driver
        self.allconstants=Allconstant()

    def timesheet_prev_button_and_date(self):
        self.driver.find_element_by_xpath(self.prev_button_xpath).click()
        timesheet_date = self.driver.find_element_by_class_name(self.allconstants.fetch_date_of_timesheet_by_class).text
        timesheet_month_date = timesheet_date.split(", ")[1]
        return timesheet_month_date

    def prev_date_from_today(self):
        prev_date = date.today() - timedelta(days=1)
        prev_date = prev_date.strftime('%b %d')
        return prev_date
