from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações do WebDriver
driver = webdriver.Chrome()  # ou caminho para seu ChromeDriver
driver.get('https://webmail.seudominio.com')  # substitua pela URL do seu Roundcube

# Login no Webmail
email = 'seu_email@dominio.com'
senha = 'sua_senha'

driver.find_element(By.ID, 'rcmloginuser').send_keys(email)
driver.find_element(By.ID, 'rcmloginpwd').send_keys(senha)
driver.find_element(By.ID, 'rcmloginsubmit').click()

# Aguardar login e carregar a página principal
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'mailboxlist')))

# Procurar e-mails com assunto específico
search_box = driver.find_element(By.ID, 'quicksearchbox')
search_box.send_keys('impressão de boletos')
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Aguarde o carregamento dos resultados

# Selecionar todos os e-mails encontrados
checkboxes = driver.find_elements(By.NAME, 'uid[]')
for checkbox in checkboxes:
    checkbox.click()

# Mover para a pasta desejada
driver.find_element(By.ID, 'rcmbtn103').click()  # Clique para mover
driver.find_element(By.XPATH, '//span[text()="Boletos"]').click()  # Escolha a pasta "Boletos"

# Fechar navegador
time.sleep(5)
driver.quit()
