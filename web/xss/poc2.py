import requests

url = "http://localhost:3000"

def check_escaping():
    """
    index.html이 사용자 입력을 이스케이프 처리하는지 검사합니다.
    사용한 payload: "<script>alert('XSS');</script>"
    이스케이프가 제대로 된다면, 브라우저에는 <script> 태그 대신 &lt;script&gt;와 같이 표시되어야 합니다.
    """
    test_payload = "<script>alert('XSS');</script>"
    res = requests.get(url, params={"q": test_payload})
    
    # unescaped payload가 그대로 출력되지 않고, 대신 이스케이프된 문자열(&lt;script&gt; 또는 &lt;script)이 보이면 이스케이프가 적용된 것으로 판단.
    if "<script>" not in res.text and ("&lt;script&gt;" in res.text or "&lt;script" in res.text):
        return True
    else:
        return False

def check_xss(payload):
    """
    주어진 payload가 이스케이프 없이 그대로 출력되어 XSS 취약점이 발생하는지 검사합니다.
    만약 payload가 unescaped 상태라면, <script> 태그와 alert('XSS'); 부분이 그대로 노출됩니다.
    """
    res = requests.get(url, params={"q": payload})
    
    # unescaped payload인 경우, 실제 <script> 태그와 그 내용이 그대로 포함되어 있어야 합니다.
    if "<script>" in res.text and "</script>" in res.text and "alert('XSS');" in res.text:
        return True
    return False

# XSS 공격이 가능한 올바른 페이로드
valid_payload = "<script>alert('XSS');</script>"
# 일반 문자열 (XSS 공격에 사용될 수 없는 값)
invalid_payload = "hello"
#invalid_payload = "<script>alert('XSS');</script>"

# 1. 먼저 index.html 파일이 사용자 입력을 이스케이프 처리하는지 검사합니다.
if check_escaping():
    print("[+] index.html은 사용자 입력을 올바르게 이스케이프 처리합니다.")
    # 이스케이프 처리된 경우 valid_payload라도 unescaped 상태로 출력되지 않아야 합니다.
    if check_xss(valid_payload):
        print("[-] 하지만, 유효한 XSS payload가 unescaped 상태로 출력되었습니다! (예상치 않은 결과)")
    else:
        print("[+] 유효한 XSS payload가 이스케이프 처리되므로, 취약점은 존재하지 않습니다.")
else:
    print("[-] index.html에서 이스케이프 처리가 적용되지 않았습니다!")
    # 이스케이프 처리가 되지 않았다면 valid_payload를 넣었을 때 unescaped 상태로 출력되어 XSS 취약점이 있다고 판단해야 합니다.
    if check_xss(valid_payload):
        print("[+] PoC 성공: XSS 취약점 존재!")
    else:
        print("[-] PoC 실패: XSS 취약점 없음.")

# 추가로, 일반 문자열이 false positive로 취약점으로 감지되지 않는지 확인합니다.
if check_xss(invalid_payload):
    print("[-] 일반 문자열이 취약점으로 감지되었습니다! (False positive)")
else:
    print("[+] 일반 문자열은 취약점으로 감지되지 않습니다.")
