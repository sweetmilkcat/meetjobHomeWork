# -*- coding: utf-8 -*-
"""
請使用python 程式來執行SQL相關東西

請建立一個資料庫: jobs

在這個資料庫中建立二個資料表
1. employee id,name,sex,tel,assume(日期)
2. works id,items,info,employeeid

由python 程式撰寫:
    使用者依輸入的方式填入:員工姓名、性別、電話後，程式新增到employee的資料表中
    
    使用者依輸入的方式填入:工作項目、工作詳述、對應的員工編號(id)
    
    使用者可以依員工id 來修改員工的電話及性別
    
    使用者可以依員工編號來查詢員工的基本資料
    
    使用者輸入員工編號，請印出員工姓名及工作項目、工作詳述 
"""
import db
import datetime

cursor=db.conn.cursor()
while (True):
    chooes=input("( 1:員工資料相關 2:工作項目相關 3:離開) :")
    if chooes == '1':
        while(True):
            empchooes=input("想做甚麼? (1:新增 2:修改性別及電話 3:查詢 4:刪除 5:回首頁) :")
            #新增
            if empchooes == '1':
                print("請新增員工資料:")
                empname= input("員工姓名:")
                sex =input("性別(M/F):")
                tel =input("請輸入連絡電話:")
                date= datetime.date.today()
                
                sql="select *from employee where name='{}'".format(empname)
                cursor.execute(sql)
                db.conn.commit()
                if cursor.rowcount ==0:                                
                    sql="insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(empname,sex,tel,date)           
                    cursor.execute(sql)
                    db.conn.commit()
                    print("新增成功!")
                    sql="select id from employee order by id desc limit 1"
                    cursor.execute(sql)
                    db.conn.commit()
                    data=cursor.fetchall()
                    empid=data[0][0]
                        
                    print("該員工編號為:",empid)
                else:
                    chooes=input("已有員工名稱已存在，是否繼續新增? Y/N :")
                    if chooes == "Y":
                        sql="insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(empname,sex,tel,date)           
                        cursor.execute(sql)
                        db.conn.commit()
                        print("新增成功!")
                        sql="select id from employee order by id desc limit 1"
                        cursor.execute(sql)
                        db.conn.commit()
                        data=cursor.fetchall()
                        empid=data[0][0]
                            
                        print("該員工編號為:",empid)
                    else:
                        continue
            #修改性別及電話    
            elif empchooes =='2':
                number=input("請輸入要修改員工的編號:")
                sql="select id from employee where id='{}'".format(number)
                cursor.execute(sql)
                db.conn.commit()
                if cursor.rowcount ==0:
                    print("輸入的編號不存在!請確認後再重新操作")
                else:
                    sex =input("請輸入要修改的性別:")
                    tel =input("請輸入要修改的電話:")
                    modifi_date=datetime.date.today()
                    sql="update employee set sex='{}',tel='{}',modified_date='{}' where id='{}'".format(sex,tel,modifi_date,number)
                    
                    cursor.execute(sql)
                    db.conn.commit()
                    print("修改完成，修改內容如下:")
                    sql="select id,name,sex,tel from employee where id='{}'".format(number)
                    cursor.execute(sql)
                    db.conn.commit()
                    emp=cursor.fetchall()
                    print("員工編號:{}，員工名稱:{}，性別:{}，電話:{}".format(emp[0][0],emp[0][1],emp[0][2],emp[0][3]))
            #查詢員工資訊
            elif empchooes =='3':
                print("目前的員工編號有:")
                sql="select id from employee"
                cursor.execute(sql)
                db.conn.commit()
                data=cursor.fetchall()
                for row in data:
                    print(row[0],end=',')
                empid=input("請輸入要查詢的員工編號:")
                sql="select * from employee where id='{}'".format(empid)
                cursor.execute(sql)
                db.conn.commit()
                thisemp=cursor.fetchall()
                print("員工編號:",thisemp[0][0])
                print("員工姓名:",thisemp[0][1])
                print("性別:",thisemp[0][2])
                print("連絡電話:",thisemp[0][3])
                print("建檔日期:",thisemp[0][4])
                print("修改日期:",thisemp[0][5])
            elif empchooes =='4':
                print("目前的員工編號有:")
                sql="select id from employee"
                cursor.execute(sql)
                db.conn.commit()
                data=cursor.fetchall()
                for row in data:
                    print(row[0],end=',')
                empid=input("請輸入要刪除的員工編號:")
                sql="delete from employee where id='{}'".format(empid)
                cursor.execute(sql)
                db.conn.commit()
                print("該員工資料已刪除!")
            elif empchooes =='5':
                break
            else :
                print("輸入錯誤請重新輸入!")
                continue
    elif chooes =='2':
        while (True):           
            workchooes=input("想做甚麼?(1:建立工作項目 2:查詢 3:回首頁) :")
            if workchooes == '1':
                items=input("工作項目:")
                info=input("工作詳述:")
                empid=input("請輸入員工編號:")
                date=datetime.date.today()
                sql="insert into works(items,info,employeeid,date) values('{}','{}','{}','{}')".format(items,info,empid,date)
                cursor.execute(sql)
                db.conn.commit()
                print("工作項目已建立!")
            elif workchooes =='2':
                print("目前的員工編號有:")
                sql="select id from employee"
                cursor.execute(sql)
                db.conn.commit()
                data=cursor.fetchall()
                for row in data:
                    print(row[0],end=',')
                empid=input("請輸入要查詢的員工編號:")
                sql="select e.name,w.items,w.info,w.date from employee as e inner join works as w where e.id=w.employeeid and e.id='{}'".format(empid)
                cursor.execute(sql)
                db.conn.commit()
                if cursor.rowcount ==0:
                    print("查無資料")
                else:
                    works=cursor.fetchall()
                    print("員工姓名:",works[0][0])
                    for row in works:
                            print("日期:",row[3])                            
                            print("工作項目:",row[1])
                            print("工作詳述:",row[2])
                            
            elif workchooes =='3':
                break
            else:
                print("輸入錯誤請重新輸入!")
    elif chooes =='3':
        break
    else :
        print("輸入錯誤請重新輸入!")
        continue
db.conn.close()


