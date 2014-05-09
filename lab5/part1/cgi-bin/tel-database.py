#!/usr/bin/env python
import cgi
import shelve

form = cgi.FieldStorage()

op = form.getfirst('op', 'noop')
name = cgi.escape(op)

key = form.getfirst('key', None)
name = cgi.escape(op)

val = form.getfirst('val', None)
name = cgi.escape(op)

phonebook = shelve.open('phonebook')

print("Content-type: text/html\n")

print('''
<html>
    <head>
        <title>Telephone Database</title>
    </head>
    <body>
''')

if((op == 'noop')):
    print('You must select an opperation')
elif(op == 'insert'):
    phonebook[key] = val
    print('Inserted<br>')
    print('Key: ' + key + '<br>')
    print('Val: ' + val + '<br>')
elif(op == 'delete'):
    try:
        del phonebook[key]
        print('Deleted<br>')
        print('Key: ' + key + '<br>')
        print('Val: ' + val + '<br>')
    except KeyError:
        print('Sorry, could not find key: ' + key + '<br>')
elif(op == 'find'):
    if((val is None) and (key is None)):
        print('Sorry but you must fill out the Key/Search or Value feild.<br>')
    elif((val is None) or ((val is not None) and (key is not None))):
        try:
            data = phonebook[key]
            print('Find<br>')
            print('Key: ' + key + '<br>')
            print('Val: ' + phonebook[key] + '<br>')
        except KeyError:
            print('Sorry, could not find key: ' + key + '<br>')
    elif(key is None):
        found = False
        for key in phonebook:
            if(phonebook[key] == val):
                print('Find<br>')
                print('Key: ' + key + '<br>')
                print('Val: ' + phonebook[key] + '<br>')
                found = True
                break
        if(not found):
            print('Sorry, could not find value: ' + val + '<br>')
elif(op == 'print'):
    for key in phonebook:
        print('Key: ' + key + '<br>')
        print('Val: ' + phonebook[key] + '<br><br>')
else:
    print('Sorry but there is no opperation called ' + op + '<br>')

print('''
        <form method="get" action="../tel-database.html">
            <input type="submit" id="submit_btn" value="Back">
        </form>
    </body>
</html>
''')
phonebook.close()
