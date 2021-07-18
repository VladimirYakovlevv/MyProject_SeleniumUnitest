import time

from project_demo.pages.AllData import AllData


class Login(AllData):

    def login_user(self):

        self.enter_first_name("סמנטה")
        self.enter_second_name("רוזה")
        self.enter_phone_number("0538308795")
        self.enter_passport_id("342654399")
        self.click_start_day()
        time.sleep(0.3)
        self.enter_start_day("24/07/2021")

    def user_data_wr_id(self):

        time.sleep(0.3)
        self.enter_first_name("סמנטה")
        self.enter_second_name("רוזה")
        time.sleep(0.3)
        self.enter_phone_number("0538308795")
        time.sleep(0.3)
        self.enter_passport_id("342654333")
        self.click_start_day()
        self.enter_start_day("24/07/2021")

    def user_data_wr_phone(self):

        time.sleep(0.3)
        self.enter_first_name("סמנטה")
        self.enter_second_name("רוזה")
        time.sleep(0.3)
        self.enter_phone_number("adsdasd")
        time.sleep(0.3)
        self.enter_passport_id("342654399")
        self.click_start_day()
        self.enter_start_day("24/07/2021")
