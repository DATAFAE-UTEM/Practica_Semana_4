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



def link(url):
    driver.get(url)
    data = {}
    df = pd.DataFrame(columns=['Links'])

    ids = driver.find_elements_by_xpath('/html/body/table/tbody/tr[5]/td[2]/p[1]') #Definición de elemento para descarga
    for ii in ids:
        data['Links'] = ii.get_attribute('href')
        df = df.append(data, ignore_index=True)
        print(df)
    df.to_csv('RiskPrem_OtherMkts_links')


link('')

#Extracción de documentos

