import pymysql
from tkinter import *

def getdata():
    us = u.get()
    ps = p.get()
    db = pymysql.connect('localhost','root','root','login')
    cr = db.cursor()
    q = """INSERT INTO user(Username,Password) VALUES(%s,%s);"""
    val = (us,ps)
    rwCount1 = cr.rowcount
    cr.execute(q,val)
    rwCount2 = cr.rowcount
    db.commit()
    cr.execute("SELECT * FROM user")
    for i in cr:
        print(i)
    if(rwCount1<rwCount2):
        messagebox.showinfo("Signup", "Signup Successful")
    else:
        messagebox.showinfo("Signup", "Signup Failed")
        
    cr.close()
    db.close()
    
def val():
    db = pymysql.connect('localhost','root','root','login')
    cr = db.cursor()
    us = u.get()
    ps = p.get()
    uq = """SELECT Username,Password FROM user WHERE Username = %s"""
    s = (us)
    cr.execute(uq,s)
    flg = 0
    for i in cr:
        if(i[0]==us and i[1]==ps):
            flg = 1
    if(us=='' or ps==''):
        messagebox.showinfo("Login","Please enter details")
    elif(flg==0):
        messagebox.showinfo("Login", "Login failed")
    else:
        messagebox.showinfo("Login", "Login successful")

window = Tk()
window.title("SignUp")

window.geometry('350x180')

Label(window,text="    ").grid(row=0)

Label(window,text=" ").grid(row=1,column=0)
Label(window,text='Username : ').grid(column=1,row=1)
u = Entry(window,width=25)
u.grid(column=2,row=1)

Label(window,text=" ").grid(row=2)
Label(window,text=" ").grid(row=3,column=0)
Label(window,text='Password : ').grid(column=1,row=3)
p = Entry(window,width=25,show='*')
p.grid(column=2,row=3)

Label(window,text=" ").grid(row=4)

Label(window,text="    ").grid(row=5,column=0)
SignUpbt = Button(window,text='SignUp',width=20,command=getdata)
SignUpbt.grid(column=1,row=5)

Loginbt = Button(window,text='Login',width=20,command=val)
Loginbt.grid(column=2,row=5)


window.mainloop()
