from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class AllData:

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
        self.invalid_passport_id_xpath = "//ng-message[@id='idErrorMsg']"
        self.vehicle_type_button_css_selector = "body.ng-scope.MainClaims.ToGoApp.useragent-safari:nth-child(2) div.container-fluid.BodyContent:nth-child(3) div.Content.row:nth-child(7) div.Section.row:nth-child(3) div.fullWidthPage:nth-child(2) div.ng-scope:nth-child(1) div.main-div.car-to-go.ng-scope span.ng-scope div.animated.fadeInUpBig.carToGoStep3.ng-isolate-scope div.BannerWrap.BannerWrapRight.ng-dirty.ng-valid-parse.ng-valid-invalid-first-time-on-road-date.ng-valid.ng-valid-required div.BannerContent.locateBanner.L_10_B_ASR_L12.ng-scope:nth-child(1) fieldset.buttonGroupField:nth-child(6) div.carType button-group.ng-untouched.ng-isolate-scope.ng-dirty.ng-valid-parse.ng-valid.ng-valid-required div.button-group-wrap:nth-child(2) > button.group-btn.btn-secondary.group-btn-active.btn-secondary-selected:nth-child(1)"
        self.text_cars_type_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[3]"
        self.prati_xpath = "//button[contains(text(),'פרטי')]"
        self.mshari_xpath = "//button[contains(text(),'מסחרי')]"
        self.aski_xpath = "//button[contains(text(),'עיסקי')]"
        self.yes_xpath = "//button[contains(text(),'כן')]"
        self.no_xpath = "//button[contains(text(),'לא')]"
        self.months_track_xpath = "//select[@id='FirstTimeOnRoadMonth']"
        self.PreventAccidentSystem_xpath = "//span[contains(text(),'קיימת מערכת למניעת תאונות דרכים')]"
        self.text_purpouse_to_use_car_xpath = "/html[1]/body[1]/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[4]/div[2]/button-group[1]/div[2]/button[1]"
        self.button_continue_det_drivers_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/div[4]/button[1]"
        self.button_single_driver_xpath = "//button[contains(text(),'נהג יחיד')]"
        self.male_sex_driver_xpath = "//button[contains(text(),'גבר')]"
        self.date_of_birth_xpath = "//input[@id='birthdateId']"
        self.year_issue_license_xpath = "//select[@id='IssuingLicenseDdl']"
        self.button_continue_towards_insurance_xpath = "//div[contains(text(),'המשך לעבר ביטוחי')]"
        self.button_makif_3years_yes_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[1]/div[2]/button-group[1]/div[2]/button[1]"
        self.button_makif_3years_no_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[1]/div[2]/button-group[1]/div[2]/button[2]"
        self.button_comprehensive_mandatory_insurance_claims_last3_years_yes_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[2]/div[2]/button-group[1]/div[2]/button[1]"
        self.button_comprehensive_mandatory_insurance_claims_last3_years_no_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[2]/div[2]/button-group[1]/div[2]/button[2]"
        self.button_comprehensive_insurance_row_past_3years_no_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[1]/div[2]/button-group[1]/div[2]/button[2]"
        self.button_comprehensive_insurance_row_past_3years_yes_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[1]/div[2]/button-group[1]/div[2]/button[1]"
        self.button_had_negatives_last3_years_yes_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[3]/div[2]/button-group[1]/div[2]/button[1]"
        self.button_had_negatives_last3_years_no_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/fieldset[1]/fieldset[3]/div[2]/button-group[1]/div[2]/button[2]"
        self.button_for_offer_xpath = "//div[contains(text(),'לקבלת הצעה')]"
        self.message_error_xpath = "//body/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/span[1]/div[1]/div[3]/div[1]/lable[2]/span[1]"

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

    def choice_months_track(self, set_months_track):
        self.driver.find_element_by_xpath(self.months_track_xpath).send_keys(set_months_track)

    def wrong_type_phone(self):
        wrt = self.driver.find_element_by_id(self.phone_number_id).text
        return wrt

    def wrong_type_id(self):
        wrt = self.driver.find_element_by_id(self.passport_id).text
        return wrt

    def click_single_driver(self):
        self.driver.find_element_by_xpath(self.button_single_driver_xpath).click()

    def click_sex_driver(self):
        self.driver.find_element_by_xpath(self.male_sex_driver_xpath).click()

    def date_of_birth(self, date_brd):
        self.driver.find_element_by_xpath(self.date_of_birth_xpath).click()
        self.driver.find_element_by_xpath(self.date_of_birth_xpath).clear()
        self.driver.find_element_by_xpath(self.date_of_birth_xpath).send_keys(date_brd)

    def year_issue_license(self, text):
        sel = Select(self.driver.find_element_by_xpath(self.year_issue_license_xpath))
        sel.select_by_visible_text(text)

    def click_continue_towards_insurance(self):
        self.driver.find_element_by_xpath(self.button_continue_towards_insurance_xpath).click()

    def click_button_comprehensive_mandatory_insurance_claims_last3_years_yes(self):
        self.driver.find_element_by_xpath(self.button_comprehensive_mandatory_insurance_claims_last3_years_yes_xpath).click()

    def click_button_comprehensive_mandatory_insurance_claims_last3_years_no(self):
        self.driver.find_element_by_xpath(self.button_comprehensive_mandatory_insurance_claims_last3_years_no_xpath).click()

    def click_button_had_negatives_last3_years_yes(self):
        self.driver.find_element_by_xpath(self.button_had_negatives_last3_years_yes_xpath).click()

    def click_button_had_negatives_last3_years_no(self):
        self.driver.find_element_by_xpath(self.button_had_negatives_last3_years_no_xpath).click()

    def click_button_for_offer(self):
        self.driver.find_element_by_xpath(self.button_for_offer_xpath).click()

    def click_button_comprehensive_insurance_row_past_3years_no(self):
        self.driver.find_element_by_xpath(self.button_comprehensive_insurance_row_past_3years_no_xpath).click()

    def click_button_comprehensive_insurance_row_past_3years_yes(self):
        self.driver.find_element_by_xpath(self.button_comprehensive_insurance_row_past_3years_yes_xpath).click()

    def message(self):
        msg = self.driver.find_element_by_xpath(self.message_error_xpath).text
        if msg == "מצטערים, לא ניתן להמשיך את תהליך הרכישה באתר, אנא פנה לסוכן הביטוח שלך":

            assert True
        else:
            assert False


















