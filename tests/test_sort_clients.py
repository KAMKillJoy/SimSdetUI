import allure
from conftest import browser
from selenium.webdriver.common.by import By
from ui.pages.manager_form import ManagerFormPage


@allure.epic("UI test")
@allure.feature("Работа с пользователями")
@allure.story("Сортировка клиентов")
@allure.title("Тест сортировки таблицы с клиентами")
@allure.description(
    "Тест нажимает заголовок поля Firstname 2 раза для сортировки по имени в алфавитном порядке"
    "затем проверяет соответствие результата сортировки ожидаемому")
@allure.tag("GUI_test", "Simbirsoft", "ManagerForm")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager",
             name="Website")
def test_sort_clients(browser):
    manager_form = ManagerFormPage(browser)
    with allure.step("Открытие сайта"): manager_form.go_to_site()
    with allure.step("Открытие таблицы с клиентами"): manager_form.click_customers()
    with allure.step("Первый клик на заголовок столбца Firstname"): manager_form.click_firstname_sort()
    with allure.step("Второй клик на заголовок столбца Firstname"): manager_form.click_firstname_sort()

    rows = manager_form.get_customers_table()
    names = list()
    for row in rows:
        name = row.find_elements(By.TAG_NAME, "td")[0].text
        names.append(name)
    sorted_names = names
    sorted_names.sort()
    with allure.step("Проверка соответствия результата сортировки ожидаемому"): assert sorted_names == names
