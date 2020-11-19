sections = [l.strip() for l in open('sections.txt').readlines()]
districts = [m.strip() for m in open('districts.txt').readlines()]

base_url = "https://www.eenadu.net/archivespage/"
month = '05'
year = '2020'
days = 31
section_urls = []
district_urls = []

for i in range(days):
    day = i+1
    for category in range(len(sections)):
        url = base_url+sections[category]+'/'+str(day)+'-'+month+'-'+year
        print(url)
        section_urls.append(url)
    for category in range(len(districts)):
        url = base_url + 'districtmore/' + districts[category] + '/' + str(day) + '-' + month + '-' + year
        print(url)
        district_urls.append(url)

f=open('section_links_may.txt','w')
section_urls=map(lambda x:x+'\n', section_urls)
f.writelines(section_urls)
f.close()

f=open('district_links_may.txt','w')
district_urls=map(lambda x:x+'\n', district_urls)
f.writelines(district_urls)
f.close()