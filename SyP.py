# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # hace que se ejecuten las acciones cuando ya ha cargado la pagina
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd 


# Opciones de navegacion 
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\panch\\Desktop\\python\\driver\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inica el navegador
url1 = "https://espanol.spindices.com/indices/equity/sp-ipsa-clp" 
driver.get(url1)


WebDriverWait(driver, 5)
sectores = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[7]/div/div[2]/div[1]/div[2]/div/ul/li[4]")
sectores.click()

# Se extrae el IPSA de Chile
ispa_chile = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[7]/div/div[2]/div[1]/div[3]/div[4]/div[1]")
ispa_chile = ispa_chile.text 

print(ispa_chile)

driver.quit()

time.sleep(10)


options2 = webdriver.ChromeOptions()
options2.add_argument('--start-maximized')
options2.add_argument('--disable-extensions')

driver_path2 = 'C:\\Users\\panch\\Desktop\\python\\driver\\chromedriver.exe'

driver2 = webdriver.Chrome(driver_path2, chrome_options=options2)
url2 = "https://espanol.spindices.com/indices/equity/sp-clx-igpa-clp"
driver2.get(url2)

# hacer click en sectores
igpa = driver2.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[7]/div/div[2]/div[1]/div[2]/div/ul/li[4]")
igpa.click()

# Se extrae el IGPA de Chile
igpa_chile = driver2.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[7]/div/div[2]/div[1]/div[3]/div[4]/div[1]")
igpa_chile = igpa_chile.text 

print(igpa_chile)

driver2.quit()