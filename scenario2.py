import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
# #Set-up the WebDriver
# driver = webdriver.Chrome ()

# Set desired capabilities for LambdaTest
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

@pytest.mark.parametrize ("capabilities",LT_CAPABILITIES)
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
    # driver = webdriver. Remote (command_executor=grid_url,options=webdriver.ChromeOptions() if capabilities["browserName"]=="Chrome"else webdriver.EdgeOptions ())
    # driver. capabilities.update (capabilities)
    driver.get("https://www.lambdatest.com/selenium-playground")
    # Maximize window
    driver.maximize_window()
    driver.find_element(By.XPATH,"//*[@id='__next']/div/section[2]/div/ul/li[13]/a").click()
    # Locate the slider with value 15
    slider=driver.find_element (By.XPATH, "//*[@id='slider3']/div/input")
    time.sleep (3)
    # Create an ActionChains object
    actions = ActionChains(driver)

    #Move the slider
    # Drag by 80 offset to the right to move from 15 to 95
    #Attactions.cLick and.hold(slider).move. by offset (200) release performa
    driver.execute_script("arguments[0].value=95;",slider)
    #time.sleep (3)
    # Verify if the slider moved to
    slider_value = driver.find_element(By.XPATH, "//*[@id='slider3']/div/input"). get_attribute('value')
    print(f"Slider moved to: {slider_value}")
    time. sleep (10)
# Close the browser e#driver-quite