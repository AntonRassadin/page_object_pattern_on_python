from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()

    def should_be_busket_allert_product_name(self):
        basket_alerts = self.browser.find_elements(*ProductPageLocators.BASKET_ALERTS)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert basket_alerts[0].text == product_name, "Product name in basket allert are different"

    def should_be_busket_allert_price(self):
        basket_alerts = self.browser.find_elements(*ProductPageLocators.BASKET_ALERTS)
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert basket_alerts[2].text == price, "Price in basket allert are different"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"

    def should_success_message_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"