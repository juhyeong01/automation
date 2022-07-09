from TestBase.DriverSetup import DriverSetup
from Scenario.Test_Scenario import auth_setting_test, login_test, cart_test, move_shop
from selenium.webdriver.common.by import By
from Config.config import Accounts
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

"""
해당 모듈은 각 테스트 케이스를 순차적으로 구현한 것입니다.
test_case_1은 권한 설정 및 기본 설정
test_case_2는 로그인
test_case_3은 상품의 추가 테스트 케이스 입니다.
"""

class Test_Suites(DriverSetup):

    
     # 해당 함수는 권한 설정 및 기본 설정을 자동으로 수행하며 메인 Shop화면이 정상적으로 노출되는지 테스트 하는 함수입니다.
    def test_case_1_auth(self):
        
        auth_setting_test(self.driver)

        try:
            Shop_Menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView[1]')))
            
        except:
            raise Exception("Not Shop display")

        self.assertTrue(Shop_Menu.is_selected(), "Not Shop display")


    # 해당 함수는 로그인 동작을 자동으로 수행하며 로그인시 기입 한 메일과 내 정보에서 나타는 메일의 정보가 동일한지 테스트 하는 함수입니다.
    def test_case_2_login(self):

        auth_setting_test(self.driver)

        sleep(5)

        login_test(self.driver)

        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/emailTextView')))
        email = email.text
        
        self.assertEqual(email, Accounts['ID'], "ID is not correct")

    
    # 해당 함수는 선택한 상품과 옵션 그리고 수량이 정상적으로 장바구니에 추가되는지 테스트 하는 함수입니다.
    def test_case_3_cart(self):
        
        auth_setting_test(self.driver)

        sleep(5)

        login_test(self.driver)

        sleep(5)

        move_shop(self.driver)
        
        Product, Member, Count = cart_test(self.driver)

        Cart_Product = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/nameTextView'))).text
        Cart_Member = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/optionTextView'))).text
        Cart_Member = Cart_Member.split(":")[1][1:]
        Cart_Count = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/quantityTextView'))).text
        
        self.assertEqual(Cart_Product, Product, "Wrong product added")
        self.assertEqual(Cart_Member, Member, "Wrong option added")
        self.assertEqual(Cart_Count, Count, "Wrong quantity added")

        
        

        sleep(10)
