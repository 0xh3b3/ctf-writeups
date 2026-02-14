import requests
from bs4 import BeautifulSoup

#BASE_URL = "https://jupiter.challenges.picoctf.org/problem/36474/"
#robots = "https://jupiter.challenges.picoctf.org/problem/36474/robots.txt"

def main():
    url = "https://jupiter.challenges.picoctf.org/problem/36474/477ce.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    print(soup.flag.text)

if __name__ == "__main__":
    main()







