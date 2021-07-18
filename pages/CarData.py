from project_demo.pages.AllData import AllData
import time


class CarData(AllData):

    def input_car_data(self):
        self.click_checkbox_button()
        time.sleep(1)
        self.click_continue_button()
        time.sleep(1)
        self.click_drop_box_button()
        time.sleep(1)
        self.choice_a_car("רנו")
        time.sleep(1)
        self.choice_a_car_year("2011")
        time.sleep(1)
        self.choice_a_car_model("רנו סניק החדשה אקספרסיון")
        time.sleep(1)
        self.choice_months_track("8")
        time.sleep(2)
        self.prevent_accident_system()
        self.set_car_type("לא")
        time.sleep(1)
        self.set_purpose_of_using("עיסקי")
        time.sleep(1)
        self.owned_by_company("לא")
        time.sleep(1)
        self.click_button_continue_details_drivers()

    def set_car_type(self, choice):
        self.driver.find_element_by_xpath(self.text_cars_type_xpath)

        if choice == "פרטי":
            self.driver.find_element_by_xpath(self.prati_xpath).click()
        elif choice == "מסחרי":
            self.driver.find_element_by_xpath(self.mshari_xpath).click()
            """if type not מיסחרי or פרטי choice is פרטי """
        else:
            self.driver.find_element_by_xpath(self.prati_xpath).click()

    def set_purpose_of_using(self, choice):
        self.driver.find_element_by_xpath(self.text_purpouse_to_use_car_xpath)

        if choice == "פרטי":
            self.driver.find_element_by_xpath(self.prati_xpath).click()
        elif choice == "עיסקי":
            self.driver.find_element_by_xpath(self.aski_xpath).click()
            """if type not עיסקי or פרטי choice is פרטי """
        else:
            self.driver.find_element_by_xpath(self.prati_xpath).click()

    def owned_by_company(self, choice):
        self.driver.find_element_by_xpath(self.text_purpouse_to_use_car_xpath)
        if choice == "כן":
            self.driver.find_element_by_xpath(self.yes_xpath).click()
        elif choice == "לא":
            self.driver.find_element_by_xpath(self.no_xpath).click()
            """ if type not כן or לא raises an False """
        else:
            assert False

    def prevent_accident_system(self):
        self.driver.find_element_by_xpath(self.PreventAccidentSystem_xpath).click()

    def click_button_continue_details_drivers(self):
        self.driver.find_element_by_xpath(self.button_continue_det_drivers_xpath).click()


