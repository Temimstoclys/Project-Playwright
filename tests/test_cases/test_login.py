import pytest
from tests.pages.login_page import LoginPage

@pytest.mark.order(1)
def test_login_sucesso(page):
    login = LoginPage(page)
    login.navigate()
    login.login()
    assert "Bem vindo" in login.get_toast_message()
