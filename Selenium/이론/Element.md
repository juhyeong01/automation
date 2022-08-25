<h1>Web element</h1>

Identifying and working with element objects in the DOM<br><br>

<h1>Locator strategies</h1>

Ways to identify one or more specific elements in the DOM<br><br>

<h2>Locator : Description</h2>

class name : Locates elements whose class name contains the search value(compound class names are not permitted)<br><br>
css selector : Locates elements matching a CSS selector<br><br>
id : Locates elements whose ID attributes matches the search value<br><br>
name : Locates elements whose NAME attribute matches the search value<br><br>
link text : Locates anchor elements whose visible text matches the search value<br><br>
partial link text : Locates anchor elements whose visible text contains the search value. If multiple elements are matching, only the first one will be selected<br><br>
tag name : Locates elements whose tag name amtches the search value<br><br>
xpath : Locates elements matching an XPATH expression<br><br>

<h2> Relative Locators</h2>

![image](https://user-images.githubusercontent.com/37740450/186636738-47d847fb-2285-4a23-adae-4767b0de26f1.png)

<h2> Above</h2>
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID : "password"})<br><br>

<h2> Below</h2>

password_locator = locate_with(By.TAG_NAME, "input").below({By.ID : "email"})<br><br>

<h2> Left of</h2>

cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID : "submit"})<br><br>

<h2> Right of</h2>

submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID : "cancel"})<br><br>
