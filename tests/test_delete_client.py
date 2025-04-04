import allure

from helpers.find_del_client import find_del_client
from tests.conftest import manager_form


@allure.epic("UI test")
@allure.feature("Работа с пользователями")
@allure.story("Удаление клиента")
@allure.title("Тест удаления клиента")
@allure.description(
    "Удаляет клиента, чьё имя ближе всего по длине к среднему значению длин всех имён клиентов")
@allure.tag("GUI_test", "Simbirsoft", "ManagerForm")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager",
             name="Website")
def test_delete_client(manager_form):
    manager_form.go_to_site()
    with allure.step("Открытие таблицы со всеми клиентами"):
        manager_form.click_customers()

    with allure.step("Получение строк таблицы с клиентами"):
        rows = manager_form.get_customers_table()

    with allure.step("Составление списков со всеми именами и фамиличми и посткодами клиентов"):
        client_names = manager_form.get_client_names(rows)
        client_lastnames = manager_form.get_client_lastnames(rows)
        client_postcodes = manager_form.get_client_postcodes(rows)
    with allure.step("Вычисление имени ближе всего по длине к среднему значению длин всех имён клиентов"):
        del_client_name = find_del_client(client_names)
        del_client_number = client_names.index(del_client_name)
        del_client_lastname = client_lastnames[del_client_number]
        del_client_postcode = client_postcodes[del_client_number]

    with allure.step("Удаление найденного клиента"):
        manager_form.delete_client_by_row_number(del_client_number)

    with (allure.step("Проверка отсутствия удалённого клиента в таблице")):
        rows = manager_form.get_customers_table()
        for row in rows:
            row_text = row.text
            with allure.step(f"Проверка отсутствия клиента {del_client_name} в строке {row_text}"):
                assert not (
                        (del_client_name in row_text) and
                        (del_client_lastname in row_text) and
                        (del_client_postcode in row_text)
                ), \
                    f"Клиент {del_client_name} {del_client_lastname} postcode {del_client_postcode} обнаружен в таблице"

    with allure.step("Проверка что итоговый список клиентов равен ожидаемому"):
        client_names.remove(del_client_name)  # Ожидаемый список имён
        actual_client_names = manager_form.get_client_names(rows)
        assert actual_client_names == client_names, (f"Ожидаемый список: {client_names},"
                                                     f" актуальный: {actual_client_names}")
