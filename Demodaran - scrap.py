# Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

# Chrome
driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")


url = 'http://pages.stern.nyu.edu/~adamodar/'

driver.get(url)

Data_boton = driver.find_element_by_xpath('/html/body/center/div/table/tbody/tr/td[4]').click()
data_web = Data_boton.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[4]/a').click

data = {}
df = pd.DataFrame(columns=['Links'])

ids = driver.find_elements_by_xpath('/html/body/table/tbody/tr[5]/td[2]/p[1]') #Definición de elemento para descarga
for ii in ids:
    data['Links'] = ii.get_attribute('href')
    df = df.append(data, ignore_index=True)
    print(df)
df.to_csv('RiskPrem_OtherMkts_links')




#Extracción de documentos

