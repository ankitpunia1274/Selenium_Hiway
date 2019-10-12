class Timesheetname:
    timesheet_name_xpath="//md-content//div['@class=ng-binding']/h2"
    profile_name_xpath="//div['@class=flex-xs-20']/md-menu/button/span"

    def __init__(self,driver):
        self.driver=driver

    def timesheet_name(self):
        content_of_timesheeet=self.driver.find_element_by_xpath(self.timesheet_name_xpath).text
        only_name=content_of_timesheeet[15:]

        content_of_profile_name=self.driver.find_element_by_xpath(self.profile_name_xpath).text
        index_in_mail=content_of_profile_name.index('@')
        replace_index=content_of_profile_name("."," ")
        only_profile_username=replace_index[:index_in_mail].lower()

    ''''
    var = driver.find_element_by_xpath("//md-content//div['@class=ng-binding']/h2").text  ##profile user name
         zz = var[15:]
         var = driver.find_element_by_xpath("//div['@class=flex-xs-20']/md-menu/button/span").text  ##profile name
         x = var.index("@")
         y = var.replace(".", " ")
         z = y[:x].lower()

         assert zz == z '''