from Function.BaseFunction import BaseFunction
from selenium.webdriver.common.by import By
from Config.Accounts import Accounts



class Login(BaseFunction):

    input_id = (By.ID, "id_line")
    input_pw = (By.ID, "pw_line")

    btn_login = (By.ID, "log.login")

    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"


    def __init__(self, driver):

        super(Login, self).__init__(driver)

    
    def get_login_page(self):

        self.get(self.url)

    
    def send_keys_id(self):

        self.send_keys(self.input_id, Accounts["id"])

    def send_keys_pw(self):

        self.send_keys(self.input_pw, Accounts["pw"])
