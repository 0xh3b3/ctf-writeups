import requests
import sys
from bs4 import BeautifulSoup

def main(port):
    url = f"http://saturn.picoctf.net:{port}/"
    
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,"html.parse")

    print(soup)

if __name__ == "__main__":
    try:
        port = sys.argv[1]

        if len(sys.argv) == 2:
            main(port)
    
    except (ValueError, IndexError):
        print("Usage: python3 script.py <port>")