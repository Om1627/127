  
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

response = requests.get(START_URL,verify=False)
time.sleep(10)
def scrape():
    headers = ["Proper name","Distance","Mass","Radius"]
    stars_data = []
    for i in range(0, 100):
        soup = BeautifulSoup(response.content, "html.parser")
        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
        
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()