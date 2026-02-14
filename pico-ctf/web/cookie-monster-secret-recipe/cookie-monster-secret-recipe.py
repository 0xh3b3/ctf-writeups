import requests
import base64
import sys 
from urllib import parse

def main(p):

    url = f"http://verbal-sleep.picoctf.net:{p}/login.php"
    credentials = {"username":"foo","password":"bar"} 
    r = requests.post(url,data=credentials)

    if r.status_code == 200:
        value = r.headers["Set-Cookie"].split(";")[0]
        cookie = value.split("=")[1]
        flag = base64.b64decode(parse.unquote(cookie,"utf-8"))
        print(flag.decode())

    else:
        print("Error Parsing Url")

if __name__ == "__main__":
    try:
        port = sys.argv[1]

        if len(sys.argv) == 2:
            main(port)   

    except(ValueError,IndexError):
        print("Usage: python3 script.py <port>")
