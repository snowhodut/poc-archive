# PoC Archive :test_tube:

**보안 취약점 분석 및 PoC (Proof of Concept) 실습 아카이브**  
웹 기반 보안 취약점을 직접 재현하고, 실습 가능한 코드와 환경을 제공합니다.

---

## :mag: 포함된 웹 취약점 목록

- SQL Injection (기본, WAF 우회)
- XSS (Reflected)
- SSRF (Server-Side Request Forgery)
- File Upload
- IDOR (Insecure Direct Object Reference)

<br>

## :hammer_and_wrench: 활용 방법

1. 각 폴더별 `app.py` 실행 (또는 `challenge/` 내 Docker 실행)
2. `poc.py`를 통해 취약점 공격 시나리오 자동 실행
3. 필요 시 `payloads.txt`로 여러 입력 실험
4. `challenge/`는 실습 심화용 CTF-style 문제 환경

<br>

## :book: 활용 목적

- 취약점 개념의 직접 실습 및 재현
- CTF 준비 및 문제 해결력 강화

> :warning: 본 저장소의 코드는 **학습 및 연구 목적**으로 작성되었습니다.  
> 실제 시스템이나 타인의 서비스에 대한 **무단 테스트 또는 비윤리적 사용을 금지**합니다.
