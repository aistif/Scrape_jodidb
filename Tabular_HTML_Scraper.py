from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from DB_Config import add_data


chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=3')
browser = webdriver.Chrome(ChromeDriverManager().install())
 
browser.get('http://www.jodidb.org/TableViewer/tableView.aspx?ReportId=93906')
 
 
wait = WebDriverWait(browser, 30)
 
 
elem = wait.until(EC.element_to_be_clickable((By.ID, 'selectMenu2')))
elem.click()

elem_selectAllNone = browser.find_element_by_xpath('//*[@id="li-el-d2-mi3"]')
elem_selectAllNone.click()
 
elem_times = browser.find_elements_by_xpath('//*[@id="DataTable"]/thead/tr[1]/*[@class="TVItemColHeader"]')
dates = []
time.sleep(5) #seconds

for i in elem_times:
    date = i.text
    if (date != "null") and (date != "&nbsp;"):
        dates.append(date)

elem_cont = browser.find_element_by_xpath('//*[@id="Row3"]/nobr/span/a').get_attribute("innerHTML")

data = []
headers = []
rows = browser.find_elements_by_xpath('//*[@class="DataTable"]/tr')
for row in rows:
    header = row.find_element_by_xpath('./th').text
    values = row.find_elements_by_xpath('./td/nobr')
    details = []
    for v in values:
        details.append(v.text)
    headers.append(header)
    data.append(details)

final_data = []

for i in range(len(headers)):
    country = headers[i]
    values = data[i]
    for j in range(len(values)):
        v = values[j]
        dt = dates[j]
        final_data.append([country,dt,v])

df = pd.DataFrame(final_data, columns=[elem_cont,'MonthYear','Value'])

add_data(df)

time.sleep(5) #seconds
browser.close()