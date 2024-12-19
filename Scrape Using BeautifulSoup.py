pip install pandas
pip install beautifulsoup4


from bs4 import BeautifulSoup
from urllib import request
import pandas as pd

req = request("https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue")
page = urlopen(req).read()