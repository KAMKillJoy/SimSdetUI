from ui.base.base_page import BasePage
from ui.pages.manager_form_locators import ManagerFormLocators
from selenium.webdriver.common.by import By


class ManagerFormPage(BasePage):
    PATH = "#/manager"

    def go_to_site(self):
        super().go_to_site(self.PATH)

    def enter_firstname(self, firstname):
        self.input_data(ManagerFormLocators.FIRSTNAME_FIELD, firstname)

    def enter_lastname(self, lastname):
        self.input_data(ManagerFormLocators.LASTNAME_FIELD, lastname)

    def enter_postcode(self, postcode):
        self.input_data(ManagerFormLocators.POSTCODE_FIELD, postcode)

    def click_add_customer_button(self):
        self.click_element(ManagerFormLocators.ADD_CUSTOMER_BUTTON)

    def click_submit_customer_button(self):
        self.click_element(ManagerFormLocators.SUBMIT_CUSTOMER_BUTTON)

    def click_firstname_sort(self):
        self.click_element(ManagerFormLocators.FIRSTNAME_SORT)

    def click_customers(self):
        self.click_element(ManagerFormLocators.CUSTOMERS_BUTTON)

    def get_customers_table(self):
        return self.find_elements(ManagerFormLocators.CUSTOMERS_TABLE)

    def delete_client_by_row_number(self, row):
        ManagerFormLocators.DELETE_CUSTOMER = \
            (ManagerFormLocators.DELETE_CUSTOMER[0],
             ManagerFormLocators.DELETE_CUSTOMER[1].replace("{row}", str(row + 1)))
        self.find_element(ManagerFormLocators.DELETE_CUSTOMER).click()

    def get_client_names(self, rows):
        client_names = []
        for row in rows:
            client_names.append(row.find_element(By.XPATH, "./td[1]").text)
        return client_names
