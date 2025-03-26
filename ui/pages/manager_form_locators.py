from selenium.webdriver.common.by import By


class ManagerFormLocators:
    LOCATOR_ADD_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[1]")
    LOCATOR_OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    LOCATOR_CUSTOMERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Customers')]")

    LOCATOR_FIRSTNAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
    LOCATOR_LASTNAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
    LOCATOR_POSTCODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
    LOCATOR_SUBMIT_CUSTOMER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add Customer')])[2]")

    LOCATOR_FIRSTNAME_SORT = (By.XPATH, "//a[contains(text(), 'First Name')]")

    LOCATOR_CUSTOMERS_TABLE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/table/tbody/tr")

    LOCATOR_DELETE_CUSTOMER = (By.XPATH, "//tr[@class='ng-scope'][{row}]//button[@ng-click='deleteCust(cust)']")
