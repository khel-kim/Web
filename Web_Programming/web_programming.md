# 웹 프로그래밍의 이해

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