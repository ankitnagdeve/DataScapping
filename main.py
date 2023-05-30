# Importing
import os
import re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def c_browser():
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')  # incognito tab
    option.add_argument('--mute-audio')  # dis audio
    option.add_argument('window-size=1080,720')  # change window-size(chrome)
    web_d = webdriver.Chrome(options=option)
    return web_d


def scroll_page(driver=None):
    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        sleep(1)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
    print("END")


def main(name):
    web = c_browser()
    try:
        url = 'https://www.linkedin.com/school/case-western-reserve-university/people/?keywords=hiring'
        web.get(url)
        sleep(1)
        web.find_element(By.ID, 'username').send_keys("ankitkapoor992@gmail.com")
        sleep(0.5)
        web.find_element(By.ID, 'password').send_keys("Kapoor@992")
        sleep(0.5)
        web.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(1)
        scroll_page(web)
        while True:
            try:
                sleep(1)
                button_s = web.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--muted.artdeco-button--1.artdeco-button--full.artdeco-button--secondary.ember-view.scaffold-finite-scroll__load-button')
                sleep(2)
                button_s.click()
            except NoSuchElementException:
                print("No Scroll Button Found")
                break
            else:
                scroll_page(web)

        source_code = web.page_source
        profiles_list = web.find_elements(By.CLASS_NAME, "app-aware-link.link-without-visited-state")
        sleep(1)
        print(f"Total Profiles: {len(profiles_list)}")
        profile_urls = []
        sleep(0.5)
        for ele in profiles_list:
            try:
                sleep(0.01)
                profile_page = ele.get_attribute('href')
            except:
                print(f"Error in Profile: {traceback.format_exc()}")
            else:
                profile_urls.append(profile_page)
        print(f"Total Profiles URLs: {len(profile_urls)}")
        print("DATA", profile_urls)
        if profile_urls:
            profile_urls = [str(ele)+'\n' for ele in profile_urls]
    except Exception:
        print(f"Error: {traceback.format_exc()}")

    else:
        pass
        try:
            with open('abc.txt', 'w', encoding='utf-8') as t_file:
                t_file.writelines(profile_urls)
        except Exception:
            pass

        #print(f"Source: {source_code}")




if __name__ == '__main__':
    main('PyCharm')

