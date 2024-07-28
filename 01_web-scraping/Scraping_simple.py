from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def simpleScraping(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option("excludeSwitches", ["enable=automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    service = Service(executable_path='D:\dowload\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(simpleScraping("https://automated.pythonanywhere.com/"))


