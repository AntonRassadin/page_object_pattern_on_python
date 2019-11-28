from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS_BLOCK), "In basket has no items"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_BLOCK), "There are items in the basket" 

    def should_be_message_empty_basket(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        if language == "en":
            assert "empty" in message
        else:
            assert False, "temporally work with only EN lang"
    
    def should_not_message_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)