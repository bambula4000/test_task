from selenium.webdriver import Remote
from selenium import webdriver


class MainPage:
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def load(self, url: str) -> None:
        self._browser.get(url)

    def switch_to_frame(self) -> None:
        # frame = self._browser.find_element_by_xpath('//*[@id="auth-dialog"]/cm-auth-dialog/iframe')
        # self._browser.switch_to.frame(frame)
        self._browser.switch_to.frame(
            self._browser.find_element_by_xpath('//*[@id="auth-dialog"]/cm-auth-dialog/iframe')
        )

    def switch_to_main(self) -> None:
        self._browser.switch_to.defaultContent()
