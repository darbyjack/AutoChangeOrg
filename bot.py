from selenium import webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
from time import sleep

options = Options
options.headless = True
options.add_argument('log-level=3')
driver = webdriver.Chrome('chromedriver.exe', options=options)
fake = Faker()

print("Input Petition URL: ")
petition = input()

print("Input # of times to run: ")
amount = int(input())


def element(input):
    return driver.find_element_by_name(input)


def reload():
    driver.delete_all_cookies()
    driver.get(petition)


def submit():
    full_name = fake.name().split(" ")
    first = full_name[0]
    last = full_name[1]
    email = fake.email()

    first_name_box = element("firstName")
    last_name_box = element("lastName")
    email_box = element("email")

    sign_button = driver.find_element_by_xpath(
        """//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]""")

    first_name_box.send_keys(first)
    last_name_box.send_keys(last)
    email_box.send_keys(email)

    sleep(0.6)
    sign_button.click()
    sleep(0.6)
    reload()


def main():
    driver.get(petition)
    for run in range(1, amount):
        try:
            submit()
        except:
            reload()

main()
