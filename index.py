#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
print("Content-Type: text/html")    # HTML is following
print()
import cgi # URL의 query string을 입력 값으로 웹애플리케이션으로 끌어오는 방법
form = cgi.FieldStorage()
if 'id' in form:
  pageId = form["id"].value
else:
  pageId = 'welcome'
  description = 'hello, web'  # 이라는 것이 id 값이 있는 경우에는 처리되지 않기 때문에 오류가 생긴다.
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))