from selenium.webdriver.common.by import By

SAMOKAT_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
SURNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
METRO_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
METRO_LIST = (
    By.XPATH,
    "//button[contains(@class, 'select-search__option')][.//div[text()='{}']]",
)
PHONE_FIELD = (
    By.CSS_SELECTOR,
    "input[placeholder='* Телефон: на него позвонит курьер']",
)
NEXT_PAGE_BTN = (By.CSS_SELECTOR, "button[class*='Button_Middle']")

DATE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
PERIOD_LIST = (By.CLASS_NAME, "Dropdown-control")
PERIOD_OPTION_LIST = (
    By.XPATH,
    "//div[contains(@class, 'Dropdown-option') and text()='{}']",
)
COLOR_CHECKBOX = (By.XPATH, "//label[text()='{}']")
COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

ORDER_SUBMIT_BTN = (
    By.XPATH,
    "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']",
)
ORDER_YES_BTN = (
    By.XPATH,
    "//div[contains(@class, 'Order_Buttons')]/button[text()='Да']",
)

ORDER_FINISH_WINDOW = (By.CSS_SELECTOR, "[class*='Order_ModalHeader']")
