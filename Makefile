.PHONY: install test test-headed report allure clean

# Instala as dependências
install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	python -m playwright install

# Executa testes em modo headless (padrão)
test:
	pytest

# Executa testes com navegador visível (headed)
test-headed:
	pytest --headed

# Gera relatório HTML
report:
	pytest --html=reports/report.html

# Executa testes e gera relatório Allure
allure:
	pytest --alluredir=reports/allure-results --clean-alluredir

# Limpa os relatórios
clean:
	rm -rf reports/*
