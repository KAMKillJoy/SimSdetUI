import allure


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
def test_sort_clients(manager_form):
    manager_form.go_to_site()
    with allure.step("Открытие таблицы с клиентами"): manager_form.click_customers()
    with allure.step("Первый клик на заголовок столбца Firstname (сортировка Z->A"): manager_form.click_firstname_sort()
    with allure.step(
            "Второй клик на заголовок столбца Firstname (сортировка A->Z)"): manager_form.click_firstname_sort()

    with allure.step("Проверка соответствия результата сортировки ожидаемому"):
        rows = manager_form.get_customers_table()
        current_names = manager_form.get_client_names(rows)
        assert current_names == sorted(current_names, key=lambda x: x.lower()), "Имена в таблице не отсортированы"
