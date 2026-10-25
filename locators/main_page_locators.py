from selenium.webdriver.common.by import By

FAQ_QUESTION = (By.ID, "accordion__heading-{}")
FAQ_ANSWER = (By.ID, "accordion__panel-{}")
UP_ORDER_BTN = (By.CSS_SELECTOR, "button[class*='Button_Button']")
DOWN_ORDER_BTN = (By.CSS_SELECTOR, "div[class*='Home_FinishButton'] button")
YANDEX_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
