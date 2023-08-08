from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
  soup = BeautifulSoup(browser.page_source, "html.parser")
  bright_star_table = soup.find('table', attrs={'class', 'wikitable sortable jquery-tablesorter'})
  table_body = bright_star_table.find('tbody')
  table_rows = table_body.find_all('tr')


  for cell in table_rows:
    tmp=[]
    table_col = cell.find_all('td')

    

    for value in table_col:
      data = value.text.strip()
      tmp.append(data)

    scraped_data.append(tmp)
  
stars_data = []

scrape()

for i in range(0, len(scraped_data)):
  star_name = scraped_data[i][1]
  distance =  scraped_data[i][3]
  mass = scraped_data[i][5]
  radius = scraped_data[i][6]
  lum = scraped_data[i][7]

  required_data = [star_name, distance, mass, radius, lum]
  stars_data.append(required_data)

print(stars_data)




# Calling Method


# Define Header
headers = ["Star name", "Distance from Earth", "Star mass", "Radius", "Luminosity"]

# Define pandas DataFrame 
star_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
star_df_1.to_csv('stars_data.csv',index=True, index_label="id")
