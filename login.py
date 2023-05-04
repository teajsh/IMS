from tkinter import *
# from PIL import ImageTk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import os
import email_pass
import time
import smtplib  #send message transfer protocol
class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System |Inventory Management system | Developed by Vidyalankar Institute of technology")
        self.root.geometry("1285x700+100+40")
        self.root.config(bg="white")
        self.otp =''
        #========images===============================
        self.photo_image = ImageTk.PhotoImage(file="Images/backgroundimage.jpg")
        self.lbl_phone_image = Label(self.root,image=self.photo_image,bd=0).place(x=2,y=0)

        self.MenuLogo=Image.open("Images/Objectives-of-Inventory-Control.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        

        self.employee_id =StringVar()
        self.password = StringVar()
        #====login frame=========================
        login_frame = Frame(self.root,bd=2,relief="raised")
        login_frame.place(x=650,y=10,width=600,height=650)

        lbl_text = Label(login_frame,font=("Impact",30,"bold"),text="LOGIN",bg="black",fg="white")
        lbl_text.pack(fill=X,side=TOP)
           
        lbl_menuLogo=Label(login_frame,image=self.MenuLogo)
        lbl_menuLogo.pack(side=BOTTOM,fill=X)   

        title = Label(login_frame,text="Login System",font=("Elephant",15,"bold")).place(x=0,y=60,relwidth=1)

        lbl_user= Label(login_frame,text="Employee ID ",font=("Andalus",20,"bold")).place(x=203,y=120)
        
        txt_employee_id =Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15,"bold")).place(x=150,y=160,width=300)

        lbl_pass= Label(login_frame,text="Password ",font=("Andalus",20,"bold")).place(x=220,y=190)
        txt_pass =Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15,"bold")).place(x=150,y=230,width=300)
       
        btn_login = Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",16,"bold"),bg="#00B0F0").place(x=150,y=300,width=300)
        
        hr = Label(login_frame,text=("--------------------------OR------------------------------"),fg="grey").place(x=150,y=350)

        btn_forget = Button(login_frame,text="Forget Password??",command=self.forget_window,font=("times new roman",10,"bold"),fg="red",bd=0,cursor="hand2").place(x=240,y=400)


        #==========register Frame ============================
     #    register_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
     #    register_frame.place(x=750,y=450,width=350,height=160)

        # lbl_reg = Label(register_frame,text="Don't have an account",font=("times new roman",10,"bold"))
        # btn_forget = Button(login_frame,text="Forget")

      

    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                 messagebox.showerror("Error","Credentials are Required!!",parent=self.root)
            else:
                 cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                 user = cur.fetchone()
                 if user == None:
                      messagebox.showerror("error","Invalid username/password",parent=self.root)
                 else:
                      if user[0]=="Admin":
                       self.root.destroy()
                       os.system("python dashboard.py")
                      else:
                           self.root.destroy()
                           os.system("python billing.py")      
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def forget_window(self):
          con=sqlite3.connect(database=r'ims.db')
          cur=con.cursor()
          try:  
            if self.employee_id.get() == "":
              messagebox.showerror("Error","Employee ID is required..!!",parent=self.root)
            else:     
                 cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                 email = cur.fetchone()
                 if email == None:
                      messagebox.showerror("error","Invalid Employee ID,try again",parent=self.root) 
                    
                 else:
                      #==========forget window===================   
                      self.var_otp =StringVar()
                      self.var_new_pass = StringVar()
                      self.var_conf_pass = StringVar()
                      #   call send email function
                      chk = self.send_email(email[0])
                      if chk!='s':
                           messagebox.showerror("Error","Connection Error try again",parent=self.root)
                      else:  
                         self.forget_win=Toplevel(self.root)
                         self.forget_win.title("RESET PASSWORD")
                         self.forget_win.geometry('400x350+500+100')
                         self.forget_win.focus_force()
                         title = Label(self.forget_win,text='Reset Password',font=('goudy old style',15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                         lbl_reset = Label(self.forget_win,text="Enter OTP send on register Email",font=("times new roman",15)).place(x=20,y=60)
                         txt_reset = Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="yellow").place(x=20,y=100,width=250,height=30)
                         #=================================================================
                         lbl_new_pass = Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                         txt_new_pass = Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="yellow").place(x=20,y=190,width=250,height=30)
                         #====================================================================
                         lbl_c_pass = Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                         txt_c_pass = Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="yellow").place(x=20,y=255,width=250,height=30)
                         #======================================================
                         self.btn_reset = Button(self.forget_win,text="Verify",command=self.validate_otp,font=("times new roman",15),bg="light green")
                         self.btn_reset.place(x=280,y=100,width=100,height=30)  
                         #=========================================================
                         self.btn_update = Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="light green")
                         self.btn_update.place(x=150,y=300,width=100,height=30)  
          except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def update_password(self):
         if self.var_new_pass.get()=='' or self.var_conf_pass.get()=='':
              messagebox.showerror("Error","Password is Required!!",parent=self.forget_win)
         elif self.var_new_pass.get()!= self.var_conf_pass.get():
              messagebox.showerror("Error","Confirm Password must be same!!",parent=self.forget_win)
         else:
              con=sqlite3.connect(database=r'ims.db')
              cur=con.cursor()
              try: 
                   cur.execute("Update employee SET pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                   con.commit()
                   messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                   self.forget_win.destroy()
              except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)      
                        

    def send_email(self,to_):
         s=smtplib.SMTP('smtp.gmail.com',587)
         s.starttls() #third person hack na kar sake  (encrpt kar diya hai)
         email_=email_pass.email_
         pass_=email_pass.pass_

         s.login(email_,pass_)

         self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
     #     print(self.otp)
         subj= 'IMS-Reset Password OTP'
         msg=f'Dear Sir/Madam ,\n\nYour Reset OTP is {str(self.otp)}\n\n with regards\nIMS Teams'
         msg = "Subject:{}\n\n{}".format(subj,msg)
         s.sendmail(email_,to_,msg)
         chk=s.ehlo()    #check whether email is send or not
         if chk[0]==250:
              return 's'
         else:
              return 'f'

    def validate_otp(self):
         if int(self.otp)==int(self.var_otp.get()):
              self.btn_update.config(state=NORMAL)
              self.btn_reset.config(state=DISABLED)
         else:
              messagebox.showerror("Error","Please enter the correct OTP",parent=self.forget_win)     
                     
root = Tk()
obj = Login_System(root)
root.mainloop()

#app password
# mdhlyaxijqdnmzxl