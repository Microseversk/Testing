from selenium.webdriver.common.by import By


class RootPageLocators(object):
    INPUT1 = (By.ID, 'input1')
    INPUT2 = (By.ID, 'input2')

    BUTTON1 = (By.ID, 'button1')
    BUTTON2 = (By.ID, 'button2')


class ResultPageLocators(object):
    RESULT_CONTAINER = (By.ID,'result_container')
    RESULT = (By.ID,'result')
    ERROR = (By.TAG_NAME, 'h1')