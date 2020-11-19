get_article_links.py

This one needs a Selenium scrapper
So..
install selenium chrome web driver

pip install selenium
pip install pandas

This is a Monthly Scrapper

Set Year, Month and Days (in month)

RUN the code

get_links_txt.py

give it input filename and output filename #follow standards
Just selects the links from csv file and pastes them into a txt file (after filtering videos and photos category)

links_to_txt_files.py

pip install scrapy

python -m scrapy runspider links_to_txt_files.py
python -m scrapy runspider links_to_txt_files.py -t csv -o "filename.csv" --loglevel=INFO