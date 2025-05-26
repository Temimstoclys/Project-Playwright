
# 🧪🚀 Projeto de Testes Automatizados com Playwright + Pytest + Allure

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/SEU_USUARIO/SEU_REPOSITORIO/playwright.yml?branch=main&label=CI%2FCD)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📑 Descrição

Projeto de testes automatizados utilizando:
- ✅ **Playwright (Python)**
- ✅ **Pytest**
- ✅ **Allure Reports**
- ✅ **Pipeline CI/CD no GitHub Actions**

Automatizando cenários do site 👉 [https://seubarriga.wcaquino.me](https://seubarriga.wcaquino.me), incluindo:
- 🔐 Login
- ➕ Criação de conta
- 📝 Edição de conta
- 🔍 Visualização de conta
- ❌ Exclusão de conta

## 🗂️ Estrutura de Pastas

```plaintext
.
├── tests
│   ├── pages          # Page Objects
│   ├── test_cases     # Casos de testes
│   └── config.py      # Configurações (BASE_URL, LOGIN, PASSWORD)
├── reports            # Relatórios gerados (Allure)
├── .github
│   └── workflows      # Pipeline CI/CD
├── pytest.ini         # Configurações Pytest
├── requirements.txt   # Dependências
└── README.md
```

## ⚙️ Instalação e Setup Local

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Instale os browsers do Playwright:

```bash
playwright install
```

## 🚀 Como executar os testes

👉 Modo **headless** (sem abrir o navegador):

```bash
pytest
```

👉 Modo **headed** (com navegador visível):

```bash
pytest --headed
```

## 📊 Gerar relatório Allure

1. Execute os testes:

```bash
pytest --alluredir=reports/allure-results
```

2. Gere e visualize o relatório:

```bash
allure serve reports/allure-results
```

## 🔗 CI/CD com GitHub Actions

✔️ O pipeline roda automaticamente a cada push no repositório.

📄 Ver configuração em: `.github/workflows/playwright.yml`

## 🧠 Observações

- ✅ As credenciais e URL estão no arquivo `config.py`.
- ✅ A ordem de execução dos testes é controlada com `pytest-order`.
- ✅ O relatório Allure é gerado e pode ser acessado localmente ou publicado.

## 👨‍💻 Desenvolvido por

**Temínstoclys Pinheiro | QA Engineer**  
🔗 [LinkedIn](https://linkedin.com/in/temínstoclys-pinheiro-7130b990)  
