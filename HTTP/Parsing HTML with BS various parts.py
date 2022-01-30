import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrive all anchor tags
tags = soup('a')
for tag in tags:
    print('TAG: ', tag)
    print('URL: ', tag.get('href', None))
    print('Contents: ', tag.contents[0])
    print('Attrs: ', tag.attrs)