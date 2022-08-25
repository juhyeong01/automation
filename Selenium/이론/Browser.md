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

<br><br><br>
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
    wait.until(EC.title_is("SeleniumHQ Browser Automation")</code>
 </pre>
    
    
    
    
 <h2>Create new window or new tab and switch</h2>
 #opens a new tab and switches to new tab<br>
 driver.switch_to.new_window('tab')<br><br>
 
 #opens a new windown and switches to new window<br>
 driver.switch_to.new_window('window')<br><br>
 
 <h2>Closing a window or tab</h2>
 #Close the tab or window<br>
 driver.close()<br><br>
 
 #Switch back to the old tab or window<br>
 driver.switch_to.window(original_window)<br><br>
 
 <h2>Quitting the browser at the end of a session</h2>
 driver.quit()<br><br>
 
 
 
 <h1>Window management</h1>
 
 <h2>Get windown size</h2>
 #Access each dimension individually<br>
 width = driver.get_window_size().get("width")<br>
 height = driver.get_window_size().get("height")<br><br>
 
 #Or store the dimensions and query them later<br>
 size = driver.get_window_size()<br>
 width1 = size.get("width")<br>
 height1 = size.get("height")<br><br>
 
 <h2>Set window size</h2>
 
 driver.set_window_size(1024, 768)<br><br>
 
 <h2>Get window position</h2>
 
 #Access each dimension individually<br>
 x = driver.get_window_position().get('x')<br>
 y = driver.get_window_position().get('y')<br><br>
 
 #Or store the dimenstions and query them later<br>
 position = driver.get_window_position()<br>
 x1 = position.get('x')<br>
 y1 = position.get('y')<br><br>
 
 <h1>Set window size</h1>
 #Move the window to the top left of the primary window.<br>
 driver.set_window_position(0,0)<br><br>
 
 <h2>Maximize window</h2>
 driver.maximize_window()<br><br>
 
 <h2>Minimize window</h2>
 driver.minimize_window()<br><br>
 
 <h2>Fullscreen window(F11)</h2>
 drvier.fullscreen_window()<br><br>
 
 <h2>Takescreenshot</h2>
 
 <pre><code>
 from selenium import webdriver
 
 driver = webdriver.Chrome()
 
 driver.get("htttp://example.com")
 
 #Returns and base64 encoded string into image.
 driver.save_screenshot('./image.png')
 
 driver.quit()</code>
 </pre>
 
 
 
