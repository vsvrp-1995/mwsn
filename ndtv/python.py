from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time as time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = r'C:\Users\vsvrp\Downloads\chromedriver.exe'
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

year = '2020'
month = '04'
headline = []
link = []
date = []

url = 'https://archives.ndtv.com/articles/'+year+'-'+month+'.html'


driver.get(url)
time.sleep(5)
main_content = driver.find_element_by_id('main-content')
list_h3 = main_content.find_elements_by_tag_name('h3')
print(len(list_h3))
list_ul = main_content.find_elements_by_tag_name('ul')
print(len(list_ul))

for i in range(len(list_h3)):
    print(i)
    current_date = list_h3[i].find_element_by_tag_name('a')
    current_date = current_date.text
    current_news_list = list_ul[i].find_elements_by_tag_name('a')
    for j in range(len(current_news_list)):
        print(j)
        headline.append(current_news_list[j].text)
        link.append(current_news_list[j].get_attribute('href'))
        date.append(current_date)

df = pd.DataFrame({'Headline':headline,'Link':link,'Date':date})
filename = year+'_'+month+'.csv'
df.to_csv(filename, index=False, encoding='utf-8')

#
# year = '2020'
# month = '04'
# number_of_days = 30
# starttime = 43922
# category = []
# headline = []
# link = []
# date = []
#
# for dates in range(number_of_days):
#
#
#
#     paper_container = driver.find_elements_by_class_name('cnt')
#     list_container = paper_container[1].find_element_by_tag_name('table')
#     list_of_links = list_container.find_elements_by_tag_name('a')
#
#     for i in range(len(list_of_links)):
#         category.append('unknown')
#         headline.append(list_of_links[i].text)
#         link.append(list_of_links[i].get_attribute('href'))
#         date.append(dates+1)
#         print(i)
#
# df = pd.DataFrame({'Category':category,'Headline':headline,'Link':link,'Date':date,'Month':month,'Year':year})
# filename = year+'_'+month+'.csv'
# df.to_csv(filename, index=False, encoding='utf-8')
#
# driver.quit()
