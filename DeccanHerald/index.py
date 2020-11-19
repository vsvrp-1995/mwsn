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
month = '4'
days_in_month = 30
category = []
headline = []
link = []
date = []

url = 'https://www.deccanherald.com/archives'
driver.get(url)

calender_button = driver.find_element_by_class_name('wrap-date')
calender_button = calender_button.find_element_by_tag_name('a')
calender_button.click()
time.sleep(1)

prev_month_button = driver.find_element_by_class_name('flatpickr-prev-month')
prev_month_button.click()
time.sleep(1)
next_month_button = driver.find_element_by_class_name('flatpickr-next-month')

submit_button = driver.find_element_by_class_name('datepicker-submit')


day_container = driver.find_element_by_class_name('dayContainer')
daybuttons = day_container.find_elements_by_tag_name('span')

for i in range(0,6):
    if (daybuttons[i].text == "1"):
        start = i
        break

print(start)

for i in range(days_in_month):
    print(i+1)
    daybuttons[start+i].click()
    submit_button.click()
    time.sleep(3)
    archive_result = driver.find_element_by_id("archive_result")
    blocks = archive_result.find_elements_by_xpath('./div')
    for j in range(int(len(blocks)/2)):
        k = 2*j
        category_temp = blocks[k].find_element_by_class_name('text-uppercase')
        category_temp = category_temp.text

        newslinks = blocks[k+1].find_elements_by_tag_name('a')
        for l in range(len(newslinks)):
            category.append(category_temp)
            headline.append(newslinks[l].text)
            link.append(newslinks[l].get_attribute('href'))
            date.append(i + 1)

    calender_button = driver.find_element_by_class_name('wrap-date')
    calender_button = calender_button.find_element_by_tag_name('a')
    calender_button.click()
    time.sleep(1)
    day_container = driver.find_element_by_class_name('dayContainer')
    daybuttons = day_container.find_elements_by_tag_name('span')

df = pd.DataFrame({'Category':category,'Headline':headline,'Link':link,'Date':date,'Month':month,'Year':year})
filename = year+'_'+month+'.csv'
df.to_csv(filename, index=False, encoding='utf-8')