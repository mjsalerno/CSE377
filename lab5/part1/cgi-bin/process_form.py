import cgi

form = cgi.FieldStorage()  # instantiate only once!

# FieldStorage.getfirst(name[, default])
# This method always returns only one value associated with form field name.
# The method returns only the first value in case that more values were
# posted under such name. Please note that the order in which the values
# are received may vary from browser to browser and should not be counted
# on. If no such form field or value exists then the method returns the
# value specified by the optional parameter default. This parameter defaults
# to None if not specified

name = form.getfirst('name', 'empty')

# Avoid script injection escaping the user input
name = cgi.escape(name)

# Triple-quotes
# Strings can be surrounded in a pair of matching triple-quotes: """ or '''
# either double quotes or single quotes can be used.
#
# backslash at end of the first line is needed, otherwise, a newline is read,
# which disturbs the HTTP protocol operation.
#
# The extra newline at the end of the second line is needed, which marks the
# end of HTTP header lines.
print
'''\
Content-Type: text/html\n
<html><body>
'''
print
'''
<p>The submitted name was "%s"</p>
</body></html>
''' % name
# Python formated output
# python use format % values for formated output. E.g., a format can be "%s"
# it will take the object, convert it to string, and print it. "%d" is used
# to output an integer decimal. "%f" is for floating point decimal numbers.
# see the "Coversion" table at the following site:
# http://docs.python.org/library/stdtypes.html#string-formatting-operations
