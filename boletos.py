from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações do WebDriver
driver = webdriver.Chrome()  # ou caminho para seu ChromeDriver
driver.maximize_window()  # Maximiza a janela do navegador
driver.get('https://pontoazi.com.br/mail/')  # substitua pela URL do seu Roundcube

# Login no Webmail
email = 'caua.monteiro'
senha = '2e5qdsfz'

driver.find_element(By.ID, 'rcmloginuser').send_keys(email)
driver.find_element(By.ID, 'rcmloginpwd').send_keys(senha)
driver.find_element(By.ID, 'rcmloginsubmit').click()

# Aguardar login e carregar a página principal
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'mailboxlist')))

# Procurar e-mails com assunto específico
search_box = driver.find_element(By.ID, 'mailsearchform')
search_box.send_keys('boleto')
search_box.send_keys(Keys.RETURN)

# Aguardar o carregamento dos resultados de pesquisa
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'message')))

# Selecionar o botão "Selecionar" para abrir as opções
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#select" and contains(@class, "select active")]'))).click()

# Selecionar todos os e-mails encontrados
wait.until(EC.element_to_be_clickable((By.ID, 'rcmbtn147'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Mais"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Mover para..."]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Boletos"]'))).click()

time.sleep(5)
driver.quit()
