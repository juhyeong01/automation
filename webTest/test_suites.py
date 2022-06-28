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

        sleep(3)
        self.driver_test.quit()




    def test_1_Login(self):
        body_name = self.driver_test.find_element(By.TAG_NAME, 'body').get_attribute("class")
        print(body_name)
        test_scenario.Login_admin(self.driver_test, 'id' , 'pw')
        body_name = self.driver_test.find_element(By.TAG_NAME, 'body').get_attribute("class")
        print(body_name)
        
        #self.assertTrue(body_name.startswith("bg"), msg = "Longin Failed")
        

    def test_2_Customer_page(self):
        
        test_scenario.Login_admin(self.driver_test , 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        

    def test_3_Customer_add(self):
        
        test_scenario.Login_admin(self.driver_test, 'id', 'pw')
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_add(self.driver_test, 'Ju Hyeong', 'Kim', 'kjhkjh75@naver.com', '20220602', '01045977210', 'South Korea', 'Suwon', 'Busan')

        #assert문 추가 못한 경우 fail , 화면 전환 안됨

        
        #num_row_bf, num_row_af 값 비교 해서 다른 경우 추가된 것으로 간주 아니면 add실패

    def test_4_Customer_edit(self):

        test_scenario.Login_admin(self.driver_test, 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_edit(self.driver_test, 'David', 'United States')
        #assert문 추가 못한 경우 fail , 화면 전환 안됨

    def test_5_Customer_del(self):

        test_scenario.Login_admin(self.driver_test, 'id' , 'pw')
        test_scenario.Customer_page(self.driver_test)
        test_scenario.Customer_del(self.driver_test)

        #assert 전체 요소수 비교로 해서 삭제 안됐는지 판별 해도 될듯.
        #num_row_bf = add하기 전 개수
        #assert문 수정 못하는 경우 마찬가지, 화면 전환 안됨, assert문 하나더 추가된 고객 없으면 fail내고 종료
        #num_row_af = self.driver_test.find_element(By.XPATH,' ' ).get_attribute("rowspan")


if __name__ == '__main__':
    unittest.main()

