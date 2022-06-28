from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



# TC 1
def Login_admin(driver, email, password):
    
    
    driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[1]/label/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[2]/label/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[4]/button').click()
    


# TC 2
#driver.find_element(By.XPATH, '//*[@id="drawerToggle"]').click()
def Customer_page(driver):

    # dash board nav가 닫혀 있으면 대쉬보드 클릭,  열려 있으면 open 하는 코드 추가
    driver.find_element(By.XPATH, '//*[@id="drawerAccordion"]/div/div/a[6]').click()
    driver.find_element(By.XPATH, '//*[@id="collapseLayouts"]/nav/a[4]').click()


#TC 3
def Customer_add(driver, First_Name, Last_Name, Email, Password, Mobile, country, Address1, Address2):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/header/div/div/div[2]/form').click()

    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').send_keys(First_Name)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[2]/div/input').send_keys(Last_Name)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[3]/div/input').send_keys(Email)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[4]/div/input').send_keys(Password)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[5]/div/input').send_keys(Mobile)

    driver.implicitly_wait(10)


    Country = Select(driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[6]/div/select'))
    Country.select_by_visible_text(country)

    

    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[8]/div/input').send_keys(Address1)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[9]/div/input').send_keys(Address2)


    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[4]/button').click()



#TC 4
def Customer_edit(driver, First_Name, country):

    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/span/a[1]').click()



    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').send_keys(First_Name)

    Country = Select(driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[6]/div/select'))
    Country.select_by_visible_text(country)


    driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[4]/button').click()


#TC 5
def Customer_del(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/span/a[2]').click() # 삭제 버튼

    delete = Alert(driver)
    delete.accept()