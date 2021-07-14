class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.choice_of_insurance_css_selector = "legend[class='accessabilityHidden'"

    def click_choice_of_insurance(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_css_selector(self.choice_of_insurance_css_selector).click()

