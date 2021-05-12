# Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")

url = 'http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html'

# Información asociada a la tabla
driver.get(url)
print(driver.title)

data1 = {}
df1 = pd.DataFrame(
    columns=['Country', 'Continent', 'Moody´s Rating', 'Rating-based Default Spread', 'Total Equity Risk Premium',
             'Country Risk Premium'])  # Nombres de los header de tabla

rows = len(driver.find_elements_by_xpath("/html/body/div/div/div/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div/div/div/div/table/tbody/tr[1]/td"))
print(rows)
print(cols)

# Considerar Alinear elementos dentro de 'data['']' según definición de headers
# PERMITE EXTRAER HASTA ZAMBIA, LUEGO EL MODELO SE QUIEBRA POR ESTRUCTURA DE TABLA PRESENTE AL FINAL.

# Tabla 1

for r in range(2, rows + 1):
    data1['Country'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
    data1['Continent'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
    data1['Moody´s Rating'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[3]").text
    data1['Rating-based Default Spread'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[4]").text
    data1['Total Equity Risk Premium'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[5]").text
    data1['Country Risk Premium'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[6]").text
    df1 = df1.append(data1, ignore_index=True)
    print(df1)
    df1.to_csv('Risk Premiums for Other Markets - data 1')

# Tabla 2

data2 = {}
df2 = pd.DataFrame(columns=['Country', 'PRS Composite Risk Score', 'ERP', 'CRP', 'Default Spread'])

for r in range(160, rows + 1):
    data2['Country'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[1]").text
    data2['PRS Composite Risk Score'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[2]").text
    data2['ERP'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[3]").text
    data2['CRP'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[4]").text
    data2['Default Spread'] = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/table/tbody/tr[" + str(r) + "]/td[5]").text
    df2 = df2.append(data2, ignore_index=True)
    print(df2)
    df2.to_csv('Frontier Markets (no sovereign ratings) - data')
