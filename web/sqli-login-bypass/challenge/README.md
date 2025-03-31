## :whale: Docker로 실행하기

이 challenge 환경은 실전 CTF처럼 구성되어 있으며,  
플래그(`flag.txt`)는 Docker 컨테이너 내부에만 존재합니다.  
깃허브에는 포함되어 있지 않으며, 사용자는 플래그 내용을 확인할 수 없습니다.

```bash
docker build -t sqli-login-challenge .
docker run -p 3000:3000 sqli-login-challenge
```

http://localhost:3000/login 으로 접속 후,
SQL Injection을 통해 admin 로그인에 성공하면 플래그가 출력됩니다.
