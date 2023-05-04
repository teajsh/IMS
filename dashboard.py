from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from customtkinter import *
from tkinter import ttk,messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from sales import salesClass
from product import productClass
import time
import os
import re
from tkcalendar import Calendar, DateEntry


class categoryClass:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Manage Product Category | Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="white")
        # self.root.resizable(width=False,height=False)
        back  = set_appearance_mode("light")
        # =======variables==========================#
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        # =================title==================
        lbl_title = Label(self.root, text="Manage Product Category", bd=3, relief=RIDGE,
                          font=("goudy old style", 30, "bold"), bg="#184a45", fg="white")
        # lbl_title.place(x=0,y=0,height=60,relwidth=1)
        lbl_title.pack(side=TOP, fill=X)

        lbl_title = Label(self.root, text=" Enter Category Name", font=("goudy old style", 25, "bold"), bg="white",
                          fg="#184a45")
        lbl_title.place(x=40, y=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="light yellow",
                         fg="black")
        txt_name.place(x=50, y=150, width=270)

        # +=============button_01===================

        btn_add = Button(self.root, text="Add", command=self.add, font=("goudy old style", 20, "bold"),
                         bg="light green", fg="black", cursor="hand2")
        btn_add.place(x=350, y=150, height=38, width=170)
        # ==============button02 +=================

        btn_delete = Button(self.root, text="Delete", command=self.delete1, font=("goudy old style", 20, "bold"),
                            bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=550, y=150, height=38, width=170)

        # +++++++++++++++++tree view________________====================

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=750, y=100, width=480, height=450)

        # _________scrolling____________________________

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview(cat_frame, columns=("category_ID", "name"), yscrollcommand=scrolly.set,
                                           xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("category_ID", text="Category_ID")
        self.category_table.heading("name", text="Name")
        # self.category_table.heading("contact",text="Contact")
        # self.category_table.heading("desc",text="D escription")
        # _____________________________________________________________
        self.category_table["show"] = "headings"
        # =============================================================
        self.category_table.column("category_ID", width=70)
        self.category_table.column("name", width=100)
        # self.category_table.column("contact",width=100)
        # self.category_table.column("desc",width=100)
        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)

        # ====Category========================================

        lbl_txt = Label(self.root, text="=====================Category list===================",
                        font=("goudy old style", 15, "bold"), fg="black", bg="white").place(x=100, y=200)
        self.show()

    # ==============================function================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name is required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category already present try another one!!!", parent=self.root)
                else:
                    cur.execute("Insert into category(name)values(?)", (
                        self.var_name.get(),
                        #   self.var_name.get(),
                        #   self.var_contact.get(),
                        #   self.text_desc.get('1.0',END),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category Addedd Successfully....Done✅", parent=self.root)
                    self.show()
            # if self.var_contact.get()=="":
            #     messagebox.showerror("Error","Contact must be required",Parent=self.root)
            # if self.var_salary.get()=="":
            #     messagebox.showerror("Error","Salary Must be required",parent=self.root)
            # if self.var_dob.get()=="":
            #     messagebox.showerror("Error","Date of birth is required",Parent=self.root)
            # if self.var_gender.get()=="":
            #     messagebox.showerror("Error","Gender is required",parent=self.root)
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
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row = content['values']
        # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete1(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select category from the list....", parent=self.root)
            else:
                cur.execute("Select * from category where category_ID=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Error,please try again !", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to Delete", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from category where category_ID=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Successfully Deleted Data...!!", parent=self.root)
                        #   self.clear()
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



class employeeClass:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="light blue")
        # self.root.focus_force()
        # self.root.resizable(width=False, height=False)

        # All variables=========================================
        self.var_searchby = StringVar()
        self.var_searchtxtx = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utpye = StringVar()
        self.var_salary = StringVar()

        # Search frame=======
        SearchFrame = LabelFrame(self.root, text="Search Employee ", font=("goudy old style", 20, "bold"), bg="white")
        SearchFrame.place(x=2, y=4, width=1600, height=90)

        # combo_box_search++++++++++
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15, "bold"))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        # text_search=====
        txt_search = CTkEntry(SearchFrame, textvariable=self.var_searchtxtx, font=('goudy old style', 15, "bold"),
                           bg_color="light yellow",width=930)
        txt_search.place(x=180, y=4)

        # button
        btn_search = CTkButton(SearchFrame, text="Search", command=self.search, font=('goudy old style', 17, "bold"),
                             cursor="hand2", width=130, height=29,fg_color="black",bg_color="black")
        btn_search.place(x=1140, y=4)

        # ======title=======
        title = Label(self.root, text="Employee Details", font=("times new roman", 15, "bold"), bg="#D9D9D9",
                      fg="white")
        title.place(x=2, y=100, width=1600)

        # ====contents======
        # =============================row_01==========================================================================================
        emp_id = CTkLabel(self.root, text="Emp ID :", font=("times new roman", 20, "bold"))
        emp_id.place(x=10, y=140)

        emp_gender = CTkLabel(self.root, text="Gender :", font=("times new roman", 20, "bold"))
        emp_gender.place(x=570, y=140)

        emp_contact = CTkLabel(self.root, text="Contact :", font=("times new roman", 20, "bold"))
        emp_contact.place(x=920, y=140)

        txt_emp_id = CTkEntry(self.root, textvariable=self.var_emp_id, font=("times new roman", 20, "bold"), width=400)
        txt_emp_id.place(x=141, y=140)

        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"bold"),bg='white')
        # txt_gender.place(x=680,y=140,width=210)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                  values=("Select", "Male", "Female", "Transgender"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 20, "bold"), width=20)
        cmb_gender.place(x=820, y=180)
        cmb_gender.current(0)

        txt_contact = CTkEntry(self.root, textvariable=self.var_contact, font=("times new roman", 15, "bold"), width=210)
        txt_contact.place(x=1040, y=140)

        # =====================row_02====================================================================================================

        lbl_Name = CTkLabel(self.root, text="Name :", font=("times new roman", 20, "bold"))
        lbl_Name.place(x=10, y=180)

        lbl_emp_DOB = CTkLabel(self.root, text="DOB :", font=("times new roman", 20, "bold"))
        lbl_emp_DOB.place(x=570, y=180)

        lbl_emp_DOJ = CTkLabel(self.root, text="DOJ :", font=("times new roman", 20, "bold"))
        lbl_emp_DOJ.place(x=920, y=180)

        txt_Name = CTkEntry(self.root, textvariable=self.var_name, font=("times new roman", 20, "bold"), width=400)
        txt_Name.place(x=141, y=180)

        txt_DOB = DateEntry(self.root, textvariable=self.var_dob, font=("times new roman", 20, "bold"))
        txt_DOB.place(x=795, y=225, width=210)

        txt_DOJ = DateEntry(self.root, textvariable=self.var_doj, font=("times new roman", 20, "bold"))
        txt_DOJ.place(x=1230, y=220, width=210)

        # ===================row3=========================================================================================================

        lbl_email = CTkLabel(self.root, text="Email :", font=("times new roman", 20, "bold"))
        lbl_email.place(x=10, y=220)

        lbl_Password = CTkLabel(self.root, text="Password:", font=("times new roman", 20, "bold"))
        lbl_Password.place(x=570, y=220)

        lbl_Usertype = CTkLabel(self.root, text="UserType:", font=("times new roman", 20, "bold"))
        lbl_Usertype.place(x=920, y=220)

        txt_Email = CTkEntry(self.root, textvariable=self.var_email, font=("times new roman", 20, "bold"), width=400
                          )
        txt_Email.place(x=141, y=220)

        txt_Password = CTkEntry(self.root, textvariable=self.var_pass, font=("times new roman", 20, "bold"),width=210
                             )
        txt_Password.place(x=680, y=220, )

        # txt_UserType=Entry(self.root,textvariable=self.var_utpye,font=("times new roman",15,"bold"),bg='light yellow')
        # txt_UserType.place(x=1040,y=220,width=210)

        cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_utpye, values=("Admin", "Employee"),
                                    state='readonly', justify=CENTER, font=("goudy old style", 20, "bold"))
        cmb_usertype.place(x=1300, y=270, width=210)
        cmb_usertype.current(0)

        # =============================row4========================================================================================

        lbl_address = CTkLabel(self.root, text="Address :", font=("times new roman", 20, "bold"))
        lbl_address.place(x=10, y=260)

        lbl_salary = CTkLabel(self.root, text="Salary:", font=("times new roman", 20, "bold"))
        lbl_salary.place(x=580, y=260)

        # lbl_Usertype=Label(self.root,text="UserType:-",font=("times new roman",15,"bold"),bg='light blue')
        # lbl_Usertype.place(x=920,y=220)

        self.txt_Address = Text(self.root, font=("times new roman", 20, "bold"), bg='Light yellow')
        self.txt_Address.place(x=151, y=330, width=520, height=100)

        txt_Salary = CTkEntry(self.root, textvariable=self.var_salary, font=("times new roman", 20, "bold"), width=210
                           )
        txt_Salary.place(x=660, y=260)

        # txt_UserType=Entry(self.root,textvariable=self.var_utpye,font=("times new roman",15,"bold"),bg='light yellow')
        # txt_UserType.place(x=1040,y=220,width=210)

        # cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_utpye, values=("Admin", "Employee"),
        #                             state='readonly', justify=CENTER, font=("goudy old style", 20, "bold"))
        # cmb_usertype.place(x=1100, y=260, width=210)
        # cmb_usertype.current(0)

        # ===================================button=====================================================================================
        # ________button_Save_________________
        btn_Save = CTkButton(self.root, text="Save", command=self.add, font=('goudy old style', 20, "bold"), width=100, height=40,
                          cursor="hand2")
        btn_Save.place(x=680, y=319)

        # _______button_update_________________
        btn_Update = CTkButton(self.root, text="Update", command=self.update, font=('goudy old style', 20, "bold")
                            , width=100, height=40, cursor="hand2")
        btn_Update.place(x=790, y=319)

        # _______________delete_button___________________________
        btn_delete = CTkButton(self.root, text="Delete", command=self.delete1, font=('goudy old style', 20, "bold"),
                            width=100, height=40,cursor="hand2")
        btn_delete.place(x=900, y=319)

        # _______________Clear_button___________________________
        btn_clear = CTkButton(self.root, text="Clear", command=self.clear, font=('goudy old style', 20, "bold"),
                            width=100, height=40, cursor="hand2")
        btn_clear.place(x=1010, y=319)

        # _______++++++++++++++++++========Tree view of employee details+++++++++=======___________________

        emp_frame = CTkFrame(self.root)
        emp_frame.place(x=0, y=410)
        emp_frame.place_configure(width=1690,height=300)

        # _________scrolling____________________________

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid", text="Employee_ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email_ID")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="USERTYPE")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        # _____________________________________________________________
        self.EmployeeTable["show"] = "headings"
        # =============================================================
        self.EmployeeTable.column("eid", width=70)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.show()

    # =============================================================================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if len(str(self.var_emp_id.get())) != 3:
                messagebox.showerror("Error", "Employee ID must be required and 3 digit", parent=self.root)
            elif not self.is_alphabetic(self.var_name.get()):
                messagebox.showerror("Error", "Please enter proper name ", parent=self.root)
            elif not self.is_valid_email(self.var_email.get()):
                messagebox.showerror("Error", "Please enter valid email ", parent=self.root)
            elif self.var_gender.get() == "":
                messagebox.showerror("Error", "Gender is required", parent=self.root)
            elif not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
                messagebox.showerror("Error", f"Enter a valid 10-digit Contact Number!!", parent=self.root)

            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee is already taken try another one!!!", parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utpye.get(),
                            self.txt_Address.get('1.0', END),
                            self.var_salary.get()

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Addedd Successfully....Done✅", parent=self.root)
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
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def is_alphabetic(self, input_str):
        """Checks if input string contains only alphabetic characters"""
        pattern = r'^[a-zA-Z]+$'  # regular expression pattern to match alphabetic characters
        return bool(re.match(pattern, input_str))

    def is_valid_email(self, email):
        """
        Returns True if the given string is a valid email address, else returns False.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utpye.set(row[8]),
        self.txt_Address.delete('1.0', END),
        self.txt_Address.insert(END, row[9]),
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid employee ID!", parent=self.root)
                else:
                    cur.execute(
                        "Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                        (

                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utpye.get(),
                            self.txt_Address.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get(),

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Table Updated Successfully....Done✅", parent=self.root)
                    self.show()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete1(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid employee ID!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to Delete", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Successfully Deleted Data...!!", parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

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
        self.txt_Address.delete('1.0', END)
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
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxtx.get() == "":
                messagebox.showerror("Error", "Search input should be required...!!!!", parent=self.root)
            else:

                cur.execute(
                    "Select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxtx.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:

                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


class supplierClass:
    def __init__(self, root):
        self.root=root
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="light blue")
        # self.root.focus_force()
        # self.root.resizable(width=False,height=False)
        # All variables=========================================
        self.var_searchby = StringVar()
        self.var_searchtxtx = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # =======================================Search frame=====================================
        SearchFrame = LabelFrame(frames, text="Search Employee ", font=("goudy old style", 15, "bold"), bg="white")
        SearchFrame.place(x=2, y=2, width=1600, height=70)

        # +++++++++++++++++++++++++++++++++++combo_box_search+++++++++++++++++++++++++=======+++++++
        lbl_search = Label(SearchFrame, text="Search by invoice no.", bg="white", font=("goudy old style", 15, "bold"))
        lbl_search.place(x=10, y=5)
        # lbl_search.current(0)

        # ==================================text_search====================================================
        txt_search = CTkEntry(SearchFrame, textvariable=self.var_searchtxtx, font=('goudy old style', 15, "bold"),width=930
                           )
        txt_search.place(x=200, y=2)
        # ====================================button========================================================
        btn_search = CTkButton(SearchFrame, text="Search", command=self.search, font=('goudy old style', 15, "bold"),
                            cursor="hand2", width=100, height=29)
        btn_search.place(x=1150, y=2)

        # ======title=======
        title = Label(frames, text="Supplier Details", font=("times new roman", 15, "bold"), bg="#B890FA",
                      fg="white")
        title.place(x=5, y=100, width=1600)

        # ====contents======
        # =============================row_01==========================================================================================
        emp_supplier_invoice = CTkLabel(frames, text="Emp ID :", font=("times new roman", 15, "bold"))
        emp_supplier_invoice.place(x=50, y=140)

        txt_supplier_invoice = CTkEntry(frames, textvariable=self.var_sup_invoice, font=("times new roman", 15, "bold"), width=400
                                    )
        txt_supplier_invoice.place(x=141, y=140)

        # =====================row_02====================================================================================================

        lbl_Name = CTkLabel(frames, text="Name :-", font=("times new roman", 15, "bold"))
        lbl_Name.place(x=50, y=180)

        txt_Name = CTkEntry(frames, textvariable=self.var_name, font=("times new roman", 15, "bold"), width=400)
        txt_Name.place(x=141, y=180)

        # ===================row3=========================================================================================================

        lbl_contact = CTkLabel(frames, text="Contact:", font=("times new roman", 15, "bold"))
        lbl_contact.place(x=50, y=220)

        txt_contact = CTkEntry(frames, textvariable=self.var_contact, font=("times new roman", 15, "bold"), width=400
                            )
        txt_contact.place(x=141, y=220)

        # =============================row4========================================================================================

        lbl_desc = CTkLabel(frames, text="Description:-", font=("times new roman", 15, "bold"))
        lbl_desc.place(x=50, y=260)

        self.text_desc = Text(frames, font=("times new roman", 15, "bold"), bg='Light yellow')
        self.text_desc.place(x=178, y=340, width=520, height=100)

        # ===================================button=====================================================================================
        # ________button_Save_________________
        btn_Save = CTkButton(frames, text="Save", command=self.add, font=('goudy old style', 15, "bold"),width=100, height=40,
                          cursor="hand2")
        btn_Save.place(x=680, y=319)

        # _______button_update_________________
        btn_Update = CTkButton(frames, text="Update", command=self.update, font=('goudy old style', 15, "bold"), width=100, height=40
                           , cursor="hand2")
        btn_Update.place(x=790, y=319)

        # _______________delete_button___________________________
        btn_delete = CTkButton(frames, text="Delete", command=self.delete1, font=('goudy old style', 15, "bold"), width=100, height=40
                            , cursor="hand2")
        btn_delete.place(x=900, y=319)

        # _______________Clear_button___________________________
        btn_clear = CTkButton(frames, text="Clear", command=self.clear, font=('goudy old style', 15, "bold"), width=100, height=40
                           , cursor="hand2")
        btn_clear.place(x=1010, y=319)

        # _______++++++++++++++++++========Tree view of employee details+++++++++=======___________________

        emp_frame = Frame(frames, bd=3, relief=RIDGE)
        # emp_frame.place(x=0, y=370, relwidth=1, height=240)
        emp_frame.pack(fill=X,side=BOTTOM)

        # _________scrolling____________________________

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        # _____________________________________________________________
        self.supplierTable["show"] = "headings"
        # =============================================================
        self.supplierTable.column("invoice", width=70)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # =============================================================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice No. is already taken try another one!!!", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc)values(?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get('1.0', END),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "supplier Addedd Successfully....Done✅", parent=self.root)
                    self.show()
            # if self.var_contact.get()=="":
            #     messagebox.showerror("Error","Contact must be required",Parent=self.root)
            # if self.var_salary.get()=="":
            #     messagebox.showerror("Error","Salary Must be required",parent=self.root)
            # if self.var_dob.get()=="":
            #     messagebox.showerror("Error","Date of birth is required",Parent=self.root)
            # if self.var_gender.get()=="":
            #     messagebox.showerror("Error","Gender is required",parent=self.root)
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
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.text_desc.delete('1.0', END),
        self.text_desc.insert(END, row[3]),

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice =?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice No.!", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?", (

                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get('1.0', END),
                        self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully....Done✅", parent=self.root)
                    self.show()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete1(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice number !", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to Delete", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Successfully Deleted Data...!!", parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        # con=sqlite3.connect(database=r'ims.db')
        # cur=con.cursor()
        # try:
        self.var_sup_invoice.set("")
        self.var_name.set("")

        self.var_contact.set("")

        self.text_desc.delete('1.0', END)
        #    self.text_desc.insert(END,row[9]),

        self.var_searchtxtx.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxtx.get() == "":
                messagebox.showerror("Error", "Invoice number is required...!!!!", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_searchtxtx.get(),))
                row = cur.fetchone()
                if row != None:

                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


class productClass:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Product Page | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="white")
        # self.root.focus_force()
        # self.root.resizable(width=False, height=False)
        # ==============variables=======================

        self.var_searchby = StringVar()
        self.var_searchtxtx = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        # ================================================
        product_Frame = Frame(self.root, bd=7, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=490, height=780)

        # ==================title=========================
        title = Label(product_Frame, text="Manage Product Details", font=("times new roman", 18, "bold"), bg="#B890FA",
                      fg="white")
        title.pack(side=TOP, fill=X)

        # ============category text=========================
        lbl_category = Label(product_Frame, text="Category :", font=("times new roman", 15, "bold"), fg="black",
                             bg="white")
        lbl_category.place(x=5, y=50)

        # =============== supplier========================
        lbl_supplier = Label(product_Frame, text="Supplier :", font=("times new roman", 15, "bold"), fg="black",
                             bg="white")
        lbl_supplier.place(x=5, y=100)

        # ================product Name===================
        lbl_product = Label(product_Frame, text="Product Name :", font=("times new roman", 15, "bold"), fg="black",
                            bg="white")
        lbl_product.place(x=5, y=150)

        # =================Price===========================
        lbl_price = Label(product_Frame, text="Price :", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lbl_price.place(x=5, y=50 * 4)

        # ==================Quantity=========================
        lbl_quantity = Label(product_Frame, text="Quantity :", font=("times new roman", 15, "bold"), fg="black",
                             bg="white")
        lbl_quantity.place(x=5, y=50 * 5)

        # ============status===================================
        lbl_status = Label(product_Frame, text="Status :", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lbl_status.place(x=5, y=50 * 6)

        # ==============TEXT_BOX===============================

        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly',
                               justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_cat.place(x=150, y=50, width=300)
        cmb_cat.current(0)

        # ===============Supplier combo box==================
        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly',
                               justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_sup.place(x=150, y=100, width=300)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15, "bold"),
                         bg="light yellow")
        txt_name.place(x=150, y=150, width=300)

        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15, "bold"),
                          bg="light yellow")
        txt_price.place(x=150, y=200, width=300)

        txt_quantity = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15, "bold"),
                             bg="light yellow")
        txt_quantity.place(x=150, y=250, width=300)

        # txt_status=Entry(product_Frame,textvariable=self.var_status,font=("goudy old style",15,"bold"),bg="light yellow")
        # txt_status.place(x=150,y=300,width=270)
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"),
                                  state='readonly', justify=CENTER, font=("goudy old style", 15, "bold"))
        cmb_status.place(x=150, y=300, width=300)
        cmb_status.current(0)

        # ===================================button=====================================================================================
        # ________button_Save_________________
        btn_Save = Button(product_Frame, text="Save", command=self.add, font=('goudy old style', 20, "bold"),
                          bg="#00C5FF", cursor="hand2")
        btn_Save.place(x=10, y=360, width=220, height=50)

        # _______button_update_________________
        btn_Update = Button(product_Frame, text="Update", command=self.update, font=('goudy old style', 15, "bold"),
                            bg="light green", cursor="hand2")
        btn_Update.place(x=240, y=360, width=210, height=50)

        # _______________delete_button___________________________
        btn_delete = Button(product_Frame, text="Delete", command=self.delete1, font=('goudy old style', 15, "bold"),
                            bg="#FF3600", cursor="hand2")
        btn_delete.place(x=10, y=420, width=220, height=50)

        # _______________Clear_button___________________________
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=('goudy old style', 15, "bold"),
                           bg="#C4C4C4", cursor="hand2")
        btn_clear.place(x=240, y=420, width=210, height=50)

        # ===================================================================+++++++++++++++++++++
        # Search frame=======
        SearchFrame = LabelFrame(self.root, text="Search Employee ", font=("goudy old style", 12, "bold"), bg="white")
        SearchFrame.place(x=520, y=10, width=1150, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER,
                                  font=("goudy old style", 15, "bold"))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        # text_search=====
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxtx, font=('goudy old style', 15, "bold"),
                           bg="light yellow")
        txt_search.place(x=200, y=10, width=330)

        # button
        btn_search = CTkButton(SearchFrame, text="Search", command=self.search, font=('goudy old style', 15, "bold"),
                             cursor="hand2", width=120, height=29)
        btn_search.place(x=790, y=2)

        # =============================tree view=========================================
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=520, y=100, width=1150, height=690)

        # _________scrolling____________________________

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame,
                                          columns=("pid", "Supplier", "Category", "name", "price", "qty", "status"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid", text="Product_ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"
        # =============================================================
        self.product_table.column("pid", width=70)
        self.product_table.column("Category", width=100, anchor=CENTER)
        self.product_table.column("Supplier", width=100, anchor=CENTER)
        self.product_table.column("name", width=100, anchor=CENTER)
        self.product_table.column("price", width=100, anchor=CENTER)
        self.product_table.column("qty", width=100, anchor=CENTER)
        self.product_table.column("status", width=100, anchor=CENTER)

        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.product_table.pack(fill=BOTH, expand=1)
        self.show()
        # self.fetch_cat_sup()

    # =============================================================================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()

            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_name.get() == "Select":
                messagebox.showerror("Error", "All fields must be required", parent=self.root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already present, try another one!!!", parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status)values(?,?,?,?,?,?)", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Addedd Successfully....Done✅", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product_table.focus()
        content = (self.product_table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_sup.set(row[1])
        self.var_cat.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from List", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product ID!", parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?", (

                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Table Updated Successfully....Done✅", parent=self.root)
                    self.show()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete1(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product ID must be required", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product ID!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to Delete", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from product where pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Successfully Deleted Data...!!", parent=self.root)
                        self.clear()



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        # con=sqlite3.connect(database=r'ims.db')
        # cur=con.cursor()
        # try:
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        #    self.txt_Address.insert(END,row[9]),
        # self.var_salary.set("")
        self.var_searchtxtx.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxtx.get() == "":
                messagebox.showerror("Error", "Search input should be required...!!!!", parent=self.root)
            else:

                cur.execute(
                    "Select * from product where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxtx.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


class salesClass:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1520x790+0+0")
        # self.root.title("Sales Page | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="white")
        # self.root.focus_force()
        # self.root.resizable(width=False,height=False)
        # ===================================================================================
        self.bill_list = []
        self.var_invoice = StringVar()

        # ======title================================
        lbl_title = CTkLabel(self.root, text=" View Customer Bill ",
                          font=("goudy old style", 40, "bold"))
        lbl_title.pack(side=TOP, fill=X)

        lbl_invoice = CTkLabel(self.root, text="Invoice Number :", font=("times new roman", 20, "bold"), bg_color="white")
        lbl_invoice.place(x=20, y=100)

        txt_invoice = CTkEntry(self.root, textvariable=self.var_invoice,
                            bg_color="light yellow")
        txt_invoice.place(x=175, y=100)

        btn_search = CTkButton(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"),
                             cursor="hand2", width=145,fg_color="white",text_color="black", height=28,border_color="black",border_width=2)
        btn_search.place(x=20, y=150)

        btn_clear = CTkButton(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"),
                            fg_color="black", cursor="hand2", width=135, height=28)
        btn_clear.place(x=175, y=150)

        # ==================Frame==========================

        sales_Frame = CTkFrame(self.root,width=200,height=700)
        sales_Frame.place(x=400,y=80)
        sales_Frame.place_configure(width=300,height=437)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.Sales_list = Listbox(sales_Frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH, expand=1)
        self.Sales_list.bind("<ButtonRelease-1>", self.get_data)
        # =================bill area=================

        bill_Frame = CTkFrame(self.root,width=520, height=200,border_color="black",border_width=2,bg_color="white")
        bill_Frame.place(x=690, y=80)
        bill_Frame.place_configure(height=437)

        # ============title in bill area====================
        lbl_title = Label(bill_Frame, text="Customer Bill Area ", font=("goudy old style", 20, "bold"),
                          bg="light green")
        lbl_title.pack(side=TOP, fill=X)
        # ================scroll bar in  bill area==================

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=("goudy old style", 15), bg="light yellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # ================frame===========================================================
        sal_frame = CTkFrame(self.root,height=290)
        sal_frame.place(x=0, y=440)
        # sal_frame.pack(side=BOTTOM,fill=X)
        sal_frame.place_configure(height=280,width=1690)
        

        # _________scrolling____________________________

        scrolly = Scrollbar(sal_frame, orient=VERTICAL)
        scrollx = Scrollbar(sal_frame, orient=HORIZONTAL)
        #     cur.execute("CREATE TABLE IF NOT EXISTS sales(sid INTEGER PRIMARY KEY AUTOINCREMENT,invoice text,product_ID text,Product_Name text,Product_Price text,Quantity text,cname text,cphone text,netprice text)")
        # # con.commit()
        self.salesTable = ttk.Treeview(sal_frame, columns=(
        "sid", "invoice", "product_ID", "Product_Name", "Product_Price", "Quantity", "cname", "cphone", "netprice",
        "date"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.salesTable.xview)
        scrolly.config(command=self.salesTable.yview)
        self.salesTable.heading("sid", text="SID")
        self.salesTable.heading("invoice", text="INVOICE")
        self.salesTable.heading("product_ID", text="Product ID")
        self.salesTable.heading("Product_Name", text="product Name")
        self.salesTable.heading("Product_Price", text="Price")
        self.salesTable.heading("Quantity", text="Quantity")
        self.salesTable.heading("cname", text="Name")
        self.salesTable.heading("cphone", text="Phone")
        self.salesTable.heading("netprice", text="Total_Price")
        self.salesTable.heading("date", text="Date")

        self.salesTable["show"] = "headings"
        # =============================================================
        self.salesTable.column("sid", width=70, anchor="center")
        self.salesTable.column("invoice", width=100, anchor="center")
        self.salesTable.column("product_ID", width=100, anchor="center")
        self.salesTable.column("Product_Name", width=100, anchor="center")

        self.salesTable.column("Product_Price", width=100, anchor="center")
        self.salesTable.column("Quantity", width=100, anchor="center")
        self.salesTable.column("cname", width=100, anchor="center")
        self.salesTable.column("cphone", width=100, anchor="center")
        self.salesTable.column("netprice", width=100, anchor="center")
        self.salesTable.column("date", width=100, anchor="center")
        # self.salesTable.column("utype",width=100)
        # self.salesTable.column("salary",width=100)
        self.salesTable.bind("<ButtonRelease-1>", self.get_data)
        self.salesTable.pack(fill=BOTH, expand=1)

        self.shows()
        self.show()

    # ==============================================================================
    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.Sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.Sales_list.curselection()
        file_name = self.Sales_list.get(index_)
        # self.bill_frame=file_name
        self.bill_area.delete('1.0', END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def shows(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from sales")
            rows = cur.fetchall()
            self.salesTable.delete(*self.salesTable.get_children())
            for row in rows:
                self.salesTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice Number should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invoice number is Invalid", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete("1.0", END)


class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        self.root.config(bg="white")
        back = set_appearance_mode("light")

        #title=========
        self.icon_title=PhotoImage(file="Images/icons8-in-inventory_logo-64.png")
        title=CTkLabel(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),height=70,bg_color="white",padx=10,pady=27).place(x=0,y=0)
       


        #button_logout======
        btn_logout=CTkButton(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),cursor="hand2",height=40,bg_color="white",fg_color="black",width=150).place(x=1340,y=30)

        #clock======
        self.Ibl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time : HH:MM:SS",font=("times new roman",15),bg="#000000",fg="white")
        # self.Ibl_clock.place(x=0,y=75,relwidth=1,height=30)
        self.Ibl_clock.pack(side=TOP,fill=X)
        
        
        #Left menu=======
        self.MenuLogo=Image.open("Images/Objectives-of-Inventory-Control.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=209,height=810)


        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)


        self.icon_side=PhotoImage(file="Images/Link.png")
        lbl_menu=Label(LeftMenu,text="MENU",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        #button_01
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)
        #Button_2
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)
        #button_3
        btn_category=Button(LeftMenu,text="Category",command=self.Category,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)
        #button_4
        btn_product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)
        #button_5
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)
        #button_6
        btn_exit=Button(LeftMenu,text="Dashboard",command=mainF.tkraise,font=("times new roman",25,"bold"),image=self.icon_side,compound=LEFT,padx=5,pady=4,anchor="w",bg="white",cursor="hand2",bd=3).pack(side=TOP,fill=X)

        #===Content_01===
        self.lbl_employee=Button(mainF,text="Total Employee\n[ 0 ]",bd="3",relief="ridge",bg="light blue",fg="black",font=("goudy old style",20,"bold"),command=self.employee)
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        #====content_02=======
        # self.Ibl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd="3",relief="ridge",bg="light blue",fg="black",font=("goudy old style",20,"bold"))
        # self.Ibl_employee.place(x=700,y=120,height=150,width=300)

        #====content_03====
        self.lbl_supplier=Button(mainF,text="Total Suppliers\n[ 0 ]",bd="3",relief="ridge",bg="light blue",fg="black",font=("goudy old style",20,"bold"),command=self.supplier)
        self.lbl_supplier.place(x=700,y=120,height=150,width=300)


        #======content=====
        self.lbl_Category=Button(mainF,text="Total Category\n[ 0 ]",bd="3",relief="ridge",bg="light green",fg="black",font=("goudy old style",20,"bold"),command=self.Category)
        self.lbl_Category.place(x=1100,y=120,height=150,width=300)



        #content========
        self.lbl_product=Button(mainF,text="Total Products\n[ 0 ]",bd="3",relief="ridge",bg="light pink",fg="black",font=("goudy old style",20,"bold"),command=self.product)
        self.lbl_product.place(x=300,y=350,height=150,width=300)

        #content======
        self.lbl_sales=Button(mainF,text="Total Sales\n[ 0 ]",bd="3",relief="ridge",bg="light yellow",fg="black",font=("goudy old style",20,"bold"),command=self.sales)
        self.lbl_sales.place(x=700,y=350,height=150,width=300)
        #footer=====================================
        Ibl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by Vidyalankar Institute of Technology \n For any Technical issues : contact :- +91 9619659103",font=("times new roman",10),bg="#959594",fg="white")
        Ibl_footer.pack(side=BOTTOM,fill=X)

        self.update_content()

    def employee(self):
        empf.tkraise()
        # if hasattr(self, 'new_win'):  # check if a window is already open
        #     self.new_win.destroy()  # close the previous window
        # self.new_win = Toplevel(self.root)
        # self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        frames.tkraise()
        # if hasattr(self, 'new_win'):
        #     self.new_win.destroy()
        # self.new_win = Toplevel(self.root)
        # self.new_obj = supplierClass(self.new_win)

    def Category(self):
        framec.tkraise()
        # if hasattr(self, 'new_win'):
        #     self.new_win.destroy()
        # self.new_win = Toplevel(self.root)
        # self.new_obj = categoryClass(self.new_win)

    def product(self):
        framep.tkraise()
        # if hasattr(self, 'new_win'):
        #     self.new_win.destroy()
        # self.new_win = Toplevel(self.root)
        # self.new_obj = productClass(self.new_win)

    def sales(self):
        framesel.tkraise()
        # if hasattr(self, 'new_win'):
        #     self.new_win.destroy()
        # self.new_win = Toplevel(self.root)
        # self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_Category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')

            bill =(len(os.listdir('bill')))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.Ibl_clock.config(text=f"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Date:{str(date_)}\t\t Time : {str(time_)}") 
            self.Ibl_clock.after(200,self.update_content)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def logout(self):
        self.root.destroy()
        os.system("python login.py")            

if __name__=="__main__":
    root=CTk()

    frames = Frame(root,relief=RIDGE, bg="White")
    frames.place(x=210, y=105, width=1689, height=810)

    newsup = supplierClass(frames)

    framec = Frame(root, bg="White")
    framec.place(x=210, y=105, width=1689, height=810)
    newcat = categoryClass(framec)

    empf = Frame(root, bg="White")
    empf.place(x=210, y=105, width=1689, height=810)

    emp = employeeClass(empf)

    mainF = Frame(root, bd=4, relief=RIDGE, bg="White")
    mainF.place(x=210, y=105, width=1689, height=810)

    framep = Frame(root,relief=RIDGE, bg="White")
    framep.place(x=210, y=105, width=1689, height=810)
    newp = productClass(framep)

    framesel = Frame(root,relief=RIDGE, bg="White")
    framesel.place(x=210, y=105, width=1689, height=810)
    newsal = salesClass(framesel)

    obj=IMS(root)
    root.mainloop()

