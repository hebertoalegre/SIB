import os
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def esperar_descarga(carpeta):
    while any([archivo.endswith(".crdownload") for archivo in os.listdir(carpeta)]):
        sleep(1)


# Carpeta base donde estarán las subcarpetas
os.makedirs('temporaly', exist_ok=True)
carpeta_base = os.path.abspath('temporaly')

#####################################################################################
#                                                                                   #
#                        REPORTES 18, 24, 25, 26, 37 Y 383                          #
#                                                                                   #
#####################################################################################

# Lista de reportes
reportes = [18, 24, 25, 26, 37, 383]

for reporte in reportes:
    # Define la carpeta específica para este reporte
    consulta = os.path.join(carpeta_base, f"consulta_{reporte}")
    os.makedirs(consulta, exist_ok=True)
    
    # Configura las opciones de Chrome con la carpeta de descarga específica
    options = uc.ChromeOptions()
    prefs = {
        "download.default_directory": consulta,  # Carpeta específica para el reporte
        "download.prompt_for_download": False,  # No preguntar por descargas
        "directory_upgrade": True,  # Permite sobrescribir archivos existentes
        "safebrowsing.enabled": True  # Deshabilita alertas de descargas inseguras
    }
    options.add_experimental_option("prefs", prefs)

    try:
        driver = uc.Chrome(options=options)
        driver.get(f'https://www.sib.gob.gt/ConsultaDinamica/?cons={reporte}')
        driver.maximize_window()
        sleep(8)
        consulta = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/span/span')))
        sleep(7)
        consulta.click()
        descarga = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/span')))
        descarga.click()
        sleep(5)
    finally:
        driver.quit()

#####################################################################################
#                                                                                   #
#                REPORTES 23, 248 Y 43 MONEDA NACIONAL Y EXTRANJERA                 #
#                                                                                   #
#####################################################################################

##### REPORTE 23 #####

# Lista de reportes
reportes = {0:'23mn', 1:'23me'}
try:
    for key, reporte in reportes.items():
        # Define la carpeta específica para este reporte
        consulta = os.path.join(carpeta_base, f"consulta_{reporte}")
        os.makedirs(consulta, exist_ok=True)

        # Configura las opciones de Chrome con la carpeta de descarga específica
        options = uc.ChromeOptions()
        prefs = {
            "download.default_directory": consulta,  # Carpeta específica para el reporte
            "download.prompt_for_download": False,  # No preguntar por descargas
            "directory_upgrade": True,  # Permite sobrescribir archivos existentes
            "safebrowsing.enabled": True  # Deshabilita alertas de descargas inseguras
        }
        options.add_experimental_option("prefs", prefs)

        driver = uc.Chrome(options=options)
        driver.get('https://www.sib.gob.gt/ConsultaDinamica/?cons=23')
        driver.maximize_window()
        sleep(7)
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ConsultaDinamica-1893161255"]/div/div[2]/div[5]/div/div[2]/div/div[3]/div/div/div[5]/div/select')))
        opt = select_element.find_elements(By.TAG_NAME, "option")
        select_element.click()
        opt[key].click()
        sleep(7)
        consulta = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/span/span')))
        sleep(7)
        consulta.click()
        descarga = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/span')))
        sleep(3)
        descarga.click()
        sleep(5)
finally:
    driver.quit()

##### REPORTE 43 #####
try:
    # Define la carpeta específica para este reporte
    consulta = os.path.join(carpeta_base, f"consulta_43")
    os.makedirs(consulta, exist_ok=True)

    # Configura las opciones de Chrome con la carpeta de descarga específica
    options = uc.ChromeOptions()
    prefs = {
        "download.default_directory": consulta,  # Carpeta específica para el reporte
        "download.prompt_for_download": False,  # No preguntar por descargas
        "directory_upgrade": True,  # Permite sobrescribir archivos existentes
        "safebrowsing.enabled": True  # Deshabilita alertas de descargas inseguras
    }
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    driver.get('https://www.sib.gob.gt/ConsultaDinamica/?cons=43')
    driver.maximize_window()
    sleep(7)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ConsultaDinamica-1893161255"]/div/div[2]/div[5]/div/div[2]/div/div[3]/div/div/div[5]/div/select/option[1]'))).click()
    sleep(5)
    consulta = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/span/span')))
    sleep(7)
    consulta.click()
    descarga = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/span')))
    sleep(3)  
    descarga.click()
    sleep(5)
finally:
    driver.quit()


##### REPORTE 248 #####

# # Lista de reportes
reportes = {0:'248mn', 1:'248me'}

try:
    for key, reporte in reportes.items():
        # Define la carpeta específica para este reporte
        consulta = os.path.join(carpeta_base, f"consulta_{reporte}")
        os.makedirs(consulta, exist_ok=True)

        # Configura las opciones de Chrome con la carpeta de descarga específica
        options = uc.ChromeOptions()
        prefs = {
            "download.default_directory": consulta,  # Carpeta específica para el reporte
            "download.prompt_for_download": False,  # No preguntar por descargas
            "directory_upgrade": True,  # Permite sobrescribir archivos existentes
            "safebrowsing.enabled": True  # Deshabilita alertas de descargas inseguras
        }
        options.add_experimental_option("prefs", prefs)

        driver = uc.Chrome(options=options)
        driver.get('https://www.sib.gob.gt/ConsultaDinamica/?cons=248')
        driver.maximize_window()
        sleep(7)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ConsultaDinamica-1893161255"]/div/div[2]/div[5]/div/div[2]/div/div[3]/div/div/div[3]/div/select/option[2]'))).click()
        sleep(5)
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ConsultaDinamica-1893161255"]/div/div[2]/div[5]/div/div[2]/div/div[3]/div/div/div[11]/div/select')))
        opt= select_element.find_elements(By.TAG_NAME, "option")
        select_element.click()
        opt[key].click()
        sleep(7)
        consulta = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1"]/span/span')))
        sleep(7)
        consulta.click()
        descarga = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/span')))
        sleep(3)
        descarga.click()
        sleep(5)

finally:
    driver.quit()