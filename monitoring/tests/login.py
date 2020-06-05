from selenium import webdriver
from monitoring.pages.login import LoginPage
from monitoring.pages.base import MainPage
from time import sleep


def test_login_nonexistent_user():
    driver = webdriver.Chrome('C:\\Users\\Grom\\Documents\\chromedriver.exe')
    login = LoginPage(driver)
    driver.get('https://eos.com/crop-monitoring/')
    sleep(5)
    MainPage(driver).switch_to_frame()
    login.transition_to_login()
    sleep(0.5)
    login.fill_credentials(
        'test+1@test.com',
        'secretPassword'
    )
    login.click_sign_in()
    sleep(1)
    login.available()
    driver.close()
    driver.quit()


if __name__ == "__main__":
    test_login_nonexistent_user()
