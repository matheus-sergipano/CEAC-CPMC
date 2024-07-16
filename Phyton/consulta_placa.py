import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

t0 = time.time()

placa = input('Informe a placa(sem hífen):')
driver = webdriver.Chrome()
driver.get('https://placafipe.com/')
consulta = driver.find_element(By.ID, 'sPlaca')
consulta.send_keys(placa + Keys.ENTER)
resultado = driver.find_element(By.XPATH, '//*[@id="siteHeader"]/div/div').text

#options = Options()
#options.add_argument("--headless")
#print(consulta)

#consulta.send_keys(placa)
