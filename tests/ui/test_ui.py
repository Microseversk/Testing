import page_object.page as page
from page_object.locators import RootPageLocators



class TestAppUI:

    def test_app_title_matches(self,browser):
        root_page = page.RootPage(browser)

        assert root_page.is_title_matches()

    def test_app_result_is_not_empty_if_valid_data(self, browser):
        root_page = page.RootPage(browser)
        root_page.fill_data_in_input2('aaa')
        root_page.click_send_button2()

        result_page = page.ResultPage(browser)

        assert result_page.is_result_found()

    def test_app_button1_is_mounted(self,browser):
        root_page = page.RootPage(browser)

        assert root_page.driver.find_element(*RootPageLocators.BUTTON1)

    def test_app_button2_is_mounted(self,browser):
        root_page = page.RootPage(browser)

        assert root_page.driver.find_element(*RootPageLocators.BUTTON2)

    def test_app_input1_is_mounted(self, browser):
        root_page = page.RootPage(browser)

        assert root_page.driver.find_element(*RootPageLocators.INPUT1)

    def test_app_input2_is_mounted(self, browser):
        root_page = page.RootPage(browser)

        assert root_page.driver.find_element(*RootPageLocators.INPUT2)


    def test_app_result_correct(self, browser):
        root_page = page.RootPage(browser)
        root_page.fill_data_in_input2('aaa')
        root_page.click_send_button2()

        result_page = page.ResultPage(browser)

        assert result_page.get_result() == '6'

    def test_app_bad_request_if_invalid_data(self, browser):
        root_page = page.RootPage(browser)
        root_page.fill_data_in_input2('INVALID DATA {} {}} .,/!#')
        root_page.click_send_button2()

        result_page = page.ResultPage(browser)

        assert result_page.get_error() == 'Bad Request'
