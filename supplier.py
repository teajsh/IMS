from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        # self.root=root
        # self.root.geometry("1300x610+210+130")
        # self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        # self.root.config(bg="light blue")
        # self.root.focus_force()
        # self.root.resizable(width=False,height=False)
        
        #All variables=========================================
        self.var_searchby=StringVar()   
        self.var_searchtxtx=StringVar()       


        self.var_sup_invoice=StringVar() 
        self.var_name=StringVar()
        self.var_contact=StringVar()
        


        #=======================================Search frame=====================================
        SearchFrame=LabelFrame(self.root,text="Search Employee ",font=("goudy old style",12,"bold"),bg="white")
        SearchFrame.place(x=200,y=20,width=900,height=70)


        #+++++++++++++++++++++++++++++++++++combo_box_search+++++++++++++++++++++++++=======+++++++
        lbl_search=Label(SearchFrame,text="Search by invoice no.",bg="white",font=("goudy old style",15,"bold"))
        lbl_search.place(x=10,y=10)
        # lbl_search.current(0)

        #==================================text_search====================================================
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxtx,font=('goudy old style',15,"bold"),bg="light yellow")
        txt_search.place(x=200,y=10,width=330)
        #====================================button========================================================
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=('goudy old style',15,"bold"),bg="light green",cursor="hand2")
        btn_search.place(x=550,y=10,width=100,height=29)
        

        #======title=======
        title=Label(self.root,text="Supplier Details",font=("times new roman",15,"bold"),bg="#B890FA",fg="white")
        title.place(x=50,y=100,width=1200)
        
        #====contents======
        #=============================row_01==========================================================================================
        emp_supplier_invoice=Label(self.root,text="*Emp ID :",font=("times new roman",15,"bold"),bg='light blue')
        emp_supplier_invoice.place(x=50,y=140)

       

        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_supplier_invoice.place(x=141,y=140,width=400)

        

        
        #=====================row_02====================================================================================================

        lbl_Name=Label(self.root,text="Name :-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_Name.place(x=50,y=180)

       
        txt_Name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_Name.place(x=141,y=180,width=400)
        
      
        #===================row3=========================================================================================================

        lbl_contact=Label(self.root,text="Contact:",font=("times new roman",15,"bold"),bg='light blue')
        lbl_contact.place(x=50,y=220)     

       
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg='Light yellow')
        txt_contact.place(x=141,y=220,width=400)
        
       
        
        #=============================row4========================================================================================

        lbl_desc=Label(self.root,text="Description:-",font=("times new roman",15,"bold"),bg='light blue')
        lbl_desc.place(x=50,y=260)     

        self.text_desc=Text(self.root,font=("times new roman",15,"bold"),bg='Light yellow')
        self.text_desc.place(x=151,y=260,width=520,height=100)
        
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

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
        #_____________________________________________________________
        self.supplierTable["show"]="headings"
        #=============================================================
        self.supplierTable.column("invoice",width=70)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #=============================================================================================
    
    def add(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))   
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No. is already taken try another one!!!",parent=self.root) 
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc)values(?,?,?,?)",(
                          self.var_sup_invoice.get(),
                          self.var_name.get(),
                          self.var_contact.get(),
                          self.text_desc.get('1.0',END),
                          

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","supplier Addedd Successfully....Done✅",parent=self.root)
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
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())   
            for row in rows:
               self.supplierTable.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def get_data(self,ev):
           f=self.supplierTable.focus()
           content=(self.supplierTable.item(f))
           row=content['values']
           #print(row)
           self.var_sup_invoice.set(row[0]),
           self.var_name.set(row[1]),
           self.var_contact.set(row[2]),
           self.text_desc.delete('1.0',END),
           self.text_desc.insert(END,row[3]),
          
    
    def update(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice =?",(self.var_sup_invoice.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice No.!",parent=self.root) 
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                          
                          self.var_name.get(),
                          self.var_contact.get(),
                          self.text_desc.get('1.0',END),
                          self.var_sup_invoice.get(),

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully....Done✅",parent=self.root)
                    self.show()     
                       


         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete1(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number !",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==TRUE: 
                      cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                      con.commit()
                      messagebox.showinfo("Delete","Successfully Deleted Data...!!",parent=self.root)
                      self.clear()
                    


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        # con=sqlite3.connect(database=r'ims.db')
        # cur=con.cursor() 
        # try:
           self.var_sup_invoice.set("")
           self.var_name.set("")
           
           self.var_contact.set("")
           
           self.text_desc.delete('1.0',END)
        #    self.text_desc.insert(END,row[9]),
         
           self.var_searchtxtx.set("")
           
           
           self.show()




    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxtx.get()=="":
                messagebox.showerror("Error","Invoice number is required...!!!!",parent=self.root)
            else:    
             cur.execute("Select * from supplier where invoice=?",(self.var_searchtxtx.get(),))
             row=cur.fetchone()
             if row!=None:

                self.supplierTable.delete(*self.supplierTable.get_children())   
                self.supplierTable.insert('',END,values=row)
             else:
                messagebox.showerror("Error","No record found",parent=self.root)

              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()        