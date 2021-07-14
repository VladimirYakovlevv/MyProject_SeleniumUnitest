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

    def test_01(self):
        driver = self.driver

        driver.get("https://www.clalbit.co.il")

        start = StartPage(driver)
        start.click_button_menu()
        start.click_button_car_insurance()
        start.click_button_purchase_of_insurance()
        time.sleep(2)

    def test_02(self):
        driver = self.driver

        driver.get("https://www.clalbit.co.il/car#/home")

        driver.close()
        homepage = HomePage(driver)
        homepage.click_choice_of_insurance()

        time.sleep(15)

        input_table = HomePage(driver)
        input_table.enter_first_name("ולדימיר")
        input_table.enter_second_name("יעקובלב")
        input_table.enter_phone_number("0584691401")
        input_table.enter_passport_id("317921013")
        input_table.click_start_day()
        input_table.enter_start_day("24/07/2021")
        time.sleep(15)
        checkbox = HomePage(driver)
        checkbox.click_checkbox_button()
        checkbox.click_continue_button()
        time.sleep(15)
        drop_box_button = HomePage(driver)
        drop_box_button.click_drop_box_button()
        time.sleep(5)
        table = HomePage(driver)
        table.choice_a_car("רנו")
        time.sleep(2)
        table.choice_a_car_year("2011")
        table.choice_a_car_model("רנו סניק החדשה אקספרסיון")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\boban\PycharmProjects\Selenium\project_demo\Logs'))
