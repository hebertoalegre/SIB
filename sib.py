import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime 


driver = uc.Chrome()
driver.get('https://www.sib.gob.gt/ConsultaDinamica/?cons=248')
sleep(5)
select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="v-select-select"]')))
options = select_element.find_elements(By.TAG_NAME, "option")

for i in range(len(options))[2:3]:
    opt= select_element.find_elements(By.TAG_NAME, "option")
    fecha = opt[i].text
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@class="v-select-select"]'))).click()
    opt[i].click()
    sleep(7)
    consulta = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/span/span')))
    sleep(7)
    consulta.click()
    descarga = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/span')))
    sleep(3)
    descarga.click()
    sleep(10)

driver.quit()