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
category = []
headline = []
link = []
date = []

for dates in range(number_of_days):

    url = 'https://www.thehindu.com/archive/print/'+year+'/'+month+'/'+str(dates+1)+'/'
    print(dates+1)

    driver.get(url)

    paper_container = driver.find_element_by_class_name('tpaper-container')
    sections = paper_container.find_elements_by_tag_name('section')

    for i in range(len(sections)):
        category_name = sections[i].find_element_by_class_name('section-list-heading')
#        print(category_name.text)
        list_container = sections[i].find_element_by_class_name('archive-list')
        list_of_links = list_container.find_elements_by_tag_name('a')
        for j in range(len(list_of_links)):
            category.append(category_name.text)
            headline.append(list_of_links[j].text)
            link.append(list_of_links[j].get_attribute('href'))
            date.append(dates+1)

df = pd.DataFrame({'Category':category,'Headline':headline,'Link':link,'Date':date,'Month':month,'Year':year})
filename = year+'_'+month+'.csv'
df.to_csv(filename, index=False, encoding='utf-8')

driver.quit()
