from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Lista de descrições a serem preenchidas
descricao = [
    # Adicione suas descrições aqui
]    

indice_arquivo = "ARQUIVO.txt"

# Verifica se o arquivo de índice existe, se não existe, cria o índice inicial
if os.path.exists(indice_arquivo):
    with open(indice_arquivo, "r") as f:
        try:
            indice_atual = int(f.read().strip())
        except ValueError:
            indice_atual = 0
else:
    indice_atual = 0

# Loop através das descrições
for i in range(len(descricao)):
    indice_atual = indice_atual % len(descricao)  # Garante que o índice não exceda o limite da lista
    descricao_selecionada = descricao[indice_atual]

    # Atualiza o índice no arquivo
    with open(indice_arquivo, "w") as f:
        f.write(str(indice_atual + 1))
        
    # Inicia o navegador Edge
    driver = webdriver.Edge()
    driver.get("URL_DO_SEU_SITE")  # Insira a URL do site que deseja automatizar
    # Localiza e preenche o campo de login
    login = driver.find_element(By.ID, 'login')
    login.send_keys('SEU_LOGIN')  # Insira seu login
    password = driver.find_element(By.ID, 'password')
    password.send_keys('SUA_SENHA')  # Insira sua senha
    time.sleep(10)  # Aguarda o carregamento da página
    submitButton = driver.find_element(By.XPATH, '/html/body/div/form/div[3]/div/div/input')
    submitButton.click()  # Clica no botão de envio do login
    time.sleep(10)  # Aguarda o carregamento da próxima página
    
    # Espera até que o elemento desejado esteja clicável e clica nele
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/ui-view/div/nav/div[2]/div[2]/ul[1]/li[1]/a'))
    ).click()
    
    # Acessa o tipo de acesso e seleciona acesso físico/lógico
    WebDriverWait(driver, 13).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/ui-view/div/div[1]/ui-view/vg-tabs/div/div[1]/div[1]/ng-form/div/div[4]/div[1]/vg-field-select/div/div/select'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/ui-view/div/div[1]/ui-view/vg-tabs/div/div[1]/div[1]/ng-form/div/div[4]/div[1]/vg-field-select/div/div/select/option[2]'))
    ).click()  # Seleciona o tipo de acesso
    
    # Continuando a interação e preenchendo campos adicionais...
    
    date_Initial = driver.find_element(By.XPATH, '/html/body/ui-view/div/div[1]/ui-view/vg-tabs/div/div[1]/div[1]/ng-form/div/div[5]/div[2]/vg-field-range-datepicker/div/div/div[3]/input[2]')
    date_Initial.send_keys('01/01/2025')  # Insere data inicial
    date_Final = driver.find_element(By.XPATH, '/html/body/ui-view/div/div[1]/ui-view/vg-tabs/div/div[1]/div[1]/ng-form/div/div[5]/div[2]/vg-field-range-datepicker/div/div/div[3]/input[4]')
    date_Final.send_keys('31/12/2025')  # Insere data final
    
    # Preenche a descrição
    inserindoDescricao = driver.find_element(By.XPATH, '/html/body/ui-view/div/div[1]/ui-view/vg-tabs/div/div[1]/div[1]/ng-form/div/div[14]/div/vg-field/div/div/span/textarea')
    inserindoDescricao.send_keys(descricao_selecionada)
    time.sleep(5)
    
    # Envia o formulário
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/ui-view/div/div[1]/nav/div[2]/span/button'))
    ).click()
    
    # Confirma o envio
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div[3]/button[2]'))
    ).click()

    time.sleep(10)  # Aguarda o processamento final
    driver.quit()  # Encerra o navegador
    indice_atual += 1  # Atualiza o índice para a próxima descrição
