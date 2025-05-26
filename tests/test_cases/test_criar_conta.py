import pytest
from tests.pages.login_page import LoginPage
from tests.pages.contas_page import ContasPage

@pytest.mark.order(2)
def test_criar_conta(page):
    login = LoginPage(page)
    conta = ContasPage(page)

    login.navigate()
    login.login()

    conta.acessar_menu_contas()
    conta.acessar_adicionar_conta()

    conta.criar_conta("Conta Teste")
    toast = conta.get_toast_message()

    assert "Conta adicionada" in toast
