import pytest
from tests.pages.login_page import LoginPage
from tests.pages.contas_page import ContasPage

@pytest.mark.order(3)
def test_editar_conta(page):
    login = LoginPage(page)
    conta = ContasPage(page)

    login.navigate()
    login.login()

    conta.acessar_menu_contas()
    conta.editar_conta("Conta Teste", "Conta Editada")

    toast = conta.get_toast_message()
    assert "Conta alterada" in toast
