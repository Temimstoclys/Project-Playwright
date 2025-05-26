import pytest
from tests.pages.login_page import LoginPage
from tests.pages.contas_page import ContasPage

@pytest.mark.order(4)
def test_visualizar_conta(page):
    login = LoginPage(page)
    conta = ContasPage(page)

    login.navigate()
    login.login()

    conta.acessar_menu_contas()

    assert conta.conta_existe("Conta Editada"), "Conta não encontrada na listagem!"
