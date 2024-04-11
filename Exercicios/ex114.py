import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site OFFLINE')
else:
    print('Website ONLINE!')
    print(site.read)
