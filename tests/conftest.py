import pytest

from ui.pages.manager_form import ManagerFormPage


@pytest.fixture(scope="session")
def manager_form(browser):
    return ManagerFormPage(browser)
