from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)
driver.get('url')
driver.maximize_window()


#TC1

driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[1]/label/input').send_keys('ID')
driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[2]/label/input').send_keys('pw')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="layoutAuthentication_content"]/main/div/div/div/div[1]/div/form/div[4]/button').click()




# TC2
#driver.find_element(By.XPATH, '//*[@id="drawerToggle"]').click()
driver.find_element(By.XPATH, '//*[@id="drawerAccordion"]/div/div/a[6]').click()
driver.find_element(By.XPATH, '//*[@id="collapseLayouts"]/nav/a[4]').click()


#TC 3
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/header/div/div/div[2]/form').click()

driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').send_keys('Ju Hyeong')
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[2]/div/input').send_keys('Kim')
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[3]/div/input').send_keys('kjhkjh75@naver.com')
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[4]/div/input').send_keys('20020602')
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[5]/div/input').send_keys('01045977210')

driver.implicitly_wait(10)


Country = Select(driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[6]/div/select'))
Country.select_by_visible_text('South Korea')



driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[8]/div/input').send_keys('Suwon')
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[9]/div/input').send_keys('Busan')


driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[4]/button').click()



#TC 4

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/span/a[1]').click()



driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').clear()
driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[1]/div/input').send_keys('David')

Country = Select(driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[3]/div[6]/div/select'))
Country.select_by_visible_text('United States')


driver.find_element(By.XPATH, '//*[@id="layoutDrawer_content"]/main/div/form/div/div[1]/div/div/div[4]/button').click()


#TC 5

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/span/a[2]').click() # 삭제 버튼

delete = Alert(driver)
delete.accept()



os.system("pause")