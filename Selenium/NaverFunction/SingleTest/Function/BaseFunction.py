from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BaseFunction:

    def __init__(self,driver):

        self.driver = driver


    def get(self, url):
        
        self.driver.get(url)
        

    def send_keys(self, locator, value):

        self.find_element(locator).send_keys(value)


    def click(self, locator):

        try :
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementExcpetion : %s" str(locator))

        except TimeoutException:
            raise TimeoutException("TimeoutException")

        

    def find_element(self, locator):

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(locator)
            
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementExcpetion : %s" str(locator))

        except TimeoutException:
            raise TimeoutException("TimeoutException")
