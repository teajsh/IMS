import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
import re
from tkcalendar import Calendar, DateEntry

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x610+210+130")
        self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        self.root.config(bg="light blue")
        self.root.focus_force()
        self.root.resizable(width=False,height=False)     
        
        #All variables=========================================
        self.var_searchby=StringVar()   
        self.var_searchtxtx=StringVar()       

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utpye=StringVar()
        self.var_salary=StringVar()

        #Search frame=======
        SearchFrame=LabelFrame(self.root,text="Search Employee ",font=("goudy old style",12,"bold"),bg="white")
        SearchFrame.place(x=250,y=20,width=900,height=70)

        #combo_box_search++++++++++
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #text_search=====
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxtx,font=('goudy old style',15,"bold"),bg="light yellow")
        txt_search.place(x=200,y=10,width=330)
        
        #button
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=('goudy old style',15,"bold"),bg="light green",cursor="hand2")
        btn_search.place(x=550,y=10,width=100,height=29)
        

        #======title=======
        title=Label(self.root,text="Employee Details",font=("times new roman",15,"bold"),bg="#B890FA",fg="white")
        title.place(x=50,y=100,width=1200)
        
        #====contents======
        #=============================row_01==========================================================================================
        emp_id=Label(self.root,text="*Emp ID :",font=("times new roman",15,"bold"),bg='light blue')
        emp_id.place(x=50,y=140)

        emp_gender=Label(self.root,text="*Gender :",font=("times new roman",15,"bold"),bg='light blue')
        emp_gender.place(x=570,y=140)

        emp_contact=Label(self.root,text="*Contact :",font=("times new roman",15,"bold"),bg='light blue')
        emp_contact.place(x=920,y=140)

        txt_emp_id=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_emp_id.place(x=141,y=140,width=400)

        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"bold"),bg='white')
        #txt_gender.place(x=680,y=140,width=210)

        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Transgender"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_gender.place(x=680,y=140,width=210)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg='white')
        txt_contact.place(x=1040,y=140,width=210)
        
        #=====================row_02====================================================================================================

        lbl_Name=Label(self.root,text="Name :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_Name.place(x=50,y=180)

        lbl_emp_DOB=Label(self.root,text="DOB :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_emp_DOB.place(x=570,y=180)

        lbl_emp_DOJ=Label(self.root,text="DOJ :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_emp_DOJ.place(x=920,y=180)

        txt_Name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_Name.place(x=141,y=180,width=400)
        
        txt_DOB=DateEntry(self.root,textvariable=self.var_dob,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_DOB.place(x=680,y=180,width=210)

        txt_DOJ=DateEntry(self.root,textvariable=self.var_doj,font=("times new roman",15,"bold"),bg='light yellow')
        txt_DOJ.place(x=1040,y=180,width=210)
           
        #===================row3=========================================================================================================

        lbl_email=Label(self.root,text="Email :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_email.place(x=50,y=220)     

        lbl_Password=Label(self.root,text="Password:-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_Password.place(x=570,y=220)

        lbl_Usertype=Label(self.root,text="UserType:-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_Usertype.place(x=920,y=220)

        txt_Email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_Email.place(x=141,y=220,width=400)
        
        txt_Password=Entry(self.root,textvariable=self.var_pass,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_Password.place(x=680,y=220,width=210)
        
        # txt_UserType=Entry(self.root,textvariable=self.var_utpye,font=("times new roman",15,"bold"),bg='light yellow')
        # txt_UserType.place(x=1040,y=220,width=210)

        cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_utpye,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_usertype.place(x=1040,y=220,width=210)
        cmb_usertype.current(0)
        
        #=============================row4========================================================================================

        lbl_address=Label(self.root,text="Address :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_address.place(x=50,y=260)     

        lbl_salary=Label(self.root,text="Salary:-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_salary.place(x=680,y=260)

        #lbl_Usertype=Label(self.root,text="UserType:-",font=("times new roman",15,"bold"),bg='light blue')
        #lbl_Usertype.place(x=920,y=220)

        self.txt_Address=Text(self.root,font=("times new roman",15,"bold"),bg='Light yellow')
        self.txt_Address.place(x=151,y=260,width=520,height=100)
        
        txt_Salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_Salary.place(x=760,y=260,width=210)

        # txt_UserType=Entry(self.root,textvariable=self.var_utpye,font=("times new roman",15,"bold"),bg='light yellow')
        # txt_UserType.place(x=1040,y=220,width=210)

        cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_utpye,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_usertype.place(x=1040,y=220,width=210)
        cmb_usertype.current(0)


        #===================================button=====================================================================================
        #________button_Save_________________
        btn_Save=Button(self.root,text="Save",command=self.add,font=('goudy old style',15,"bold"),bg="#00C5FF",cursor="hand2")
        btn_Save.place(x=680,y=319,width=100,height=40) 

        #_______button_update_________________
        btn_Update=Button(self.root,text="Update",command=self.update,font=('goudy old style',15,"bold"),bg="light green",cursor="hand2")
        btn_Update.place(x=790,y=319,width=100,height=40)

        #_______________delete_button___________________________
        btn_delete=Button(self.root,text="Delete",command=self.delete1,font=('goudy old style',15,"bold"),bg="#FF3600",cursor="hand2")
        btn_delete.place(x=900,y=319,width=100,height=40)

        #_______________Clear_button___________________________
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=('goudy old style',15,"bold"),bg="#C4C4C4",cursor="hand2")
        btn_clear.place(x=1010,y=319,width=100,height=40)
        
        #_______++++++++++++++++++========Tree view of employee details+++++++++=======___________________

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=370,relwidth=1,height=240)

        #_________scrolling____________________________

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="Employee_ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email_ID")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="USERTYPE")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        #_____________________________________________________________
        self.EmployeeTable["show"]="headings"
        #=============================================================
        self.EmployeeTable.column("eid",width=70)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.show()
#=============================================================================================
    def add(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if len(str(self.var_emp_id.get())) != 3:
                messagebox.showerror("Error","Employee ID must be required and 3 digit",parent=self.root)
            elif not self.is_alphabetic(self.var_name.get()):
                messagebox.showerror("Error","Please enter proper name ",parent=self.root)
            elif not self.is_valid_email(self.var_email.get()):
                messagebox.showerror("Error","Please enter valid email ",parent=self.root)
            elif self.var_gender.get() == "":
                messagebox.showerror("Error","Gender is required",parent=self.root)
            elif not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", f"Enter a valid 10-digit Contact Number!!", parent=self.root)

            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee is already taken try another one!!!",parent=self.root) 
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                          self.var_emp_id.get(),
                          self.var_name.get(),
                          self.var_email.get(),
                          self.var_gender.get(),
                          self.var_contact.get(),
                          self.var_dob.get(),
                          self.var_doj.get(),
                          self.var_pass.get(),
                          self.var_utpye.get(),
                          self.txt_Address.get('1.0',END),
                          self.var_salary.get()

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Employee Addedd Successfully....Done✅",parent=self.root)
                    self.show()
            # if self.var_contact.get()=="":
            #     messagebox.showerror("Error","Contact must be required",Parent=self.root)
            # if self.var_salary.get()=="":
            #     messagebox.showerror("Error","Salary Must be required",parent=self.root)
            # if self.var_dob.get()=="":
            #     messagebox.showerror("Error","Date of birth is required",Parent=self.root)
            # if self.var_name.get()=="":
            #     messagebox.showerror("Error","Name is required",Parent=self.root)   
            # if self.var_doj.get()=="":
            #     messagebox.showerror("Error","Date of joining must be required",parent=self.root)
            # if self.var_utpye.get()=="":
            #     messagebox.showerror("Error","Usertype is required",Parent=self.root)
            # if self.var_email.get()=="":
            #     messagebox.showerror("Error","Email must be required",parent=self.root)
            # if self.var_searchby.get()=="":
            #     messagebox.showerror("Error","Search must be required",Parent=self.root)             


         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())   
            for row in rows:
               self.EmployeeTable.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def is_alphabetic(self,input_str):
        """Checks if input string contains only alphabetic characters"""
        pattern = r'^[a-zA-Z]+$'  # regular expression pattern to match alphabetic characters
        return bool(re.match(pattern, input_str))
    def is_valid_email(self, email):
        """
        Returns True if the given string is a valid email address, else returns False.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def get_data(self,ev):
           f=self.EmployeeTable.focus()
           content=(self.EmployeeTable.item(f))
           row=content['values']
           #print(row)
           self.var_emp_id.set(row[0]),
           self.var_name.set(row[1]),
           self.var_email.set(row[2]),
           self.var_gender.set(row[3]),
           self.var_contact.set(row[4]),
           self.var_dob.set(row[5]),
           self.var_doj.set(row[6]),
           self.var_pass.set(row[7]),
           self.var_utpye.set(row[8]),
           self.txt_Address.delete('1.0',END),
           self.txt_Address.insert(END,row[9]),
           self.var_salary.set(row[10])
    
    def update(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID!",parent=self.root) 
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                          
                          self.var_name.get(),
                          self.var_email.get(),
                          self.var_gender.get(),
                          self.var_contact.get(),
                          self.var_dob.get(),
                          self.var_doj.get(),
                          self.var_pass.get(),
                          self.var_utpye.get(),
                          self.txt_Address.get('1.0',END),
                          self.var_salary.get(),
                          self.var_emp_id.get(),

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Employee Table Updated Successfully....Done✅",parent=self.root)
                    self.show()
                       


         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete1(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID!",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==TRUE:
                      cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                      con.commit()
                      messagebox.showinfo("Delete","Successfully Deleted Data...!!",parent=self.root)
                      self.clear()
                    


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        # con=sqlite3.connect(database=r'ims.db')
        # cur=con.cursor() 
        # try:
           self.var_emp_id.set("")
           self.var_name.set("")
           self.var_email.set("")
           self.var_gender.set("Select")
           self.var_contact.set("")
           self.var_dob.set("")
           self.var_doj.set("")
           self.var_pass.set("")
           self.var_utpye.set("Admin")
           self.txt_Address.delete('1.0',END)
        #    self.txt_Address.insert(END,row[9]),
           self.var_salary.set("")
           self.var_searchtxtx.set("")
           self.var_searchby.set("Select")
           
           self.show()

    def enterdate(self):

        ttk.Label("Enter Date", text='Choose date').pack(padx=10, pady=10)

        cal = DateEntry("Enter Date", width=12, background='white',
                        foreground='white', borderwidth=2)
        cal.pack(padx=30, pady=30)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxtx.get()=="":
                messagebox.showerror("Error","Search input should be required...!!!!",parent=self.root)
            else:    

             cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxtx.get()+"%'")
             rows=cur.fetchall()
             if len(rows)!=0:

                self.EmployeeTable.delete(*self.EmployeeTable.get_children())   
                for row in rows:
                  self.EmployeeTable.insert('',END,values=row)
             else:
                messagebox.showerror("Error","No record found",parent=self.root)

              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()        