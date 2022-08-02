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
#Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

#Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

#Store the alert text in a variable
text = alert.text

#Press the OK button
alert.accept()

<h2>Confirm</h2>
#Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

#Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

#Store the alert in a variable for reuse
alert = driver.swith_to.alert

#Store the alert text in a variable
text = alert.text

#Press the Cancel button
alert.dismiss()

<h2>Prompt</h2>
#Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

#Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

#Store the alert in a variable for reuse
alert = Alert(driver)

#Type your message
alert.send_keys("Selenium")

#Press the OK button
alert.accept()
