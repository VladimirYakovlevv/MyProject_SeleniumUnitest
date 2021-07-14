from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.choice_of_insurance_css_selector = "legend[class='accessabilityHidden']"
        self.first_name_id = "FirstName"
        self.second_name_id = "LastName"
        self.phone_number_id = "Phone"
        self.passport_id = "Identity"
        self.start_date_insurance_xpath = "//*[@id='StartDateId']"
        self.checkbox_button_css_selector = 'label[role="checkbox"]'
        self.continue_button_xpath = '//*[@id="carToGoStep2"]/div[2]/div[3]/div/div/div/button/div[1]'
        self.drop_box_button_css_selector = "div[class='mileage-discount-mssg wrap-field ng-scope']"
        self.name_car_id = "ManufactureDdlIdObj"
        self.year_car_id = "yearName"
        self.model_car_id = "DegemName"

    def click_choice_of_insurance(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_css_selector(self.choice_of_insurance_css_selector).click()

    def enter_first_name(self, first_user_name):
        self.driver.find_element_by_id(self.first_name_id).clear()
        self.driver.find_element_by_id(self.first_name_id).send_keys(first_user_name)

    def enter_second_name(self, second_user_name):
        self.driver.find_element_by_id(self.second_name_id).clear()
        self.driver.find_element_by_id(self.second_name_id).send_keys(second_user_name)

    def enter_phone_number(self, phone_number):
        self.driver.find_element_by_id(self.phone_number_id).clear()
        self.driver.find_element_by_id(self.phone_number_id).send_keys(phone_number)

    def enter_passport_id(self, passport_id):
        self.driver.find_element_by_id(self.passport_id).clear()
        self.driver.find_element_by_id(self.passport_id).send_keys(passport_id)

    def click_start_day(self):
        self.driver.find_element_by_xpath(self.start_date_insurance_xpath).click()

    def enter_start_day(self, start_day):
        self.driver.find_element_by_xpath(self.start_date_insurance_xpath).clear()
        self.driver.find_element_by_xpath(self.start_date_insurance_xpath).send_keys(start_day)
        self.driver.find_element_by_xpath(self.start_date_insurance_xpath).send_keys(Keys.ENTER)

    def click_checkbox_button(self):
        self.driver.find_element_by_css_selector(self.checkbox_button_css_selector).click()

    def click_continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button_xpath).click()

    def click_drop_box_button(self):
        self.driver.find_element_by_css_selector(self.drop_box_button_css_selector).click()

    def choice_a_car(self, text):
        name_car = Select(self.driver.find_element_by_id(self.name_car_id))
        name_car.select_by_visible_text(text)

    def choice_a_car_year(self, text):
        year_car = Select(self.driver.find_element_by_id(self.year_car_id))
        year_car.select_by_visible_text(text)

    def choice_a_car_model(self, text):
        model_car = Select(self.driver.find_element_by_id(self.model_car_id))
        model_car.select_by_visible_text(text)