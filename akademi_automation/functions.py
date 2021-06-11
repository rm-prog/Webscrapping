from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from playsound import playsound

audio_file = "quest-605.mp3"

def open_zoom(first_link, second_link, third_link):
    with open("..\..\info.txt") as info_file:
        email = info_file.readline()
        password = info_file.readline()
    
    print(email)
    print(password)

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://akademi.al")

    time.sleep(1)   
    try:
        login_button = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Hyr"))
        )
        login_button.click()

        time.sleep(1)

        email_input = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.ID, "password"))
        )   

        email_input.clear()
        password_input.clear()
    
        email_input.send_keys(email)
        password_input.send_keys(password)

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
        submit_button.click()

        time.sleep(1)
    except:
        driver.quit()

    enter_first = False
    enter_second = False
    enter_third = False
    while datetime.datetime.now().hour >= 9 and datetime.datetime.now().hour < 13:
        if datetime.datetime.now().hour == 10 and enter_first != True:
            driver.get(first_link)
            while True:   
                try:
                    join_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Bëhu pjesë e klasës live"))
                    )
                    join_button.click()
                    playsound(audio_file)
                    enter_first = True
                    
                    break
                except:
                    time.sleep(60)
                    driver.refresh()
                    continue
        elif datetime.datetime.now().hour == 11 and enter_second != True:
            driver.get(second_link)
            while True:    
                try:
                    join_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Bëhu pjesë e klasës live"))
                    )
                    join_button.click()
                    enter_second = True
                    playsound(audio_file)
                    break
                except:
                    time.sleep(60)
                    driver.refresh()
                    continue
        elif datetime.datetime.now().hour == 12 and enter_third != True:
            driver.get(third_link)
            while True:   
                try:
                    join_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Bëhu pjesë e klasës live"))
                    )
                    join_button.click()
                    enter_third = True
                    playsound(audio_file)
                    break
                except:
                    time.sleep(60)
                    driver.refresh()
                    continue
        time.sleep(120)