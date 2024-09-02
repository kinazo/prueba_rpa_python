from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def scrape_website():
    service = Service("path/to/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get("https://example.com")
    heading = driver.find_element(By.TAG_NAME, "h1").text
    print(f"Título de la página: {heading}")

    driver.quit()
