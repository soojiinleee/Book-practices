#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print("Content-Type: text/plain")
print()

print("Welcom... CGI Scripts")
print("name is", name)
print("email is", email)
print("url is", url)
