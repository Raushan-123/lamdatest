import time

import options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions



# Set desired capabilities for LambdaTest
LT_CAPABILITIES = [
    {
        "browserName": "chrome",
        "browserVersion": "latest",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test Scenario 1 - Chrome",
        "network": True,
        "video": True,
        "console": True,
        "visual": True
      },


    {
        "browserName": "firefox",
        "browserVersion": "latest",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test Scenario 2 - Firefox",
        "network": True,
        "video": True,
        "console": True,
        "visual": True
    },
    {
        "browserName": "MicrosoftEdge",
        "browserVersion": "latest",
        "platformName": "Windows 10",
        "build": "Selenium Python Tests",
        "name": "Test Scenario 3 - Edge",
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
    #driver = webdriver. Remote (command_executor=grid_url,options=webdriver.ChromeOptions() if capabilities["browserName"]=="Chrome"else webdriver.EdgeOptions ())
    #driver. capabilities.update (capabilities)


    #options.set_capability("LT:Options", capabilities)
    driver.get ("https://www.lambdatest.com/selenium-playground")
    time.sleep (1)
    driver .maximize_window()
    time. sleep (1)
    # 2. Click "Simple Form Demo"
    driver. find_element(By.XPATH, "//*[@id='__next']/div/section[2]/div/ul/li[34]/a"). click()
    time. sleep (1)
    # 3. Validate URL contains "simple-form-demo"
    assert "simple-form-demo" in driver.current_url, "Incorrect page loaded!"
    time. sleep (1)
    # 4. Create a variable for the message
    message = "Welcome to LambdaTest"
    #5. Enter the variable value in the "Enter Message" text box
    message_box = driver.find_element(By. ID, "user-message")
    message_box.send_keys (message)
    time. sleep (2)
    # 6. Click "Get Checked Value"
    driver. find_element(By.XPATH, "//button[text()='Get Checked Value']").click()
    time.sleep(1)
    # 7. Validate whether the same text is displayed in the "Your Message:" section
    output_message = driver.find_element(By.XPATH,"//*[@id='message']").text
    assert message==output_message, "Message does not match!"
    print("Test Passed: All steps executed successfully!")