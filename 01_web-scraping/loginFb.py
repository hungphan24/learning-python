from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable=automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach", True)

    service = Service(executable_path='D:\dowload\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.facebook.com/?stype=lo&deoia=1&jlou=Afc0gN78ZI3gNBedJnfIiMOah1prgPMDy2VECVbU828xQCxWD99BQAAQMD2LIL8Eq5hIWdBDxLwuh9sb9jgmjvPvfwcaBYEaVTo5npL0_4Wb8Q&smuh=33430&lh=Ac_NtObqEITsGA3S1RQ')
    return driver

def login():
    driver = getDriver()
    driver.find_element(by="id", value="email").send_keys("youremail@gmail.com")
    time.sleep(1)
    driver.find_element(by="id", value="pass").send_keys("yourpass" + Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    
    # Sử dụng XPath để tìm phần tử với các lớp cụ thể
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'x1lliihq') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'x1n2onr6')]")))
        print("user name: " + element.text)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.execute_script("window.stop();")
    sys.exit()

login()
