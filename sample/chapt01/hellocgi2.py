#!/usr/bin/python3
import sys
import io
sys.stdout = io.TextIOWrapper( sys.stdout.buffer, encoding='utf-8' )

html = """
<html>
<head></head>
<body>
<h1>こんにちは、世界</h1>
</body>
</html>
"""

print( 'Content-type: text/html' )
print( '' )
print( html )
