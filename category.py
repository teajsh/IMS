from tkinter import *
import sqlite3
# from tkinter import * 
from tkinter import ttk,messagebox
# from PIL import Image,ImageTk
# from employee import employeeClass
# from supplier import supplierClass
class categoryClass:
    def __init__(self,root):
        self.root=root
        framec.place(x=100,y=00 ,width=1200,height=800)
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Manage Product Category | Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="white")
        # self.root.resizable(width=False,height=False)

        #=======variables==========================#
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #=================title==================
        lbl_title=Label(self.root,text="Manage Product Category",bd=3,relief=RIDGE,font=("goudy old style",30,"bold"),bg="#184a45",fg="white")
        # lbl_title.place(x=0,y=0,height=60,relwidth=1)
        lbl_title.pack(side=TOP,fill=X)
        
        lbl_title=Label(self.root,text=" Enter Category Name",font=("goudy old style",25,"bold"),bg="white",fg="#184a45")
        lbl_title.place(x=40,y=100)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="light yellow",fg="black")
        txt_name.place(x=50,y=150,width=270)
         
        # +=============button_01===================
        
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",20,"bold"),bg="light green",fg="black",cursor="hand2")
        btn_add.place(x=350,y=150,height=38,width=170)
        #==============button02 +=================
        
        
        btn_delete=Button(self.root,text="Delete",command=self.delete1,font=("goudy old style",20,"bold"),bg="red",fg="white",cursor="hand2")
        btn_delete.place(x=550,y=150,height=38,width=170)
        


        # +++++++++++++++++tree view________________====================

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=750,y=100,width=480,height=450)

        #_________scrolling____________________________

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("category_ID","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("category_ID",text="Category_ID")
        self.category_table.heading("name",text="Name")
        # self.category_table.heading("contact",text="Contact")
        # self.category_table.heading("desc",text="D escription")
        #_____________________________________________________________
        self.category_table["show"]="headings"
        #=============================================================
        self.category_table.column("category_ID",width=70)
        self.category_table.column("name",width=100)  
        # self.category_table.column("contact",width=100)
        # self.category_table.column("desc",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        # ====Category========================================

        lbl_txt=Label(self.root,text="=====================Category list===================",font=("goudy old style",15,"bold"),fg="black",bg="white").place(x=100,y=200)
        self.show()
# ==============================function================

    def add(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name is required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))   
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present try another one!!!",parent=self.root) 
                else:
                    cur.execute("Insert into category(name)values(?)",(
                          self.var_name.get(),
                        #   self.var_name.get(),
                        #   self.var_contact.get(),
                        #   self.text_desc.get('1.0',END),
                          

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Category Addedd Successfully....Done✅",parent=self.root)
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
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())   
            for row in rows:
               self.category_table.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    

    def get_data(self,ev):
           f=self.category_table.focus()
           content=(self.category_table.item(f))
           row=content['values']
           #print(row)
           self.var_cat_id.set(row[0])
           self.var_name.set(row[1])

    def delete1(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select category from the list....",parent=self.root)
            else:
                cur.execute("Select * from category where category_ID=?",(self.var_cat_id.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error,please try again !",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==TRUE: 
                      cur.execute("delete from category where category_ID=?",(self.var_cat_id.get(),))
                      con.commit()
                      messagebox.showinfo("Delete","Successfully Deleted Data...!!",parent=self.root)
                    #   self.clear()
                      self.show()
                      self.var_cat_id.set("")
                      self.var_name.set("")
                    


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)








if __name__=="__main__":
    root=Tk()
    framec = Frame(root)
    obj=categoryClass(framec)
    root.mainloop()
