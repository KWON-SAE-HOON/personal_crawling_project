# steam profile crawling system

스팀프로필 문서를 크롤링하여 보관함에 있는 아이템을 보여주고 db에 저장한다

# Requirements
Python 3.x

Django

Beautiful Soup 4

Requests

alluath

---

## 구현할 것
1. steamprofile 과 inventory를크롤링 후 서버에 저장

2. profile number을 입력하면 해당 프로필과 inventory를 공개

3. 아이디 목록을 표시

4. mtm으로 거래 요청 보냄


## url 구조
`/structure`
메인화면 home과 login 창이 있음

`/structure/accounts`
account 목록이 있음

`/structure/account/1`
account detail

`/structure/account/1/delete`
account 삭제

`/structure/account/create`
account 생성




