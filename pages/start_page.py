class StartPage:

    def __init__(self, driver):
        self.driver = driver
        self.menu_button_insurance_id = "MenuWithLinksList0"
        self.car_insurance_button_id = "MenuHeaderItemListInWrap0_1_1"
        self.purchase_of_insurance_button_id = "linkText"

    def click_button_menu(self):
        self.driver.find_element_by_id(self.menu_button_insurance_id).click()

    def click_button_car_insurance(self):
        self.driver.find_element_by_id(self.car_insurance_button_id).click()

    def click_button_purchase_of_insurance(self):
        self.driver.find_element_by_id(self.purchase_of_insurance_button_id).click()

