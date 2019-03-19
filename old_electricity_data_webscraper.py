import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

url = "https://www.nordpoolgroup.com/Market-data1/#/n2ex/table"

#driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows/bin/phantomjs.exe")
options = Options()
options.headless = True
driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe', chrome_options=options)

driver.get(url)

html = driver.execute_script("return document.documentElement.innerHTML;")

driver.quit() # is this needed?

soup = BeautifulSoup(html,"lxml")

data = []

table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

currentDayTariff = []
for i in data:
    commaToFloat = locale.atoi(i[3]) / 1000
    currentDayTariff.append(commaToFloat)

currentDayStats = [currentDayTariff[24], currentDayTariff[25], currentDayTariff[26]]
del currentDayTariff[24:]

# Last night at 1:36am it was taking data from yesterday's values (as it gets data from 2nd column)
# But it doesn't update on new day, so need to work around this
print('Today\'s kWh pricing: ')
for i in currentDayTariff:
    print(i,end="p \n")

print('Minimum value is: {min}p'.format(min=currentDayStats[0]))
print('Maximum value is: {max}p'.format(max=currentDayStats[1]))
print('Average value is: {avg}p'.format(avg=currentDayStats[2]))
