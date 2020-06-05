from selenium.webdriver import Remote


class LoginPage:
    def __init__(self, browser: Remote):
        self._browser = browser

    def transition_to_login(self):
        sss = self._browser.find_element_by_xpath(
            '/html/body/ui-view/auth/div/div/div[2]/div[2]/ui-view/register/div[3]/div/a'
        )
        sss.click()

    def fill_credentials(self, email_adress, password):
        self._browser.find_element_by_xpath('//*[@id="email"]').send_keys(email_adress)
        self._browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

    def click_sign_in(self):
        self._browser.find_element_by_xpath('//*[@id="sign_in_button"]').click()

    def available(self):
        assert 'Incorrect authentication credentials.' == \
               self._browser.find_element_by_css_selector('#toast-container > div > div > div > div').text
