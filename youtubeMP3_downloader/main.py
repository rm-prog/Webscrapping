import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def convertVideoToMP3(url):

    # Open chrome web browser
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    # Go to youtube MP3 converter
    driver.get("https://320ytmp3.com/en30/")

    time.sleep(2)

    try:
        # find video URL input and enter url
        input_field = WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.CLASS_NAME, "form-control-lg"))
            )
        input_field.clear()
        input_field.send_keys(url)

        time.sleep(2)
    except:
        driver.quit()

    # find and click searchBtn
    driver.find_element_by_xpath("//button[text()='Search']").click()
    time.sleep(5)
    # find and click convertBtn
    convert_btn = driver.find_element_by_id("cvt-btn")
    time.sleep(5)
    convert_btn.click()
    time.sleep(5)



if __name__ == "__main__":
    video_url = sys.argv[1]
    convertVideoToMP3(video_url)