import allure

from helpers.find_del_client import find_del_client


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
    with allure.step("Открытие сайта"):
        manager_form.go_to_site()
    with allure.step("Открытие таблицы со всеми клиентами"):
        manager_form.click_customers()

    with allure.step("Получение строк таблицы с клиентами"):
        rows = manager_form.get_customers_table()

    with allure.step("Составление списка со всеми именами клиентов"):
        client_names = manager_form.get_client_names(rows)

    with allure.step("Вычисление клиента, чьё имя ближе всего по длине к среднему значению длин всех имён клиентов"):
        del_client = find_del_client(client_names)
    del_client_number = client_names.index(del_client)
    with allure.step("Удаление найденного клиента"):
        manager_form.delete_client_by_row_number(del_client_number)

    with allure.step("Проверка отсутствия удалённого клиента в таблице"):
        rows = manager_form.get_customers_table()
        for row in rows:
            row_text = row.text
            with allure.step(f"Проверка отсутствия клиента {del_client} в строке {row_text}"):
                assert del_client not in row_text

    with allure.step("Проверка что итоговый список клиентов равен ожидаемому"):
        client_names.remove(del_client)  # Ожидаемый список имён
        assert manager_form.get_client_names(rows) == client_names
