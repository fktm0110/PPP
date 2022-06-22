from urllib.parse import urlparse, parse_qs
reqURL="http://203.250.133.87:8080/cgibin/test.cgi?name=hong+kildong&passwd=12%2E34"
r = urlparse(reqURL)
print(r)
q = parse_qs(r.query)
print(q)
name = q['name'][0]
passwd = q['passwd'][0]
print(name)
print(passwd)