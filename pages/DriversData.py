import time

from pages.AllData import AllData


class DriverData(AllData):

    def all_data(self):
        time.sleep(1)
        self.click_single_driver()
        time.sleep(1)
        self.click_sex_driver()
        """ Set date of birth DAY/MONTHS/YEARS """
        time.sleep(1)
        self.date_of_birth("02/08/1975")
        """ SET YEAR ONLY from 1947 - 2021 """
        time.sleep(1)
        self.year_issue_license("2000")
        time.sleep(1)
        self.click_continue_towards_insurance()



