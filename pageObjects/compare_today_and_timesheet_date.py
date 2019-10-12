from pageObjects.constant import Allconstant
import datetime


class Comparedates:

    def __init__(self, driver):
        self.driver = driver
        self.allconstants = Allconstant()

    def today_date_and_timesheet_date(self):
        fulldate = self.driver.find_element_by_class_name(self.allconstants.fetch_date_of_timesheet_by_class).text

        full_time_date = fulldate.split(", ")
        month_and_date = full_time_date[1]
        return month_and_date

    def today_date(self):
        today_date = datetime.datetime.now().strftime('%b %d')
        return today_date

