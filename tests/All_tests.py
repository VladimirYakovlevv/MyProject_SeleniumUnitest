from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from project_demo.pages.DriversData import DriverData
from project_demo.pages.login import Login
from project_demo.pages.Start_Page import StartPage
from project_demo.pages.CarData import CarData
from project_demo.pages.PassedInsurance import PassedInsurance


import HtmlTestRunner


class PagesTests(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        start = StartPage(cls.driver)
        start.start()

    def test_00_star_page(self):
        self.driver.get("https://www.clalbit.co.il/")
        start = StartPage(self.driver)
        start.start()

    def test_01_wrong_type_phone(self):
        self.driver.get("https://www.clalbit.co.il/car#/home")
        data_user = Login(self.driver)

        data_user.click_choice_of_insurance()

        data_user.user_data_wr_phone()
        actual_msg = data_user.wrong_type_phone()
        expected_msg = "יש להזין מספר תקין1"
        if actual_msg == expected_msg:
            assert True
        else:
            assert False
        # self.assertEqual(actual_msg, expected_msg)

    def test_02_wrong_type_id(self):
        self.driver.get("https://www.clalbit.co.il/car#/home")
        data_user = Login(self.driver)

        data_user.click_choice_of_insurance()
        data_user.user_data_wr_id()

        actual_msg = data_user.wrong_type_id()
        expected_msg = "מספר ת.ז לא תקין12"

        self.assertEqual(actual_msg, expected_msg)

    def test_03(self):
        self.driver.get("https://www.clalbit.co.il/car#/home")
        data_user = Login(self.driver)

        time.sleep(1)

        data_user.click_choice_of_insurance()
        data_user.login_user()
        time.sleep(1)
        data_cars = CarData(self.driver)
        time.sleep(1)
        data_cars.input_car_data()
        driver_data = DriverData(self.driver)
        driver_data.all_data()
        time.sleep(1)

    def test_04(self):
        self.driver.get("https://www.clalbit.co.il/car#/home")
        data_user = Login(self.driver)

        data_user.click_choice_of_insurance()
        data_user.login_user()
        time.sleep(1)
        data_cars = CarData(self.driver)
        time.sleep(1)
        data_cars.input_car_data()
        driver_data = DriverData(self.driver)
        driver_data.all_data()
        time.sleep(1)

        passed_ins = PassedInsurance(self.driver)
        passed_ins.passed_insurance()

        passed_ins.message()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\boban\PycharmProjects\Selenium\project_demo\Logs'))
