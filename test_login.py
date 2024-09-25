import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

def test_login_valido(driver):
    # Abre a página de login
    driver.get("https://www.saucedemo.com/")

    # Preenche o formulário com dados válidos
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("standard_user")

    password_field.send_keys("secret_sauce")

    # Clica no botão de login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Verifica se o usuário foi redirecionado para a página inicial
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_invalido(driver):
    # Abre a página de login
    driver.get("https://www.saucedemo.com/")

    # Preenche o formulário com dados inválidos
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("usuario_invalido")

    password_field.send_keys("senha_invalida")

    # Clica no botão de login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Verifica se a mensagem de erro é exibida
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.text