from selenium import webdriver
import time
import unittest
from project_demo.pages.start_page import StartPage
from project_demo.pages.HomePage import HomePage
import HtmlTestRunner

class StartPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\boban\PycharmProjects\Selenium\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_main_menu(self):
        driver = self.driver

        driver.get("https://www.clalbit.co.il")

        start = StartPage(driver)
        start.click_button_menu()
        start.click_button_car_insurance()
        start.click_button_purchase_of_insurance()

        homepage = HomePage(driver)
        homepage.click_choice_of_insurance()

        # self.driver.find_element_by_id("MenuWithLinksList0").click()
        # self.driver.find_element_by_id("MenuHeaderItemListInWrap0_1_1").click()
        # self.driver.find_element_by_id("linkText").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\boban\PycharmProjects\Selenium\project_demo\Logs'))