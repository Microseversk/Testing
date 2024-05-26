from .locators import RootPageLocators, ResultPageLocators


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver


class RootPage(BasePage):
    def is_title_matches(self, title):
        return title == self.driver.title
    def fill_data_in_input1(self,data):
        element = self.driver.find_element(*RootPageLocators.INPUT1)
        element.send_keys(data)
    def fill_data_in_input2(self,data):
        element = self.driver.find_element(*RootPageLocators.INPUT2)
        element.send_keys(data)

    def click_send_button1(self):
        element = self.driver.find_element(*RootPageLocators.BUTTON1)
        element.click()

    def click_send_button2(self):
        element = self.driver.find_element(*RootPageLocators.BUTTON2)
        element.click()


class ResultPage(BasePage):
    def is_result_found(self):
        return " " not in self.driver.find_element(*ResultPageLocators.RESULT).text

    def get_result(self):
        result = self.driver.find_element(*ResultPageLocators.RESULT)
        return result.text

    def get_error(self):
        error = self.driver.find_element(*ResultPageLocators.ERROR)
        return error.text
