import requests # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup
import pandas as pd

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
soup = BeautifulSoup(r.content, "html.parser")



Title = []
Company = []
Location = []
Time = []
Link = []

URL = 'https://www.monster.de/jobs/suche/?q=java&cy=DE&rad=20&intcid=swoop_HeroSearch_DE'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

data = soup.find(id='ResultsContainer')
individual_job_data = data.find_all('section', class_='card-content')
#
# k = soup.find('title')
# print(k)
#
# k = soup.find('div', attrs={'class':'menu__wrap'})


for i in individual_job_data:
    title_data = i.find('h2', class_='title')
    company_data = i.find('div', class_='company')
    location_data = i.find('div', class_='location')
    #time_data = i.find('div', class_='meta flex-col')
    if None in (title_data, company_data, location_data):
        continue
    application_link = title_data.find('a') ['href']
    print(title_data.text.strip())
    print(company_data.text.strip())
    print(location_data.text.strip())
    #print(meta_flex-col.text.strip())
    print(application_link)

    application_link = title_data.find('a')['href']
    Title.append(title_data.text.strip())
    Company.append(company_data.text.strip())
    Location.append(location_data.text.strip())
    #Time.append(meta_flex-col.text.strip())
    Link.append(application_link)

df = pd.DataFrame({
    'Title': Title,
    'Company': Company,
    'Location': Location,
    'Time': Time,
    'Link': Link,
})

df.to_csv('JobsPython5.csv', index=False, encoding='utf-8')


