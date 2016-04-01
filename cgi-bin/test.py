#!/usr/bin/python

from datetime import datetime


html_body = """
<html><body>
{0.year:d}/{0.month:d}/{0.day:d} {0.hour:d}:{0.minute:d}:{0.second:d}
</body></html>"""

now = datetime.now()
print("Content-type: text/html\n")
print(html_body.format(now))
