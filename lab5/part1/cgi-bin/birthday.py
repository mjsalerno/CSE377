#!/usr/bin/env python
import cgi

form = cgi.FieldStorage()
name = form.getfirst('name', 'empty')
name = cgi.escape(name)

print("Content-type: text/html\n")

print('''
<html>
    <head>
        <title>Happy Birthday!</title>
    </head>
    <body>
''')

print('Happy birthday to you.<br>')
print('Happy birthday to you.<br>')
print('Happy birthday dear ' + name + '<br>')
print('Happy birthday to you.<br>')

print('''
    </body>
</html>
''')
