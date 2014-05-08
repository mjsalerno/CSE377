#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
name = form.getfirst('name', 'empty')
name = cgi.escape(name)

print("Content-type: text/html")
print("\n")
print('''
<html>
<head>
<title>Hello Word - First CGI Program</title>
</head>
<body>
<h2>Hello Word! This is my first CGI program</h2>
</body>
</html>
''')

print(name)
