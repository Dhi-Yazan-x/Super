from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess 
import os  # لاستعمال دالة os.startfile

pro = Tk()
pro.geometry('800x460+280+50')
pro.resizable(False, False)
pro.title('SUPERMARKET')
pro.iconbitmap('D:\\super\\super.ico')

title = Label(pro, text='Super Market', fg='#111111', bg='#00BFFF', font=('tajawal', 20, 'bold'))
title.pack(fill=X)

u1 = 'https://www.facebook.com/profile.php?id=61558542373743&mibextid=ZbWKwL'
u2 = 'https://whatsapp.com/channel/0029VaXsn2z6GcGEsUhGti1F'
u3 = 'https://youtube.com/@i2_i_2i?si=natUbtJmGiS-UBTJ'

def open1():
    webbrowser.open_new(u1)

def open2():
    webbrowser.open_new(u2)

def open3():
    webbrowser.open_new(u3)

def about1():
    messagebox.showinfo('المطور', 'ذي يزن ناصر الكعدي')

def about2():
    messagebox.showinfo('المشروع', 'مشروع سوبر ماركت في بايثون إشراف الدكتور حسان الخميسي')

def login():
    messagebox.showinfo('تطوير', 'تحت التطوير')

def log():
    user = En1.get()
    passw = En2.get()
    if user == 'yazan' and passw == '1059' or user=='rakan' and passw=='123456':
        messagebox.showinfo('ترحيب', 'أهلاً وسهلاً بك بيانات صحيحة')
        open_next_file() 
    else:
        messagebox.showinfo('خطأ', 'البيانات غير صحيحة الرجاء المحاولة مره اخرى')

def open_next_file():
    subprocess.Popen(['python', 'D:\\super\\super1.py']) # استبدل هذا بمسار ملف super.py

def create_account():
    os.startfile('D:\\super\\Dhi-Yazan\\register.html')  # تأكد من المسار الصحيح للملف 

F1 = Frame(pro, width=230, height=415, bg='#0B2F3A')
F1.place(x=570, y=46)
Title1 = Label(F1, text='مشروع سوبر ماركت', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title1.place(x=65, y=10)
Title2 = Label(F1, text='المطور: ذي يزن الكعدي', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title2.place(x=40, y=50)
Title3 = Label(F1, text='وسائل الاتصال بنا', bg='#0B2F3A', fg='white', font=('tajawal', 12, 'bold'))
Title3.place(x=75, y=90)

B1 = Button(F1, text='حسابنا على الفيسبوك', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=open1)
B1.place(x=8, y=120)
B2 = Button(F1, text='قناتنا على الواتساب', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=open2)
B2.place(x=8, y=168)
B3 = Button(F1, text='قناتنا على اليوتيوب', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=open3)
B3.place(x=8, y=217)
B4 = Button(F1, text='لمحة عن المطور', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=about1)
B4.place(x=8, y=266)
B5 = Button(F1, text='لمحة عن المشروع', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=about2)
B5.place(x=8, y=315)
B6 = Button(F1, text='اغلاق البرنامج', width=23, fg='black', bg='#00BFFF', font=('tajawal', 12, 'bold'),cursor='hand2', command=quit)
B6.place(x=8, y=365)

photo = PhotoImage(file="D:\\super\\super.png")
imo = Label(pro, image=photo)
imo.place(x=120, y=50, width=308, height=272)

F2 = Frame(pro, width=570, height=125, bg='#0B2F3A')
F2.place(x=0, y=335)

photo1 = PhotoImage(file='D:\\super\\super2.png')
imo1 = Label(pro, image=photo1)
imo1.place(x=458, y=348, width=110, height=100)

L1 = Label(F2, text='اسم المستخدم', fg='#00BFFF', bg='#0B2F3A', font=('tajawal', 14,'bold'))
L1.place(x=320, y=25)
L2 = Label(F2, text='كلمة المرور', fg='#00BFFF', bg='#0B2F3A', font=('tajawal', 14,'bold'))
L2.place(x=330, y=70)
En1 = Entry(F2, font=('tajawal', 12), justify='center')
En1.place(x=130, y=29)
En2 = Entry(F2, font=('tajawal', 12), justify='center', show='*')  # عرض النجوم لكلمة المرور
En2.place(x=130, y=75)
B1 = Button(F2, text='إنشأ حساب', bg='#00BFFF', font=('tajawal', 12,'bold'), width=12, height=1,cursor='hand2',command=create_account)  # تعديل هنا
B1.place(x=10, y=20)
B = Button(F2, text='تسجيل الدخول', bg='#00BFFF', font=('tajawal', 12,'bold'), width=12, height=1,cursor='hand2', command=log)
B.place(x=10, y=73)

pro.mainloop()
