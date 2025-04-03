from selenium.webdriver.common.by import By

from ui.base.base_page import BasePage
from ui.pages.manager_form_locators import ManagerFormLocators


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

    def delete_client_by_row_number(self, row_number):
        """
           Удаляет клиента из таблицы по указанному номеру строки.

           Находит и кликает кнопку удаления для конкретной строки таблицы, подставляя переданный номер строки
           в шаблон локатора. Нумерация строк начинается с 1, поэтому к переданному номеру добавляется 1.

           Args:
               row_number (int): Номер строки клиента для удаления (начиная с 0 для удобства работы с индексами)

           Логика работы:
               1. Берется базовый локатор кнопки удаления из ManagerFormLocators.DELETE_CUSTOMER
               2. В локаторе заменяется плейсхолдер {row} на фактический номер строки (row_number + 1)
               3. Находится элемент по модифицированному локатору и выполняется клик
           """
        delete_customer = \
            (ManagerFormLocators.DELETE_CUSTOMER[0],
             ManagerFormLocators.DELETE_CUSTOMER[1].replace("{row}", str(row_number + 1)))
        self.find_element(delete_customer).click()


    def get_client_names(self, rows):
        return [row.find_element(By.XPATH, "./td[1]").text for row in rows]

    def get_client_lastnames(self, rows):
        return [row.find_element(By.XPATH, "./td[2]").text for row in rows]

    def get_client_postcodes(self, rows):
        return [row.find_element(By.XPATH, "./td[3]").text for row in rows]


    def get_client_text(self, client):
        rows = self.get_customers_table()
        for row in rows:
            if client.first_name in row.text:
                if client.last_name in row.text:
                    cells = row.find_elements(By.TAG_NAME, "td")
        return [cells[0].text, cells[1].text, cells[2].text]
