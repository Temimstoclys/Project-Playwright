from playwright.sync_api import Page
from config import BASE_URL, LOGIN, PASSWORD

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = "#email"
        self.senha_input = "#senha"
        self.login_button = "button[type='submit']"
        self.toast_message = ".alert-success"

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, email=LOGIN, senha=PASSWORD):
        self.page.fill(self.email_input, email)
        self.page.fill(self.senha_input, senha)
        self.page.click(self.login_button)

        try:
            self.page.wait_for_selector(self.toast_message, timeout=5000)
        except:
            raise Exception("Login falhou: Toast de sucesso não apareceu.")

    def get_toast_message(self):
        self.page.wait_for_selector(self.toast_message, timeout=5000)
        return self.page.locator(self.toast_message).inner_text()

    def is_logged_in(self):
        try:
            return "Bem vindo" in self.get_toast_message()
        except:
            return False
