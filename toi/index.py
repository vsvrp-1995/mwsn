from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = r'C:\Users\vsvrp\Downloads\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

year = '2020'
month = '04'
number_of_days = 30
starttime = 43922
category = []
headline = []
link = []
date = []

for dates in range(number_of_days):

    url = 'https://timesofindia.indiatimes.com/'+year+'/'+month+'/'+str(dates+1)+'/archivelist/year-'+year+',month-'+month+',starttime-'+str(starttime)+'.cms'
    print(dates+1)
    starttime = starttime+1

    driver.get(url)

    paper_container = driver.find_elements_by_class_name('cnt')
    list_container = paper_container[1].find_element_by_tag_name('table')
    list_of_links = list_container.find_elements_by_tag_name('a')

    for i in range(len(list_of_links)):
        category.append('unknown')
        headline.append(list_of_links[i].text)
        link.append(list_of_links[i].get_attribute('href'))
        date.append(dates+1)
        print(i)

df = pd.DataFrame({'Category':category,'Headline':headline,'Link':link,'Date':date,'Month':month,'Year':year})
filename = year+'_'+month+'.csv'
df.to_csv(filename, index=False, encoding='utf-8')

driver.quit()
