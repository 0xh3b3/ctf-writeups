import requests
#import js2py
from bs4 import BeautifulSoup

def main():
    url = f"http://titan.picoctf.net:55666/"
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html,'html.parser')

    javascript = soup.find("textarea")

    print(str(javascript))

    #js2py.eval_js(javascript)

if __name__ == "__main__":
    main()





