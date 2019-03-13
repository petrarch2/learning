#!/usr/bin/python3

html = """
<html>
<head></head>
<body>
<h1>Hello, CGI</h1>
</body>
</html>
"""

print( 'Content-type: text/html' )
print( '' )
print( html )
