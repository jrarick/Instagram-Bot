from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import username_credential, password_credential, targeted_user, EXE_PATH
import time, random
import config

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(EXE_PATH)

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)

        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        username_field = driver.find_element_by_xpath("//input[@name='username']")
        password_field = driver.find_element_by_xpath("//input[@name='password']")
        username_field.clear()
        username_field.send_keys(self.username)
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_most_recent_photo(self, user_to_bother):
        driver = self.driver
        driver.get('https://www.instagram.com/' + user_to_bother + '/')
        time.sleep(2)

        links = driver.find_elements_by_tag_name('a')
        hrefs = [elem.get_attribute('href') for elem in links]
        photos_hrefs = []

        for href in hrefs:
            if '.com/p/' in href:
                photos_hrefs.append(href)
        self.most_recent = photos_hrefs[0]

    def comment_on_photo(self):
        driver = self.driver
        comments_to_leave = [
            'Wow great content keep it up.',
            'Really like engaging with this type of content.',
            'Inspiring, thanks for sharing.',
            'Fantastic photo, lets collab some time.',
            'I was a different person before you posted this. It changed me.'
        ]
        driver.get(self.most_recent)
        time.sleep(2)

        button = driver.find_element_by_xpath('//span[@aria-label="Comment"]')
        print(button)
        button.click()
        time.sleep(1)
        
        comment_field = driver.find_element_by_xpath('//textarea[@aria-label="Add a comment…"]')
        comment_field.clear()
        comment_field.send_keys(comments_to_leave[random.randint(0, 4)])
        comment_field.send_keys(Keys.RETURN)

MyIG = InstagramBot(username_credential, password_credential)
MyIG.login()
MyIG.get_most_recent_photo(targeted_user)
MyIG.comment_on_photo()
MyIG.close_browser()