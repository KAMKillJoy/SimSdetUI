import allure

from data.new_client import Client


@allure.epic("UI test")
@allure.feature("Работа с пользователями")
@allure.story("Добавление клиента")
@allure.title("Тест добавления нового клиента")
@allure.description("Тест генерирует Имя клиента по алгоритму из ТЗ,"
                    "заполняет поля Firstname, Lastname, Postcode и нажимает кнопку добавления клиента."
                    "Затем проверяет наличие добавленного клиента в таблице клиентов")
@allure.tag("GUI_test", "Simbirsoft", "ManagerForm")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager",
             name="Website")
def test_new_client_add_form(manager_form):
    client = Client()

    manager_form.go_to_site()
    with allure.step("Нажатие кнопки добавления клиента"):
        manager_form.click_add_customer_button()
    with allure.step("Введение имени клиента (Firstname)"):
        manager_form.enter_firstname(client.first_name)
    with allure.step("Введение фамилии клиента (Lastname)"):
        manager_form.enter_lastname(client.last_name)
    with allure.step("Введение почтового кода (postcode"):
        manager_form.enter_postcode(client.postcode)
    with allure.step("Нажатие кнопки отправки данных"):
        manager_form.click_submit_customer_button()

    with allure.step("Закрытие алерта браузера с подтверждением добавления клиента"):
        manager_form.dismiss_alert()
    with allure.step("Открытие таблицы со всеми клиентами"):
        manager_form.click_customers()
    with allure.step("Поиск в таблице строки, содержащей Firstname и Lastname добавленного клиента"):
        cells = manager_form.get_client_text(client)
    with (allure.step("Проверка соответствия Firstname ожидаемому")):
        actual_first_name = cells[0]
        expected_first_name = str(client.first_name)
        assert actual_first_name == expected_first_name, (f"Firstname {actual_first_name} "
                                                          f"не равно ожидаемому {expected_first_name}")
    with allure.step("Проверка соответствия Lastname ожидаемому"):
        actual_last_name = cells[1]
        expected_last_name = str(client.last_name)
        assert actual_last_name == expected_last_name, (f"Lastname {actual_last_name} "
                                                        f"не равно ожидаемому {expected_last_name}")
    with allure.step("Проверка соответствия Postcode ожидаемому"):
        actual_postcode = cells[2]
        expected_postcode = str(client.postcode)
        assert actual_postcode == expected_postcode, (f"Postcode {actual_postcode} "
                                                      f"не равен ожидаемому {expected_postcode}")
