from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = r'C:\Users\vsvrp\Downloads\chromedriver.exe'
# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

list_districts = [l.strip() for l in open('districts.txt').readlines()]

pages = 20  # 20
category = []
headline = []
link = []
date = []

for k in range(len(list_districts)):

    url = 'https://www.deshabhimani.com/archives/kerala/'+list_districts[k]
    category_name = list_districts[k]
    driver.get(url)
    time.sleep(5)

    for i in range(pages):
        print(i)
        linkbox = driver.find_element_by_class_name('landBtmScn')
        newslinks = linkbox.find_elements_by_tag_name('a')
        print(len(newslinks))
        for l in range(len(newslinks)):
            category.append(category_name)
            headline.append(newslinks[l].text)
            link.append(newslinks[l].get_attribute('href'))

        nextpageli = driver.find_element_by_class_name('nextPage')
        nextpagelink = nextpageli.find_element_by_tag_name('a')
        nextpagelink.click()
        time.sleep(3)

df = pd.DataFrame({'Category': category, 'Headline': headline, 'Link': link})
filename = '21May_20Pages_40.csv'
df.to_csv(filename, index=False, encoding='utf-8')