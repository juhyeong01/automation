<h1>Browser</h1>

<h2>Get title</h2>
driver.title

<h2>Get current URL</h2>
driver.current_url

<h1>Browser Navigation</h1>

<h2>Navigate to</h2>
driver.get("https://selenium.dev")

<h2>Back</h2>
driver.back()

<h2>Forward</h2>
driver.forward()

<h2>Refresh</h2>
driver.refresh()


<h1>Alerts</h1>

<h2>Alerts</h2>
#Click the link to activate the alert<br>
driver.find_element(By.LINK_TEXT, "See an example alert").click()


#Wait for the alert to be displayed and store it in a variable<br>
alert = wait.until(expected_conditions.alert_is_present())


#Store the alert text in a variable<br>
text = alert.text


#Press the OK button<br>
alert.accept()

<h2>Confirm</h2>
#Click the link to activate the alert<br>
driver.find_element(By.LINK_TEXT, "See an example alert").click()


#Wait for the alert to be displayed and store it in a variable<br>
alert = wait.until(expected_conditions.alert_is_present())


#Store the alert in a variable for reuse<br>
alert = driver.swith_to.alert


#Store the alert text in a variable<br>
text = alert.text


#Press the Cancel button<br>
alert.dismiss()

<h2>Prompt</h2>
#Click the link to activate the alert<br>
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()


#Wait for the alert to be displayed<br>
wait.until(expected_conditions.alert_is_present())


#Store the alert in a variable for reuse<br>
alert = Alert(driver)


#Type your message<br>
alert.send_keys("Selenium")


#Press the OK button<br>
alert.accept()

<h1>Cookies</h1>

<h2>Add cookies</h2>

from selenium import webdriver<br>
driver = webdriver.Chrome()<br>
driver.get("http://www.example.com")


#Add the cookie into current browser context<br>
driver.add_cookie({"name" : "key", "value" : "value"})

<h2>Get Named Cookie</h2>
driver = webdriver.Chrome()<br>
driver.get("http://www.example.com")


#Add the cookie into current browser context<br>
driver.add_cookie({"name" : "foo", "value" : "bar"})


#Get cookie details with named cookie 'foo'<br>
print(driver.get_cookie('foo'))


<h2>Get All Cookies</h2>
from selenium import webdriver<br>
driver = webdriver.Chrome()


#Navigate to url<br>
driver.get("http://www.example.com")


driver.add_cookie({"name" : "test1" , "value" : "cookie1"})<br>
driver.add_cookie({"name" : "test2" , "value" : "cookie2"})


#Get all available cookies<br>
print(driver.get_cookies(())

