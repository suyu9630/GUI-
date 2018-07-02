#coding=utf-8
import MySQLdb
import tkinter as tk
from tkinter import * 
import struct
import sys
window = tk.Tk()
window.title("數據庫管理界面")
T=Text(window,width=150)###創建TEXT文本框用於顯示與提示
S=Scrollbar(window)
S.pack(side=LEFT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
c=tk.StringVar()#绑定Entry中的textvariable,全局,获取get()
d=tk.StringVar()#绑定Entry中的textvariable,全局,获取get()
e=tk.StringVar()
f=tk.StringVar()
g=tk.StringVar()
h=tk.StringVar()
i=tk.StringVar()
j=tk.StringVar()
k=tk.StringVar()
var=tk.StringVar()#選擇值
#connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
#这只是连接到了数据库，要想操作数据库需要创建游标。
window.attributes("-alpha", 1)#窗口透明化
##-------------------------------------------------------
db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# 使用execute方法执行SQL语句
#cursor.execute("SELECT VERSION()")
cursor.execute("use text3")
# 使用 fetchone() 方法获取一条数据
#data = cursor.fetchone()
#print ("Database version : %s " % data)
#sql = 'select 發生地點 from 交通事故'

###

def btn1_clicked():#查詢
    t=1
    X=e.get()
    print(X)
    db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
    cursor = db.cursor()
    cursor.execute("use text3")
    sql =( 'select * from 交通事故 where '+var.get()+' like'+"'%"+X+"%'"+'limit 2000')
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        T.insert(END,str(t)+'-')
        T.insert(END,row)
        T.insert(INSERT,'\n')
        t=t+1  
def btn3_clicked():#增加
    db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
    cursor = db.cursor()
    cursor.execute("use text3")
    X1=c.get()
    X2=d.get()
    X3=f.get()
    X4=g.get()
    if(len(X4)==0 or len(X3)==0 or len(X2)==0 or len(X1)==0):
        T.insert(END,'有插入字段為空，請重新輸入')
    else:
        sql =('INSERT INTO 交通事故 VALUES'+"('"+X1+"'"+","+"'"+X2+"'"+','+"'"+X3+"'"+","+"'"+X4+"'"+',"0"'+')')
        print(sql)
        cursor.execute(sql)
        db.commit()
        T.insert(END,'插入成功')
        T.insert(INSERT,'\n')
def btn2_clicked():#刪除
     db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
     cursor = db.cursor()
     cursor.execute("use text3")
     X5=h.get()
     if(len(X5)==0):
         T.insert(END,'輸入ID為空，請重新輸入')
     else:
         sql =('DELETE FROM 交通事故 WHERE id='+str(X5))
         cursor.execute(sql)
         db.commit()
         T.insert(END,'刪除成功')
         T.insert(INSERT,'\n')
def btn4_clicked():#修改
    db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
    cursor = db.cursor()
    cursor.execute("use text3")
    X6=i.get()#id
    X7=j.get()#條目名稱
    X8=k.get()#修改內容
    if(len(X6)==0 or len(X7)==0 or len(X8)==0):
        T.insert(END,'存在字段為空，請重新輸入')
    else:
        sql =('UPDATE 交通事故 SET '+X7+' = '+"'"+X8+"'"+' WHERE id = '+"'"+X6+"'")
        print(sql)
        cursor.execute(sql)
        db.commit()
        T.insert(END,'修改成功')
        T.insert(INSERT,'\n')
def btn5_clicked():#tkinker text清屏
    T.delete(0.0,END)
def btn6_clicked():#操作提示
    T.insert(END,'1.Columns的名稱，從左至右分別為"發生時間"，"發生地點","死亡受傷人數","車種","id"')
    T.insert(INSERT,'\n')
    T.insert(END,'2.若查詢字段為空則返回所有結果')
    T.insert(INSERT,'\n')
    T.insert(END,'3.查詢默認columns為發生地點')
def print_selection():#選擇按鈕，打印提示
    w.config(text='你已選擇查詢'+var.get(),bg='red')
def btn7_clicked():#顯示全部數據
    t=1
    db= MySQLdb.connect(
        user='root',
        passwd='123456',
        charset ='utf8'
        )
    cursor = db.cursor()
    cursor.execute("use text3")
    sql =( 'select * from 交通事故')
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        T.insert(END,str(t)+'-')
        T.insert(END,row)
        T.insert(INSERT,'\n')
        t=t+1
btn1=tk.Button(window,text='查詢',activebackground='yellow',fg='black',bg='#48D1CC',command=btn1_clicked)    
btn2=tk.Button(window,text='刪除',activebackground='yellow',fg='black',bg='#48D1CC',command=btn2_clicked)
btn3=tk.Button(window,text='增加',activebackground='yellow',fg='black',bg='#48D1CC',command=btn3_clicked)
btn4=tk.Button(window,text='修改',activebackground='yellow',fg='black',bg='#48D1CC',command=btn4_clicked)
btn5=tk.Button(window,text='清屏',activebackground='yellow',fg='black',bg='#48D1CC',command=btn5_clicked)
btn6=tk.Button(window,text='操作提示',activebackground='yellow',fg='black',bg='#48D1CC',command=btn6_clicked)
btn7=tk.Button(window,text='查看全部數據',activebackground='yellow',fg='black',bg='#48D1CC',command=btn7_clicked)
#GUI佈局
w= Label(window, text="查詢功能",fg='black')
w.pack(fill=tk.X)
R1=tk.Radiobutton(window,text='發生時間查詢',variable=var,value='發生時間',command=print_selection)
R2=tk.Radiobutton(window,text='發生地點查詢',variable=var,value='發生地點',command=print_selection)
R3=tk.Radiobutton(window,text='車種查詢',variable=var,value='車種',command=print_selection)
R4=tk.Radiobutton(window,text='id查詢',variable=var,value='id',command=print_selection)
R5=tk.Radiobutton(window,text='死亡受傷人數查詢',variable=var,value='死亡受傷人數',command=print_selection)
R1.pack()
R2.pack()
R3.pack()
R4.pack()
R5.pack()
entry=tk.Entry(window,textvariable=e)
entry.pack(fill=tk.X)
btn1.pack(fill=tk.X)
btn7.pack(fill=tk.X)
w1= Label(window, text="增加條目時間",fg='black')
w1.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=c)
entry.pack(fill=tk.X)
w2= Label(window, text="增加條目地點",fg='black')
w2.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=d)
entry.pack(fill=tk.X)
w3= Label(window, text="增加條目死亡受傷人數",fg='black')
w3.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=f)
entry.pack(fill=tk.X)
w4= Label(window, text="增加條目車種",fg='black')
w4.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=g)
entry.pack(fill=tk.X)
btn3.pack(fill=tk.X)
w5= Label(window, text="選擇刪除條目id(最後)",fg='black')
w5.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=h)
entry.pack(fill=tk.X)
btn2.pack(fill=tk.X)
w6= Label(window, text="請鍵入修改條目ID",fg='black')
w6.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=i)
entry.pack(fill=tk.X)
w7= Label(window, text="請鍵入修改欄位",fg='black')
w7.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=j)
entry.pack(fill=tk.X)
w8= Label(window, text="請鍵入修改內容",fg='black')
w8.pack(fill=tk.X)
entry=tk.Entry(window,textvariable=k)
entry.pack(fill=tk.X)
btn4.pack(fill=tk.X)
btn5.pack(fill=tk.X)
btn6.pack(fill=tk.X)
# 关闭数据库连接
db.close()
window.mainloop()
