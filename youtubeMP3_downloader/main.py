import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time

def convertVideoToMP3(url):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Open chrome web browser
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    # Go to youtube MP3 converter
    driver.get("https://get.topsandtees.space/")

    time.sleep(3)

    try:
        # find input field and enter video URL
        input_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        input_field.send_keys(url)

        time.sleep(1)

        # find searchBtn and click it
        search_btn = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
        search_btn.click()

        time.sleep(2)

        # find downloadBtn and click it
        download_btn = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-item__download"))
        )
        download_btn.click()

        time.sleep(1)

        # click downloadBtn again

        download_btn = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-item__download"))
        )
        download_btn.click()

        time.sleep(10)
    except:
        driver.quit()

    

if __name__ == "__main__":
    video_url = sys.argv[1]
    convertVideoToMP3(video_url)