  
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = ["Proper name","Distance","Mass","Radius"]
stars_data = []
response = requests.get(START_URL,verify=False)
print(response)