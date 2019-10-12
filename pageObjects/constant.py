class Allconstant:
    def __init__(self):
        self.link_of_website = 'https://qa.hiway.hashedin.com/'
        self.login_button_link_text = 'LOGIN USING GOOGLE'
        self.csv_path_for_successful_login = '/home/ankit/Desktop/Automation-selenium/pageObjects/csv_sheets/logindata.csv'
        self.csv_for_invalid='/home/ankit/Desktop/Automation-selenium/pageObjects/csv_sheets/invalid_csvfile.csv'

        self.google_acc_locators = {
            'username_id': 'identifierId',
            'username_next_button_id': 'identifierNext',
            'password_byname': 'password',
            'password_next_button_id': 'passwordNext'
        }
        self.username = 'ankit.poonia@hashedin.com'
        self.password = '8930014017'

        self.start_highway = 'btn'

        self.timesheet_click_xpath = "//a/span[contains(text(), 'TimeSheet')]"

        self.fetch_date_of_timesheet_by_class = "mobile-timesheet-date"
