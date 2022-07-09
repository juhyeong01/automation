import unittest
import os
from appium import webdriver


'''
모든 테스트 케이스에서 공통적으로 사용하는 setUp과 tearDown 메서드를 정의하고 각 테스트 케이스는 해당 모듈을 상속받아 수행하게됩니다
'''

class DriverSetup(unittest.TestCase):

    def setUp(self):
        
        app = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'weverseshop.apk')
        app = os.path.abspath(app)

        self.driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',
                        desired_capabilities={
                            'app' : app,
                            'platformName' : 'Android',
                            'platformVersion' : '12.0',
                            'automationName' : 'uiautomator2',
                            'appPackage' : 'co.benx.weply',
                            'appActivity' : 'co.benx.weply.screen.main.MainActivity',
                            'udid' : 'R3CR103B7AP'
                        })

            
    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



