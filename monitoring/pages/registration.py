from selenium.webdriver import Remote


class PersonalDetails:
    def __init__(self, browser: Remote):
        self._browser = browser

    def enter_first_name(self, first_name: str) -> None:
        self._browser.find_element_by_id("first_name").send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self._browser.find_element_by_id("last_name").send_keys(last_name)

    def enter_email(self, email: str) -> None:
        self._browser.find_element_by_id(
            "email"
        ).send_keys(email)

    def enter_password(self, password: str) -> None:
        self._browser.find_element_by_id("password").send_keys(password)

    def enter_phone_number(self, phone_number: str) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="signup-form"]/div[4]/div[1]/auth-phone-input/div/div[1]/input'
        ).send_keys(phone_number)


class RegisterAccountPage(PersonalDetails):
    def fill_personal_details(
        self, first_name: str, last_name: str, email: str, password: str, phone_number: str
    ) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_phone_number(phone_number)

    def accept_privacy_policy(self) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="signup-form"]/div[5]/div/div[1]/label'
        ).click()

    def click_sign_up(self) -> None:
        self._browser.find_element_by_xpath(
            '//*[@id="signup-form"]/div[6]/div[1]/button/span'
        ).click()

    def restrictions(self) -> None:
        assert 'Temp and other disposable emails are restricted. Please, enter another email address' == \
            self._browser.find_element_by_css_selector(
                '#signup-form > div:nth-child(2) > div > div > div.ng-active > p'
            ).text












    url: str = "https://eos.com/crop-monitoring/"

    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def load(self, url: str) -> None:
        self._browser.get(url)

    def available(self) -> bool:
        return "Зарегистрироваться" in self._browser.find_element_by_class_name("ng-scope")

    def fill_password(self, password: str) -> None:
        self._password.enter_password(password)

    def press_continue(self) -> None:
        self._browser.find_element_by_xpath('//*[@id="signup-form"]/div[5]/div/div[1]/label').click()
        self._browser.find_element_by_xpath('//*[@id="signup-form"]/div[6]/div[1]/button/span').click()


class RegistrationSuccessPage:
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def load(self) -> None:
        raise RuntimeError("This page can't be open through an URL")

    def available(self) -> bool:
        return "Your Account Has Been Created!" in self._browser.title
