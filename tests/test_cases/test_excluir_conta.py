import pytest
from tests.pages.login_page import LoginPage
from tests.pages.contas_page import ContasPage

@pytest.mark.order(5)
def test_excluir_conta(page):
    login = LoginPage(page)
    conta = ContasPage(page)

    login.navigate()
    login.login()

    conta.acessar_menu_contas()
    conta.excluir_conta("Conta Editada")

    toast = conta.get_toast_message()
    assert "Conta removida" in toast
