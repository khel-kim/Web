# 웹 프로그래밍의 이해

## Index

[TOC]


## 웹 프로그래밍이란?

웹 프로그래밍이란 HTTP(S) 프로토콜로 통신하는, 클라이언트와 서버를 개발하는 것.

Internet Explorer, Chrome, Firefox와 같은 웹 브라우저는 이미 웹 클라이언트로서 개발되어 있기 때문에 웹 프레임워크를 활용해서 웹 서버를 개발하는 것을 마치 웹 프로그래밍의 전부인 것처럼 착각하기 쉽지만, 실제 프로젝트를 진행하다 보면 웹 클라이언트를 개발해야되는 상황도 많이 발생

웹 서버에 요청을 보내는 웹 클라이언트들

- 웹 브라우저를 사용하여 요청
- 리눅스 `curl` 명령을 사용하여 요청
- *Telnet을 사용하여 요청*
- 직접 만든 클라이언트로 요청

## 다양한 웹 클라이언트

### 웹 브라우저를 사용하여 요청

웹 브라우저는 주소창에 입력된 문장을 해석하여 웹 서버에게 HTTP 요청을 보내는 웹 클라이언트의 역할을 수행한다. 요청을 받은 도메인의 웹 서버는 그 결과를 웹 브라우저로 전송해주고 웹 브라우저는 전송받은 결과를 사용자가 볼 수 있도록 HTML 텍스트를 해석하여 화면에 보여준다.

### 리눅스 curl 명령을 사용하여 요청

리눅스 `curl` 명령은 HTTP/HTTPS/FTP 등 여러 가지의 프로토콜을 사용하여 데이터를 송수신할 수 있는 명령이다.

```
curl <http://www.example.com>

# 결과
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="<https://www.iana.org/domains/example>">More information...</a></p>
</div>
</body>
</html>
```

`curl` 명령은 인자로 넘어온 URL로 HTTP 요청을 보내는 웹 클라이언트의 역할을 수행한다. 이 요청을 받은 [`www.example.com`](http://www.example.com) 도메인의 웹 서버는 그 결과를 응답해준다.

### 직접 만든 클라이언트로 요청

```
$vim example.py

import urllib.request
print(urllib.request.urlopen('<http://www.example.com>').read().decode('uft-8'))

$python3 example.py

# 결과
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="<https://www.iana.org/domains/example>">More information...</a></p>
</div>
</body>
</html>
```

여기서는 방금 작성한 [example.py](http://example.py) 프로그램이 웹 클라이언트가 된다.

## HTTP 프로토콜

HTTP(Hypertext Transfer Protocol)는 웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식으로, TCP/IP 프로토콜 위에서 동작한다. 즉, 우리가 웹을 이용하려면 웹 서버와 웹 클라이언트는 각각 TCP/IP 주소를 가져와야 한다는 의미이다.

우리가 웹 브라우저의 주소창에 http://www.naver.com 을 입력하고 Enter를 누르면 웹 클라이언트와 웹 서버 사이에 HTTP 연결이 맺어지고, 웹 클라이언트는 웹 서버에 HTTP 요청(request) 메시지를 보내게 된다. 웹 서버는 요청에 따른 처리를 진행한 후에 그 결과를 웹 클라이언트에게 HTTP 응답(response) 메시지로 보낸다.

### HTTP 메시지의 구조

HTTP 메시지는 클라이언트에서 서버로 보내는 요청 메시지와 서버에서 클라이언트로 보내는 응답 메시지 2가지가 있고, 그 구조는 다음과 같다.

스타트라인(start line)

헤더(header)

빈 줄(blank line)

바디(Body)

요청라인 또는 상태라인

헤더는 생략 가능

헤더의 끝을 빈 줄로 식별

바디는 생략 가능

- 스타트라인: 요청 메시지일 때 요청라인(request line)이라고 하고, 응답 메시지일 때 상태라인(status line)이라고 함
- 헤더: 스타트라인에 이어 각 행의 끝에 줄 바꿈 문자인 CRLF(Carriage Return Line Feed)가 있으며, 헤더와 바디는 빈 줄로 구분, 헤더와 바디는 생략할 수 있으며, 바디에는 텍스트뿐만이 아니라 바이너리 데이터도 들어갈 수 있음

다음은 바디가 없는 요청 메시지의 예시

```
GET /book/shakespeare HTTP/1.1
Host: www.example.com:8080
```

첫 번째 줄은 요청라인으로, 요청 방식(method), 요청 URL, 프로토콜 버전으로 구성

두 번째 줄은 헤더로, 이름: 값 형식으로 표현하며, 위 예의 경우 헤더가 한 줄뿐이지만 여러 줄도 가능하다. 또한, Host 항목은 필수로 표시해줘야 하는데, 위 예시처럼 Host 헤더로 표시할 수도 있고, 아래 예시처럼 요청라인의 URL에 Host를 표시하면 Host 헤더는 생략할 수 있음. 만약 포드번호를 표시하고 싶다면 Host 항목에 같이 표시하면 된다.

```
GET <http://www.example.com:8080/book/shakespeare> HTTP/1.1
```

다음은 응답 메시지의 예시.

```
HTTP/1/1 200 OK
Content-Type: application/xhtml+xml; charset=utf-8

<html>
...
<html>
```

첫 번째 줄의 상태라인은 프로토콜 버전. 상태 코드, 상태 텍스트로 구성된다. 서버에서 처리 결과를 상태라인에 표시하는데, 위 예시에서는 `200 OK` 이므로 정상적으 처리되었음을 알 수 있다.

두 번째 줄부터 헤더인데, 위 예시는 헤더 항목이 하나뿐인 응답 메시지이고, 이 메시지는 바디를 갖고 있기 때문에 헤더와 바디가 빈 줄로 구분되어 있다.  바디에는 보통 HTML 텍스트가 포함되어 있다.

Note. URI vs URL이란?

URI는 URL을 포함하는 좀 더 넓은 의미의 표현이지만, 웹 프로그래밍에서는 URI와 URL을 동일한 의미로 사용해도 무방하다.

### HTTP 처리 방식

HTTP 메소드를 통해서 클라이언트가 원하는 처리 방식을 서버에 알려준다. HTTP 메소드는 8가지로 정의되어 있는데, 이 중 많이 사용되는 메소드는 GET, POST, PUT, DELETE 4개의 메소드이며, 데이터 조작의 기본이 되는 CRUD와 매핑되는 처리를 한다.

메소드명

GET

POST

PUT

DELETE

HEAD

OPTIONS

TRACE

CONNECT

의미

리소스 취득

리소스 생성, 리소스 데이터 추가

리소스 변경

리소스 삭제

리소스의 헤더(메타 데이터) 취득

리소스가 서포트하는 메소드 취득

루프백 시험에 사용

프록시 동작의 터널 접속으로 변경

CRUD와 매핑되는 역할

Read, 조회

Create, 생성

Update, 변경

Delete, 삭제

GET 방식은 지정한 URL의 정보를 가져오는 메소드로, 가장 많이 사용된다. 웹 브라우저를 이용하여 서버로부터 웹 페이지, 이미지, 동영상 등을 가져오려고 할 때, 수많은 GET 방식의 요청을 사용하게 된다.

POST의 대표적인 기능은 리소스를 생성하는 것으로, 블로그에 글을 등록하는 경우가 이에 해당한다. PUT은 리소스를 변경하는 데 사용된다. 예를 들어, 블로그에서 글을 업로드한 작성자를 변경하거나 글의 내용을 업데이트하는 등의 경우가 이에 해당한다.

DELETE는 이름 그대로 리소스를 삭제하는 메소드이고, 일반적으로 DELETE 요청에 대한 응답은 바디를 반환하지 않는다.

### GET과 POST 메소드

8가지 HTTP 메소드들이 있지만, 가장 많이 사용되는 메소드는 GET과 POST 2가지다. 이것은 HTML의 form에서 지정할 수 있는 메소드가 GET과 POST 밖에 없기 때문이다.

form에서 사용자가 입력한 데이터들을 서버로 보낼 때, GET과 POST는 그 방식에 차이가 있다.

GET은 아래의 예시처럼 URL 부분의 ? 뒤에 이름=값 쌍으로 이어붙여 보낸다.

```
GET <http://docs.djangoproject.com/search/?q=form&release=1> HTTP/1.1
```

반면, POST에서는 GET에서 URL에 포함시켰던 파라미터들을 아래 예시처럼 요청 메시지의 바디에 넣는다.

```
POST <http://docs.djangoproject.com/search/> HTTP/1.1
Content-Type: application/x-www-form-urlencoded

q=forms&release=1
```

URL은 길이 제한이 있기 때문에 GET 방식을 이용하면 많은 양의 데이터를 보내기 어렵다.  또한, 전달되는 사용자의 데이터가 웹 브라우저의 주소창에 노출되어 보안 측면에서도 불리하다.

따라서 form을 사용하거나 추가적인 파라미터를 서버로 보내는 경우에는 GET보다 POST 방식을 많이 사용하게 된다.

### 상태 코드

서버에서의 처리 결과는 응답 메시지의 상태라인에 있는 상태 코드(Status code)를 보고 파악할 수 있다. 상태 코드는 세 자리 숫자로 되어 있는데, 첫 번째 숫자는 HTTP 응답의 종류를 구분하는 데 사용하며, 나머지 두 개의 숫자는 세부적인 응답 내용의 구분을 위한 번호이다.

## URL 설계

URL의 설계는 웹 서버 로직 설계의 첫걸음이고, 사용자 또는 웹 클라이언트에게 웹 서버가 가지고 있는 기능을 명시해주는 중용한 단계이다. 전체 프로그램 로직을 생각하면서 차후에 로직이 변경되더라도 URL 변경은 최소화할 수 있도록 유연하게 설계하는 것이 중요하다.

```
<http://www.example.com:80/services?category=2&kind=patents#n10>

URL 스킴://호스트명:포트번호/경로?쿼리스트링#프라그먼트
```

- URL 스킴: URL에 사용된 프로토콜을 의미
- 호스트명: 웹  서버의 호스트명으로, 도메인명 또는 IP 주소로 표현됨
- 포트번호: 웹 서버 내의 서비스 포트번호. 생략 시에는 디폴트 포트번호로, http는 80을, https는 443을 사용
- 경로: 파일이나 애플리케이션 경로를 의미
- 쿼리스트링: 질의 문자열로, 앰퍼샌드(&)로 구분된 이름=값 쌍 형식으로 표현한다.
- 프라그먼트: 문서 내의 앵커 등 조각을 지정

### URL을 바라보는 측면

URL은 웹 클라이언트에서 호출한다는 시점에서 보면, 웹 서버에 존재하는 애플리케이션에 대한 API(Application Programming Interface)라고 할 수 있다. 웹 프로그래밍 기술의 발전 과정을 살펴보면, 이러한 API의 명명 규칙을 정하는 방법을 두 가지로 분류할 수 있다. 하나는 URL을 RPC(Remote Procedure Call)로 바라보는 방식이고, 다른 하나는 REST(Representational State Transfer)로 바라보는 방식이다.

RPC란 클라이언트가 네트워크상에서 원격에 있는 서버가 제공하는 API 함수를 호출하는 방식이다. RPC 방식에서는 URL 경로의 대부분이 동사가 된다. RPC 방식은 웹 개발 초기부터 사용된 방식으로, 다음에 설명하는 REST 방식이 나오면서 사용 빈도가 줄어드는 추세지만, 여전히 많이 사용된다. RPC 방식은 다음과 같은 형태로 사용한다.

```
<http://blog.example.com/search?q=test&debug=true>
```

URL을 바라보는 또 한 가지 측면은 REST 방식이다. REST 방식이란 웹 서버에 존재하는 요소들을 모두 리소스라고 정의하고, URL을 통해 웹 서버의 특정 리소스를 표현한다는 개념이다. 리소스는 시간이 지남에 따라 상태(state)가 변할 수 있기 때문에 클라이언트와 서버 간에 데이터의 교환을 리소스 상태의 교환(Representational State Transfer)으로 간주하고 있다. 그리고 중요한 점은 리소스에 대한 조작을 GET, POST, PUT, DELETE 등의 HTTP 메소드로 구분한다는 점이다.

이와 같은 REST 방식으로 바라본다면, 웹 클라이언트에서 URL을 전송하는 것이 웹 서버에 있는 리소스 상태에 대한 데이터를 주고 받는 것으로 간주될 수 있다. REST 방식을 다음과 같은 형태로 사용한다.

```
<http://blog.example.com/search/test>
```

### 간편 URL

간편 URL은 쿼리스트링 없이 경로만 가진 간단한 구조의 URL을 의미한다. 검색 엔진의 처리를 최적화하기 위해 생겨난 간편한 URL은 URL을 입력하거나 기억하기 쉽다는 부수적인 장점도 있어, 검색 엔진 최적화 URL 또는 사용자 친화적 URL이라고 부르기도 한다.

[기존 URL과 간편 URL 간의 비교를 위한 대응 예시](https://www.notion.so/e6124993e1184310a0049e83d0bcb8d0)

## 웹 애플리케이션 서버(나중에 더 자세하게)

웹 클라이언트(보통은 웹 브라우저)의 요청을 받아서 처리하는 서버를 통칭하여 웹 서버라고 부르기도 하지만, 좀 더 세분화하면, 웹 서버와 웹 애플리케이션 서버로 분류할 수 있다.

[웹 서버와 웹 애플리케이션 서버 구분](https://www.notion.so/5552a98140644322a933a744ce76b395)

이 두 개의 서버가 어떻게 다른지, 또 웹 애플리케이션 서버가 무엇인지를 이해하기 위해서는 웹 서버 기술의 발전 과정을 알아볼 필요가 있다.

keyword: CGI 프로그램, 스크립트 엔진, 데몬 프로그램, 웹 애플리케이션

### 정적 페이지 vs 동적 페이지

정적 페이지란 누가, 언제 요구하더라도 항상 같은 내용을 표시하는 웹 페이지이다. 정적 페이지들은 해당 웹 서비스의 제공자가 사전에 준비하여 서버 측에 배치한 것으로, 동일한 리소스(URL)의 요청에 대해서는 항상 동일한 내용의 페이지를 반환한다. 주로 HTML, 자바스크립트, CSS, 이미지만으로 이루어진 페이지가 해당된다.

동적페이지란 동일한 리소스의 요청이라도 누가, 언제, 어떻게 요구했는지에 따라 각각 다른 내용이 반환되는 페이지를 말한다. 예를 들면 현재 시각을 보여주는 페이지나 온라인 쇼핑 사이트에서 사용자마다 다른 카트 내용을 보여주는 페이지 등이 있다.

정적(static), 동적(dynamic)이란 용어는 사용자가 페이지를 요청하는 시점에 페이지의 내용이 유지되는가 또는 변경되는가를 구분해주는 용어이다. 동적 페이지에는 프로그래밍 코드가 포함되어 있어서 페이지 요청 시점에 HTML 문장을 만들어내는 것이다.

점차 동적 페이지에 대한 요구사항이 생기고, 필요한 데이터를 저장하고 꺼내오는 등의 데이터베이스 처리에 대한 요구가 많아짐에 따라 웹 서버와는 다른 별도의 프로그램이 필요하게 되었다. 이러한 별도의 프로그램과 웹 서버 사이에 정보를 주고받는 규칙을 정의한 것이 CGI(Common Gateway Interface) 규격이다.

### CGI 방식의 단점

전통적인 CGI 방식은 웹 서버가 C,  C++, Perl, PHP, Python 등으로 만들어진 CGI 프로그램을 직접 호출하여 개별 프로세스를 생성하는 방식이다.

하지만 CGI 방식은 각각의 클라이언트 요청에 대하여 독립적인 별도의 프로세스가 생성되기 때문에 요청이 많아질수록 프로세스가 많아지고, 프로세스가 많아질수록 비례적으로 프로세스가 점유하는 메모리 요구량도 커져서 시스템에 많은 부하를 주는 요인이 된다. 이런 이유로 CGI 방식을 거의 사용하지 않고 있으며, 이러한 단점을 해결하기 위해 대안책으로 여러 가지 기술이 등장하였다.

### CGI 방식의 대안 기술

1. 스크립트 엔진
2. 데몬

### 애플리케이션 서버 방식

애플리케이션 서버 방식은 웹 서버가 직접 프로그램을 호출하기보다는 웹 애플리케이션 서버를 통해서 간접적으로 웹 애플리케이션 프로그램을 실행한다. 웹 애플리케이션 서버는 애플리케이션 프로그램의 실행 결과를 웹 서버에 전달해주며, 웹 서버는 웹 애플리케이션 서버로부터 전달받은 응답 결과를 웹 클라이언트에 전송한다.

### 웹 서버와의 역할 구분

...