from selenium import webdriver
from monitoring.pages.base import MainPage
from monitoring.pages.registration import RegisterAccountPage
from time import sleep


def test_registration_restricted_email():
    driver = webdriver.Chrome('C:\\Users\\Grom\\Documents\\chromedriver.exe')
    driver.get('https://eos.com/crop-monitoring/')
    sleep(5)
    MainPage(driver).switch_to_frame()
    registration = RegisterAccountPage(driver)
    registration.fill_personal_details(
        'FirstName',
        'LastName',
        'test+1@test.com',
        'secretPassword',
        '508585852'
    )
    registration.accept_privacy_policy()
    registration.click_sign_up()
    sleep(0.5)
    registration.restrictions()
    driver.close()


if __name__ == "__main__":
    test_registration_restricted_email()
