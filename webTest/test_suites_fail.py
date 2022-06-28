from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import unittest
import test_scenario




class TestCustomer(unittest.TestCase):
    
    
    
    def setUp(self):
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver_test = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = self.options)
        self.driver_test.get('url')
        self.driver_test.maximize_window()


    def tearDown(self):

        sleep(10)
        self.driver_test.quit()

    def test_1_Login(self):
        
        test_scenario.Login_admin(self.driver_test, 'id' , 'demoad')
        body_name = self.driver_test.find_element(By.TAG_NAME, 'body').get_attribute("class")
        self.assertTrue(body_name.startswith("bg"), msg = "Longin Failed")

    def test_2_Customer_page(self):
        
        test_scenario.Login_admin(self.driver_test , 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        

    def test_3_Customer_add(self):

        test_scenario.Login_admin(self.driver_test)
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_add(self.driver_test, 'Ju Hyeong', 'Kim', 'kjhkjh75@naver.com', '20220602', '01045977210', 'South Korea', 'Suwon', 'Busan')
        
        #화면 전환이 안되거나(중복 email)
        #화면 전환은 됐는데 tr 개수가 추가 안된 경우는 add실패로 고려
        #update 안하고 이전페이지 간 케이스로 assert작성

    
    def test_4_Customer_edit(self):

        test_scenario.Login_admin(self.driver_test, 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_edit(self.driver_test, 'David', 'United States')
        
        #if 문 넣어서 customer_add부터 수행해달라는 print문 작성

    def test_5_Customer_del(self):

        test_scenario.Login_admin(self.driver_test, 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_del(self.driver_test)

        #if 문 넣어서 전체 개체 수 파악한 후 변화 없었다면 마찬가지로 customer_add부터 수행해달라는 print문


if __name__ == '__main__':
    unittest.main()