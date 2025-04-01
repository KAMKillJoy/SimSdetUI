from selenium.webdriver.common.by import By


class ManagerFormLocators:
    """Локаторы страницы ManagerForm"""
    ADD_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[1]")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    CUSTOMERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Customers')]")

    FIRSTNAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
    LASTNAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
    POSTCODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
    SUBMIT_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[2]")

    FIRSTNAME_SORT = (By.XPATH, "//a[contains(text(), 'First Name')]")

    CUSTOMERS_TABLE = (By.CSS_SELECTOR, ".table > tbody:nth-child(2)")

    DELETE_CUSTOMER = (By.XPATH, "//tr[@class='ng-scope'][{row}]//button[@ng-click='deleteCust(cust)']")
