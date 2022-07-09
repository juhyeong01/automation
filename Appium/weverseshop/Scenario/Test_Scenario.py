from selenium.webdriver.common.by import By
from Config.config import Accounts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

'''
각 테스트 케이스에서 수행되는 반복적인 작업을 기능별로 모듈화하여 코드의 효율을 높입니다

'''
#TC 1

def auth_setting_test(driver):

    
    Auth_setting = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/confirmTextView')))
    Auth_setting.click()

    Language = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView')))
    Language.click()
    
    Next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/confirmTextView')))
    Next_btn.click()

    Select_BTS = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat[1]')))
    Select_BTS.click()
    Next_btn.click()

    Select_Currency = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView')))
    Select_Currency.click()
    Next_btn.click()
   
    

#TC 2

def login_test(driver):

    My_Menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/myTextView')))
    My_Menu.click()

    Email_Continue = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/continueTextView')))
    Email_Continue.click()

    Email_Id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/emailEditText')))
    Email_Id.send_keys(Accounts['ID'])

    Next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/nextTextView')))
    Next_btn.click()
    
    Email_Pw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/passwordEditText')))
    Email_Pw.send_keys(Accounts['PW'])

    Next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/nextTextView')))
    Next_btn.click()
    

#TC 3

def cart_test(driver):
    
    TinyTan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.LinearLayout[@content-desc="TinyTAN"]/android.widget.TextView')))
    TinyTan.click()
    
    driver.swipe(100, 700, 100 , 100, 1000)
    sleep(2)

    Figure_Butter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.ImageView')))
    Figure_Butter.click()

    Product_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]')))                                                      
    Product_name = Product_name.text

    Buy = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/footerRightTextView')))
    Buy.click()
    
    Select_member = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.cardview.widget.CardView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')))
    Select_member.click()

    Member_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]')))
    Member_name = Member_name.text

    Count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]')))
    Count = Count.text

    Add_Cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/addToCartButton')))
    Add_Cart.click()
    
    Cart_Popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'co.benx.weply:id/gotoCartTextView')))
    Cart_Popup.click()

    return Product_name, Member_name, Count


def move_shop(driver):
    
    Shop = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView[1]')))
    Shop.click()
    

def move_my(driver):
    My_Menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.TextView[3]')))
    My_Menu.click()