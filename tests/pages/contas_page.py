from playwright.sync_api import Page
from config import BASE_URL


class ContasPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_adicionar = "a[href='/addConta']"
        self.input_nome = "#nome"
        self.btn_salvar = "button[type='submit']"
        self.toast_message = ".alert-success"

    def acessar_menu_contas(self):
        self.page.goto(f"{BASE_URL}/contas")

    def acessar_adicionar_conta(self):
        self.page.goto(f"{BASE_URL}/addConta")

    def criar_conta(self, nome):
        self.page.wait_for_selector(self.input_nome)
        self.page.fill(self.input_nome, nome)
        self.page.click(self.btn_salvar)
        self.page.wait_for_selector(self.toast_message)

    def editar_conta(self, nome_antigo, nome_novo):
        self.page.wait_for_selector(f"//table//td[contains(text(), '{nome_antigo}')]")
        self.page.click(f"//table//td[contains(text(), '{nome_antigo}')]/..//a[contains(@href, 'editar')]")
        self.page.wait_for_selector(self.input_nome)
        self.page.fill(self.input_nome, nome_novo)
        self.page.click(self.btn_salvar)
        self.page.wait_for_selector(self.toast_message)

    def excluir_conta(self, nome):
        linha = self.page.locator(f"//table//td[contains(text(), '{nome}')]/..")
       
        if not linha.is_visible():
            raise Exception(f"Conta '{nome}' não encontrada na tabela para exclusão.")
        btn_excluir = linha.locator("a[href*='remover']")
        
        if not btn_excluir.is_visible():
            raise Exception(f"Botão remover para a conta '{nome}' não encontrado.")
        btn_excluir.click()

    def get_toast_message(self):
        self.page.wait_for_selector(self.toast_message)
        return self.page.locator(self.toast_message).inner_text()

    def conta_existe(self, nome):
        return self.page.locator(f"//table//td[contains(text(), '{nome}')]").is_visible()
