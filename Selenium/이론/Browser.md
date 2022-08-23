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
driver.find_element(By.LINK_TEXT, "See an example alert").click()<br><br>


#Wait for the alert to be displayed and store it in a variable<br>
alert = wait.until(expected_conditions.alert_is_present())


#Store the alert text in a variable<br>
text = alert.text


#Press the OK button<br>
alert.accept()

<h2>Confirm</h2>
#Click the link to activate the alert<br>
driver.find_element(By.LINK_TEXT, "See an example alert").click()<br><br>


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
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()<br><br>

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
driver.get("http://www.example.com")<br><br>


#Add the cookie into current browser context<br>
driver.add_cookie({"name" : "foo", "value" : "bar"})


#Get cookie details with named cookie 'foo'<br>
print(driver.get_cookie('foo'))


<h2>Get All Cookies</h2>
from selenium import webdriver<br>
driver = webdriver.Chrome()<br><br>


#Navigate to url<br>
driver.get("http://www.example.com")


driver.add_cookie({"name" : "test1" , "value" : "cookie1"})<br>
driver.add_cookie({"name" : "test2" , "value" : "cookie2"})


#Get all available cookies<br>
print(driver.get_cookies(())



<h1>Frames</h1>

<div id="modal">
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div><br><br>

#This won`t work<br>
driver.find_element(By.TAG_NAME, 'button').click()<br><br>

<h2>Using a WebElement</h2>
#Store ifram web element<br>
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")<br><br>

#switch to selected frame<br>
driver.switch_to.frame(iframe)<br><br>

#Now click on button<br>
driver.find_element(By.TAG_NAME, 'button')click()<br><br>

<h2>Using a name or ID</h2>
#Swith frame by id<br>
driver.switch_to.frame("buttonframe") <br><br>

#Now Click on the button<br>
driver.find_element(By.TAG_NAME, "button").click()<br><br>

<h2>Using an index</h2>
#Switching to second iframe based on index
iframe = driver.find_element(By.TAG_NAME, "iframe")[1]<br><br>

#switch to selected iframe<br>
driver.switch_to.frame(iframe)<br><br>

<h2>Leaving a frame</h2>
switch back to default content<br>
driver.switch_to.default_content()


<h1>Window</h1>

<h2>Get window handle</h2>
driver.current_window_handle<br><br>

<h2>Switching windows or tabs</h2>
<pre><code>from selenium import webdriver<br>
from selenium.webdriver.support.ui import WebDriverWait<br>
from selenium.webdriver.support import expected_condition as EC

<br><br>
with webdriver.Chrome() as driver:

    #Open URL
    driver.get("https://seleniumhq.github.io")
    
    #Setup wait for later
    wait = WebDriverWait(driver, 10)
    
    #Store the ID of the original window
    original_window = driver.current_windown_handle
    
    #Check we don`t have other windows open already
    assert len(driver.window handles) == 1
    
    #Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()
    
    #Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))
    
    #Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
            
    #Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation")</code></pre>
