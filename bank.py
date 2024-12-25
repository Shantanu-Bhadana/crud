from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Combobox,Treeview,Style,Scrollbar
from tkinter import messagebox
from time import strftime
import time as tt
import re
import sqlite3
try:
    conobj=sqlite3.connect(database="banking.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table accounts(acn_no integer primary key autoincrement,acn_user text,acn_pass text,acn_father text,acn_dob text,acn_type text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_surname text,)")
    curobj.execute("create table txns(txn_acn_no int,txn_amt float,txn_type text,txn_update_bal float,txn_date text)")
    print("tables created")
except:
    print("something went wrong,might be tables already exist")
conobj.close()




win=Tk()
win.state("zoomed")
win.configure(bg='White')

title=Label(win,text="Bank Automation",font=('garamond',60,'bold','underline'),bg='White')
title.pack()
win.title('clock')
def time():
    string=strftime('%A %b %d,%Y\n%H:%M:%S  %p')
    lbl.configure(text=string)
    lbl.after(1000,time)
    
lbl=Label(win,font=('garamond',16,'bold'),background='white',foreground='purple')
lbl.place(relx=.85,rely=.075)
time()
def xxx_screen():
    xx=Frame(win)
    xx.configure(bg='blue')
    xx.place(relx=0,rely=.145,relwidth=1,relheight=.005)


def home_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    
    def home_click():
        frm.destroy
        open_account()
        
    def recoverpass_click():
        frm.destroy
        recoverpass_screen()
    def login_click():
        acn=acn_entry.get()
        pwd=pass_entry.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showerror("Login","Empty fields are not allowed")
            return
        elif not acn.isdigit():
            messagebox.showwarning("Login","Incorrect ACN")
            return
        else :
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from accounts where acn_no=? and acn_pass=?",(acn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            
            if tup==None:
                messagebox.showinfo("login","invalid ACN/PASS")
            else:
                global uname,uacn
                uacn=tup[0]
                uname=tup[1]
                frm.destroy
                welcome_screen()
        
    def clear():
        acn_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        acn_entry.focus()
        
   # acn_lbl=Label(frm,text='ACN NO.',font=('arial',20,'bold'),bg='pink',fg='black')    
    #acn_lbl.place(relx=.55,rely=.1)
    
    def on_enter(e):
        acn_entry.delete(0,"end")
    def on_leave(e):
        name=acn_entry.get()
        if name=='':
            acn_entry.insert(0,'Account Number')
    
    
    acn_entry=Entry(frm,font=('arial',15),bd=7,bg='pink',fg='black',border=0)
    acn_entry.insert(0,'Account Number')
    acn_entry.bind('<FocusIn>',on_enter)
    acn_entry.bind('<FocusOut>',on_leave)
    acn_entry.place(relx=.65,rely=.1)
    #acn_entry.focus()
    
    #pass_lbl=Label(frm,text='Password',font=('arial',20,'bold'),bg='pink',fg='black')    
    #pass_lbl.place(relx=.55,rely=.3)
    
    def on_enter(e):
        pass_entry.delete(0,"end")
    def on_leave(e):
        name=pass_entry.get()
        if name=='':
            pass_entry.insert(0,'Password')
    
    pass_entry=Entry(frm,font=('arial',15,'bold'),bd=7,show="*",bg='pink',fg='black',border=0)
    pass_entry.insert(0,'Password')
    pass_entry.bind('<FocusIn>',on_enter)
    pass_entry.bind('<FocusOut>',on_leave)
    pass_entry.place(relx=.65,rely=.3)
    
    btn_login=Button(frm,command=login_click,text="Login",width=14,font=('arial',20,'bold'),bd=7,bg='blue',fg='white')
    btn_login.place(relx=.65,rely=.57)
    
    btn_clear=Button(frm,command=clear,text="Clear",font=('arial',20,'underline'),bd=0,bg='pink',fg='blue')
    btn_clear.place(relx=.91,rely=.61)  
    
    btn_new=Button(frm,command=home_click,width=14,text="Create Account",font=('Helvetica 9 italic',20,'underline'),bd=0,bg='pink',fg='blue')
    btn_new.place(relx=.82,rely=.81)
    
    btn_recpass=Button(frm,command=recoverpass_click,width=14,text="Forget Password",font=('silkscreen',20,'underline'),bd=0,bg='pink',fg='blue')
    btn_recpass.place(relx=.82,rely=.42)
    
def open_account():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    name_lbl=Label(frm,text='Name',font=('arial',15,'bold'),bg='pink',fg='black')    
    name_lbl.place(relx=.05,rely=.21)
    
    name_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    name_entry.place(relx=.15,rely=.21)
    name_entry.focus()
    
    pass_lbl=Label(frm,text='Password',font=('arial',15,'bold'),bg='pink',fg='black')    
    pass_lbl.place(relx=.57,rely=.68)
    
    pass_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    pass_entry.place(relx=.67,rely=.68)
    
    con_pass_lbl=Label(frm,text='Confirm Pass',font=('arial',15,'bold'),bg='pink',fg='black')    
    con_pass_lbl.place(relx=.57,rely=.79)
    
    con_pass_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    con_pass_entry.place(relx=.67,rely=.79)
    
    dob_lbl=Label(frm,text='D.O.B',font=('arial',15,'bold'),bg='pink',fg='black')    
    dob_lbl.place(relx=.05,rely=.33)
    
    dob_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    dob_entry.place(relx=.15,rely=.33)
    
    email_lbl=Label(frm,text='Email',font=('arial',15,'bold'),bg='pink',fg='black')    
    email_lbl.place(relx=.05,rely=.57)
    
    email_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    email_entry.place(relx=.15,rely=.57)
    
    mob_lbl=Label(frm,text='Mob',font=('arial',15,'bold'),bg='pink',fg='black')    
    mob_lbl.place(relx=.05,rely=.45)
    
    mob_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    mob_entry.place(relx=.15,rely=.45)
    
    father_lbl=Label(frm,text='Father N',font=('arial',15,'bold'),bg='pink',fg='black')    
    father_lbl.place(relx=.05,rely=.68)
    
    father_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    father_entry.place(relx=.15,rely=.68)
    
    add_lbl=Label(frm,text='Address',font=('arial',15,'bold'),bg='pink',fg='black')    
    add_lbl.place(relx=.05,rely=.79)
    
    add_entry=Text(frm, height = 6,width =28,bg = "white",bd=7)
    add_entry.place(relx=.15,rely=.79)
    
    #pass_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    #pass_entry.place(relx=.6,rely=.65)
    
    acntype_lbl=Label(frm,text='Acntype',font=('arial',15,'bold'),bg='pink',fg='black')    
    acntype_lbl.place(relx=.57,rely=.57)
    
    style=ttk.Style()
    style.theme_use('clam')
    style.configure("test1.TCombobox",fieldbackground="white")
    acntype_cb=ttk.Combobox(frm,font=('arial',15,'bold'),values=['saving','current','salary','fixed depoist'],style="test1.TCombobox")
    acntype_cb.current(0) # by default show 0 index value 'saving'
    acntype_cb.place(relx=.67,rely=.57)
    
    surname_lbl=Label(frm,text="Surname",font=('arial',15,'bold'),bg='pink',fg='black')
    surname_lbl.place(relx=.57,rely=.21)
 
    surname_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    surname_entry.place(relx=.67,rely=.21)
    
    gender_lbl=Label(frm,text="Gender",font=('arial',15,'bold'),bg='pink',fg='black')
    gender_lbl.place(relx=.57,rely=.33)
    
    gender_entry=Checkbutton(frm,text="Male",bg='pink')
    gender_entry.place(relx=.67,rely=.33)
    
    gender1_entry=Checkbutton(frm,text="Female",bg='pink')
    gender1_entry.place(relx=.73,rely=.33)
    
    gender2_entry=Checkbutton(frm,text="Others",bg='pink')
    gender2_entry.place(relx=.79,rely=.33)
    
    adhar_lbl=Label(frm,text="Adhar No.",font=('arial',15,'bold'),bg='pink',fg='black')
    adhar_lbl.place(relx=.57,rely=.45)
    
    adhar_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    adhar_entry.place(relx=.67,rely=.45)
    
    def open_click():
        name=name_entry.get()
        dob=dob_entry.get()
        email=email_entry.get()
        mob=mob_entry.get()
        father=father_entry.get()
        #add=add_entry.get()
        acntype=acntype_cb.get()
        bal=0
        surname=surname_entry.get()
        #gender=gender_entry.get()
        adhar=adhar_entry.get()
        opendate=tt.ctime()   
        if pass_entry.get()==con_pass_entry.get():
            pwd=pass_entry.get()
            cpwd=con_pass_entry.get()
        else:
            messagebox.showerror("Create Account","Password not match")
            return
        
        if len(name)==0 or len(pwd)==0 or len(email)==0 or len(mob)==0 or len(dob)==0 or len(father)==0 or len(adhar)==0:
            messagebox.showerror("Open Account","Empty fields are not allowed")
            return
        elif not re.fullmatch("[a-zA-Z0-9._]+@[a-zA-Z]+[.][a-zA-Z]+",email):
            messagebox.showerror("Open Account","email is not correct")
            return 
        elif not re.fullmatch("[6-9][0-9]{9}",mob):
            messagebox.showerror("Open Account","Mobile no. is not correct")
            return
        elif not re.fullmatch("[a-zA-Z]+",name):
            messagebox.showerror("Create Account","Digit and symbol not allow")
            return
        elif not re.fullmatch("[a-zA-Z]+",father):
            messagebox.showerror("Create Account","Digit and symbol not allow")
            return
        elif not re.fullmatch("[0-9]{4}[-]+[0-9]{4}[-]+[0-9]{4}",adhar):
            messagebox.showwarning("Create Account","Incorrect Adhar Number")
            return
       #elif not re.fullmatch("[0-9]{2}[/]+[0-9]{2}+[0-9]{4}",dob):
       #    messagebox.showwarning("Create Account","Incorrect DOB")
       #    return
            
        
        import sqlite3
        conobj=sqlite3.connect(database='banking.sqlite')
        curobj=conobj.cursor()
        curobj.execute("insert into accounts(acn_user,acn_pass,acn_father,acn_dob,acn_type,acn_email,acn_mob,acn_bal,acn_opendate,acn_surname) values(?,?,?,?,?,?,?,?,?,?)",(name,pwd,father,dob,acntype,email,mob,bal,opendate,surname))
        conobj.commit()
        curobj.close()
        curobj=conobj.cursor()
        curobj.execute("select max(acn_no) from accounts")
        tup=curobj.fetchone()
        conobj.close()
        messagebox.showinfo("Open Account",f"Your Account is Opend with ACN:{tup[0]}")
        
        name_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        dob_entry.delete(0,"end")
        father_entry.delete(0,"end")
        email_entry.delete(0,"end")
        mob_entry.delete(0,"end")
        surname_entry.delete(0,"end")
        #gender_entry.delete(0,"end")
        #gender1_entry.delete(0,"end")
        add_entry.delete("1.0","end")
        pass_entry.delete(0,"end")
        con_pass_entry.delete(0,"end")
        adhar_entry.delete(0,"end")
        name_entry.focus()
        
          
    
    
    def home_click():
        frm.destroy
        home_screen()
    
    btn_back=Button(frm,command=home_click,text="BACK",font=('arial',15,'bold'),bd=6,bg='black',fg='white')
    btn_back.place(relx=0,rely=0)
    
    btn_open=Button(frm,command=open_click,text="OPEN",width=7,font=('arial',20,'bold'),bd=6,bg='blue',fg='white')
    btn_open.place(relx=.38,rely=.87)
    
    def clear():
        name_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        dob_entry.delete(0,"end")
        father_entry.delete(0,"end")
        email_entry.delete(0,"end")
        mob_entry.delete(0,"end")
        surname_entry.delete(0,"end")
        #gender_entry.delete(0,"end")
        #gender1_entry.delete(0,"end")
        add_entry.delete("1.0","end")
        pass_entry.delete(0,"end")
        con_pass_entry.delete(0,"end")
        adhar_entry.delete(0,"end")
        name_entry.focus()
        
    btn_clear=Button(frm,command=clear,text="Clear",font=('arial',20,'bold','underline'),bd=0,bg='pink',fg='white')
    btn_clear.place(relx=.56,rely=.9)

def recoverpass_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    
    def recover_db():
        acn_no=acn_entry.get()
        name=name_entry.get()
        mob=mob_entry.get()
        email=email_entry.get()
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_pass from accounts where acn_no=? and acn_user=? and acn_mob=? and acn_email=?",(acn_no,name,mob,email))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showerror("Recover pass","Account does not exist")
        else:
            messagebox.showinfo("Recover Pass",f"Your Password :{tup[0]}")
            acn_entry.delete(0,"end")
            name_entry.delete(0,"end")
            mob_entry.delete(0,"end")
            email_entry.delete(0,"end")
        acn_entry.focus()
    def recover_clear():
        acn_entry.delete(0,"end")
        name_entry.delete(0,"end")
        mob_entry.delete(0,"end")
        email_entry.delete(0,"end")
        acn_entry.focus()
    
    def home_click():
        frm.destroy
        home_screen()
    
    btn_back=Button(frm,command=home_click,text="BACK",font=('arial',15,'bold'),bd=6,bg='black',fg='white')
    btn_back.place(relx=0,rely=0)
    
    acn_lbl=Label(frm,text='ACN NO.',font=('arial',15,'bold'),bg='pink',fg='black')    
    acn_lbl.place(relx=.15,rely=.25)
    
    acn_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    acn_entry.place(relx=.25,rely=.25)
    acn_entry.focus() #cursor blink
    
    name_lbl=Label(frm,text='Name',font=('arial',15,'bold'),bg='pink',fg='black')    
    name_lbl.place(relx=.15,rely=.4)
    
    name_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    name_entry.place(relx=.25,rely=.4)
    
    mob_lbl=Label(frm,text='Mob',font=('arial',15,'bold'),bg='pink',fg='black')    
    mob_lbl.place(relx=.6,rely=.25)
    
    mob_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    mob_entry.place(relx=.7,rely=.25)
   
    email_lbl=Label(frm,text='Email',font=('arial',15,'bold'),bg='pink',fg='black')    
    email_lbl.place(relx=.6,rely=.4)
    
    email_entry=Entry(frm,font=('arial',15,'bold'),bd=7)
    email_entry.place(relx=.7,rely=.4)
    
      
    btn_recover=Button(frm,command=recover_db,text="Recover",font=('arial',20,'bold'),bd=6,bg='blue',fg='white')
    btn_recover.place(relx=.4,rely=.75)
    
    btn_clear=Button(frm,command=recover_clear,text="Clear",font=('arial',20,'bold'),bd=6,bg='blue',fg='white')
    btn_clear.place(relx=.55,rely=.75)

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
      
    def home_click():
        res=messagebox.askquestion("Question","Do you want to exit from application")
        if res=='yes':
            frm.destroy
            home_screen()
    
    def update_screen():
        
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def home_click():
            ifrm.destroy
            welcome_screen()
        
        def update_db():
            name=name_entry.get()
            pwd=pass_entry.get()
            mob=mob_entry.get()
            email=email_entry.get()
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_user=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?",(name,pwd,email,mob,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Profile","Profile Updated")
            frm.destroy()
            global uname
            uname=name
            welcome_screen()
            
            
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn_no=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        
        title_lbl=Label(ifrm,text='This is update screen',font=('arial',20,'bold'),bg='white',fg='blue')    
        title_lbl.pack()
        
        name_lbl=Label(ifrm,text='Name',font=('arial',20,'bold'),bg='white',fg='blue')    
        name_lbl.place(relx=.08,rely=.2)
        
        name_entry=Entry(ifrm,font=('arial',20,'bold'),bd=7,width=10)
        name_entry.place(relx=.25,rely=.2)
        name_entry.insert(0,tup[1])
        
        pass_lbl=Label(ifrm,text='Password',font=('arial',20,'bold'),bg='white',fg='blue')    
        pass_lbl.place(relx=.08,rely=.4)
        
        pass_entry=Entry(ifrm,font=('arial',20,'bold'),bd=7,width=10)
        pass_entry.place(relx=.25,rely=.4)
        pass_entry.insert(0,tup[2])
        
        email_lbl=Label(ifrm,text='Email',font=('arial',20,'bold'),bg='white',fg='blue')    
        email_lbl.place(relx=.5,rely=.2)
        
        email_entry=Entry(ifrm,font=('arial',20,'bold'),bd=7,width=10)
        email_entry.place(relx=.6,rely=.2)
        email_entry.insert(0,tup[9])
        
        mob_lbl=Label(ifrm,text='Mob',font=('arial',20,'bold'),bg='white',fg='blue')    
        mob_lbl.place(relx=.5,rely=.4)
        
        mob_entry=Entry(ifrm,font=('arial',20,'bold'),bd=7,width=10)
        mob_entry.place(relx=.6,rely=.4)
        mob_entry.insert(0,tup[10])
        
        btn=Button(ifrm,command=home_click,text="back",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.6,rely=.7)
        
        btn=Button(ifrm,command=update_db,text="Update",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.7,rely=.7)
        
    def balance_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def home_click():
            ifrm.destroy
            welcome_screen()
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_no,acn_bal,acn_opendate from accounts where acn_no=?",(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        title_lbl=Label(ifrm,text='This is Check Balance screen',font=('arial',20,'bold'),bg='white',fg='blue')    
        title_lbl.pack()   
        
        acn_lbl=Label(ifrm,text=f'Account No \t {tup[0]}',font=('arial',15,'bold'),bg='white',fg='blue')
        acn_lbl.place(relx=.2,rely=.2)
        
        bal_lbl=Label(ifrm,text=f'Available Bal \t {tup[1]}',font=('arial',15,'bold'),bg='white',fg='blue')
        bal_lbl.place(relx=.2,rely=.3)
        
        opendate_lbl=Label(ifrm,text=f'ACN open date\t {tup[2]}',font=('arial',15,'bold'),bg='white',fg='blue')
        opendate_lbl.place(relx=.2,rely=.4)
        
        btn=Button(ifrm,command=home_click,text="back",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=0,rely=0)
        
        
    def deposit_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def home_click():
            ifrm.destroy
            welcome_screen()
        
        def deposit_db():
            amt=float(amt_entry.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()

            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_bal=acn_bal+? where acn_no=?",(amt,uacn))
            curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Cr.',bal+amt,tt.ctime()))
            conobj.commit()
            conobj.close()

            messagebox.showinfo("Deposit Amt",f"{amt} deposited ")
        
        title_lbl=Label(ifrm,text='This is Deposit Screen',font=('arial',20,'bold'),bg='white',fg='blue')    
        title_lbl.pack()
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.2)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.2)
        amt_entry.focus()
        
        btn=Button(ifrm,command=home_click,text="back",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.6,rely=.35)
        
        btn=Button(ifrm,command=deposit_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.35)
        
    def withdrawal_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def home_click():
            ifrm.destroy
            welcome_screen()
        
        def withdraw_db():
            amt=float(amt_entry.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            
            tup=curobj.fetchone()
            bal=tup[0]
            curobj.close()
            if bal>=amt:
                curobj=conobj.cursor()
                curobj.execute("update accounts set acn_bal=acn_bal-? where acn_no=?",(amt,uacn))
                curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Db.',bal-amt,tt.ctime()))
                conobj.commit()
                conobj.close()
    
                messagebox.showinfo("Withdraw Amt",f"{amt} withdrawn ")
            else:
                messagebox.showinfo("Withdraw Amt","Insufficient Bal")
        
        title_lbl=Label(ifrm,text='This is Withdrawal Screen',font=('arial',20,'bold'),bg='white',fg='blue')    
        title_lbl.pack()
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.2)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.2)
        amt_entry.focus()
        
        btn=Button(ifrm,command=withdraw_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.35)
        
        btn=Button(ifrm,command=home_click,text="back",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.6,rely=.35)
        
    def transfer_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=0,relwidth=1,relheight=1)
        
        def home_click():
            ifrm.destroy
            welcome_screen()
        
        def transfer_db():
            amt=float(amt_entry.get())
            toacn=to_entry.get()
            
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(uacn,))
            tup=curobj.fetchone()
            bal_frm=tup[0]
            curobj.close()

            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(toacn,))
            tup=curobj.fetchone()
            bal_to=tup[0]
            curobj.close()
            
            curobj=conobj.cursor()
            curobj.execute("select acn_no from accounts where acn_no=?",(toacn,))
            tup1=curobj.fetchone()
            curobj.close()
            if tup1==None:
                messagebox.showerror("Transfer",f"To ACN {toacn} does not exist !")
                
            else:
                if bal_frm>=amt:
                    curobj=conobj.cursor()
                    curobj.execute("update accounts set acn_bal=acn_bal-? where acn_no=?",(amt,uacn))
                    curobj.execute("update accounts set acn_bal=acn_bal+? where acn_no=?",(amt,toacn))
                    
                    curobj.execute("insert into txns values(?,?,?,?,?)",(uacn,amt,'Db.',bal_frm-amt,'15march'))
                    curobj.execute("insert into txns values(?,?,?,?,?)",(toacn,amt,'Cr.',bal_to+amt,'15march'))
                   
                    conobj.commit()
                    conobj.close()
        
                    messagebox.showinfo("Transfer Amt",f"{amt} transfered to ACN {toacn} ")
                else:
                    messagebox.showwarning("Withdraw Amt","Insufficient Bal")
        
        
        title_lbl=Label(ifrm,text='This is Transfer screen',font=('arial',20,'bold'),bg='white',fg='blue')    
        title_lbl.pack()
        
        to_lbl=Label(ifrm,text='TO',font=('arial',20,'bold'),bg='white',fg='blue')
        to_lbl.place(relx=.28,rely=.2)
        
        to_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        to_entry.place(relx=.4,rely=.2)
        
        amt_lbl=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white',fg='blue')
        amt_lbl.place(relx=.28,rely=.35)
        
        amt_entry=Entry(ifrm,font=('arial',20,'bold'),border=7)
        amt_entry.place(relx=.4,rely=.35)
        
        btn=Button(ifrm,command=transfer_db,text="Submit",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.4,rely=.5)
        
        btn=Button(ifrm,command=home_click,text="back",font=('arial',20,'bold'),border=7,bg='powder blue')
        btn.place(relx=.6,rely=.5)
        
        
    def txnhist_screen():
        iifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        iifrm.configure(bg='white')
        iifrm.place(relx=0,rely=0,relwidth=1,relheight=.11)
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=0,rely=.11,relwidth=1,relheight=.89)
        
        def home_click():
            ifrm.destroy
            welcome_screen()

        title_lbl=Label(ifrm,text='This is Transaction History Screen',font=('arial',20,'bold'),bg='white',fg='purple')
        title_lbl.pack()
        
        btn=Button(iifrm,command=home_click,text="back",font=('arial',20,'bold'),width=4,border=7,bg='powder blue')
        btn.place(relx=0,rely=0)

        tv=Treeview(ifrm)
        tv.place(x=0,y=0,relheight=1,relwidth=1)
        
        style = Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='black')
        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(relx=.98,y=0,relheight=1)
        
        tv['columns']=('Txn date','Txn amount','Txn type','Updated bal')
        
        tv.column('Txn date',width=150,anchor='c')
        tv.column('Txn amount',width=100,anchor='c')
        tv.column('Txn type',width=100,anchor='c')
        tv.column('Updated bal',width=100,anchor='c')

        tv.heading('Txn date',text='Txn date')
        tv.heading('Txn amount',text='Txn amount')
        tv.heading('Txn type',text='Txn type')
        tv.heading('Updated bal',text='Updated bal')
        
        tv['show']='headings'

        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select txn_date,txn_amt,txn_type,txn_update_bal from txns where txn_acn_no=?",(uacn,))
        for row in curobj:
            tv.insert("","end",values=(row[0],row[1],row[2],row[3]),tags='ft')
            tv.tag_configure('ft',font=('',12))
        conobj.close()
        
    btn_logout=Button(frm,command=home_click,text="Logout",width=7,font=('arial',20,'bold'),bd=6)
    btn_logout.place(relx=.91,rely=0)
    
    wel_lbl=Label(frm,text=f'Welcome,{uname}',font=('arial',20,'bold'),bg='pink',fg='blue')    
    wel_lbl.place(relx=0,rely=0)
    
    btn_update=Button(frm,command=update_screen,text="Update Profile",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_update.place(relx=.1,rely=.13)
    
    btn_bal=Button(frm,command=balance_screen,text="Check Balance",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_bal.place(relx=.43,rely=.13)
    
    btn_deposit=Button(frm,command=deposit_screen,text="Deposit",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_deposit.place(relx=.76,rely=.13)
    
    btn_withdrawal=Button(frm,command=withdrawal_screen,text="Withdrawal",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_withdrawal.place(relx=.1,rely=.58) 
    
    btn_transfer=Button(frm,command=transfer_screen,text="Transfer",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_transfer.place(relx=.43,rely=.58)
    
    btn_transaction=Button(frm,command=txnhist_screen,text="Transaction",width=12,height=4,font=('arial',20,'bold'),bd=6)
    btn_transaction.place(relx=.76,rely=.58)
home_screen()
xxx_screen()
win.mainloop()
