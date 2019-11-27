from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_OPEN_BASKET_IN_HEADER = (By.XPATH, "//div[contains(@class,'basket-mini')]/span/a[contains(@href,'/basket/')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS_BLOCK = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ALERTS = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info")

    

    


