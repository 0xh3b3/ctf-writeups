import requests
import sys
import re
from bs4 import BeautifulSoup

def main(p):
	url = f"http://titan.picoctf.net:{p}/" 
	r = requests.get(url)

	match = re.search("^picoCTF{.*$")
	html = r.text
	soup = BeautifulSoup(html,'html.parse')
	
	flag = soup.find(id=soup)

if __name__ == "__main__":
	port = sys.arv[0]

	try:
		if len(sys.argv) == 2:
			main(port)

	except(ValueError,IndexError):
		print("Usage: python3 script.py <port>")
