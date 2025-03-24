import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium. webdriver. support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
LT_CAPABILITIES = [
    {
        "browserName": "chrome",
        "browserVersion": "130.0",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test2 Scenario 1 - Chrome",
        "network": True,
        "video": True,
        "console": True,
        "visual": True
    },
    {
        "browserName": "firefox",
        "browserVersion": "132.0",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test2 Scenario 2 - Firefox",
        "network": True,
        "video": True,
        "console": True,
        "visual": True
    },
    {
        "browserName": "MicrosoftEdge",
        "browserVersion": "128.0",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test2 Scenario 3 - Edge",
        "network": True,
        "video": True,
        "console": True,
        "visual": True
    }
    ]

@pytest.mark.parametrize ("capabilities", LT_CAPABILITIES)
def test_lambdatestintegration(capabilities):

		USERNAME = "raushan_kumar1"
		ACCESS_KEY = "LT_4rVnZeelu9Z5K18Q2Ua4sRQbY9AlDlFdValFQsf3DZQrHWK"
		grid_url = f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub"
		if capabilities["browserName"] == "chrome":
			driver = webdriver.Remote(command_executor=grid_url, options=webdriver.ChromeOptions())
		elif capabilities["browserName"] == "firefox":
			driver = webdriver.Remote(command_executor=grid_url, options=webdriver.FirefoxOptions())
		elif capabilities["browserName"] == "MicrosoftEdge":
			driver = webdriver.Remote(command_executor=grid_url, options=webdriver.EdgeOptions())
		else:
			raise Exception(f"Unsupported browser: {capabilities['browserName']}")



		driver.get("https://www.lambdatest.com/selenium-playground")
		#Maximize window
		driver.maximize_window()
		# Step 2: Click "Input Form Submit"
		driver.find_element(By.XPATH, "//*[@id='__next']/div/section[2]/div/ul/li[20]/a").click()
		time.sleep (3)
		driver.execute_script("window.scrollBy(0, 500) ;")
		time. sleep (2)

		# Step 3: Click "Submit" without filling in any details
		# driver.find_element (By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()
		# time.sleep(1)
		name_field = driver.find_element(By.XPATH, "//*[@id='name']")


		submitbutton = driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button")

		# Try submitting the form without filling the field
		submitbutton.click()
		time.sleep(1)

		# Refocus on the required field to check the validation message
		validation_message = name_field.get_attribute("validationMessage")
		print(validation_message)

		# Assert the validation message
		assert validation_message == "Please fill out this field.", f"Expected message not found. Got: {validation_message}"

		print("Validation message asserted successfully!")
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		time. sleep (2)
		driver.find_element(By.NAME,"name").send_keys ("John Doe")
		driver.find_element(By.XPATH,"//*[@id='inputEmail4']").send_keys("john.doe@example.com")
		driver.find_element(By.ID,"inputPassword4").send_keys("paswword4")
		driver.find_element (By.ID,"company").send_keys("Persist")
		driver.execute_script("window.scrollBy(0, 500);")
		driver.find_element(By.ID,"websitename").send_keys("Website.com")
		# Step 6: Select "United States"from the Country drop-down
		country_dropdown = Select(driver.find_element (By. NAME,"country") )
		country_dropdown.select_by_visible_text ("United States")
		driver.find_element(By.ID,"inputCity").send_keys("pune")
		driver.find_element(By.ID,"inputAddress1").send_keys("Hinjewadi")
		driver.find_element(By.ID,"inputAddress2").send_keys("phasel")
		driver.find_element(By.XPATH,"//*[@id='inputState']").send_keys("Maharastra")
		driver.find_element(By.XPATH,"//*[@id='inputZip']").send_keys("411099")
		#submit the form
		driver.find_element(By. XPATH,"//*[@id='seleniumform']/div[6]/button") .click()

		success_msg = driver.find_element(By.CLASS_NAME,"success-msg"). text
		assert"Thanks for contacting us, we will get back to you shortly." in success_msg,"Success message not displayed!"
		# Print Success Message
		print ("Form submitted successfully!")
		# Wait and close the browser
		# Wait and close the browser
		time. sleep (5)
		driver. quit ()