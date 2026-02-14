import requests
from bs4 import BeautifulSoup

url = f"http://mercury.picoctf.net:27177/check"
r = requests.get(url)
r