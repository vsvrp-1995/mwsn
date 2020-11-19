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

year = '2020'
month = '01'
days_in_month = 31
category = []
headline = []
link = []
date = []

url = 'https://www.sakshi.com/archive'
driver.get(url)

for day in range(days_in_month):

    calender_button = driver.find_element_by_class_name('archive')
    calender_input = calender_button.find_element_by_id('popupDatepicker')
    calender_input.clear()
    temp_date = year + '/' + month + '/' + str(day + 1).zfill(2)
    calender_input.send_keys(temp_date)
    time.sleep(4)
    calender_submit = driver.find_element_by_id('arch_button')
    driver.find_element_by_tag_name("body").click()
    calender_submit.click()

    time.sleep(5)
    archive_result = driver.find_element_by_id("archive_result")
    cat_blocks = archive_result.find_elements_by_class_name('cat_heading')
    archive_list_blocks = archive_result.find_elements_by_class_name('archive_list')

    for j in range(len(cat_blocks)):
        category_temp = cat_blocks[j].text
        newslinks = archive_list_blocks[j].find_elements_by_tag_name('a')
        for k in range(len(newslinks)):
            category.append(category_temp)
            headline.append(newslinks[k].text)
            link.append(newslinks[k].get_attribute('href'))
            date.append(day + 1)
    time.sleep(1)

df = pd.DataFrame({'Category':category,'Headline':headline,'Link':link,'Date':date,'Month':month,'Year':year})
filename = year+'_'+month+'.csv'
df.to_csv(filename, index=False, encoding='utf-8')
