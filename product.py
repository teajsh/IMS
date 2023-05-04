import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x610+210+130")
        self.root.title("Product Page | Developed by Vidyalankar Institute of Technology ")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(width=False,height=False) 
        #==============variables=======================


        self.var_searchby=StringVar()   
        self.var_searchtxtx=StringVar() 

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()





        #================================================
        product_Frame=Frame(self.root,bd=7,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=490,height=580)    

        #==================title=========================
        title=Label(product_Frame,text="Manage Product Details",font=("times new roman",18,"bold"),bg="#B890FA",fg="white")
        title.pack(side=TOP,fill=X)
        
        #============category text=========================  
        lbl_category=Label(product_Frame,text="Category :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_category.place(x=5,y=50)


        #=============== supplier======================== 
        lbl_supplier=Label(product_Frame,text="Supplier :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_supplier.place(x=5,y=100)
        
   
        #================product Name===================
        lbl_product=Label(product_Frame,text="Product Name :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_product.place(x=5,y=150)
  
        #=================Price===========================
        lbl_price=Label(product_Frame,text="Price :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_price.place(x=5,y=50*4)

        #==================Quantity=========================
        lbl_quantity=Label(product_Frame,text="Quantity :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_quantity.place(x=5,y=50*5)

        #============status===================================
        lbl_status=Label(product_Frame,text="Status :",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_status.place(x=5,y=50*6)

        

        #==============TEXT_BOX===============================

        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_cat.place(x=150,y=50,width=300)
        cmb_cat.current(0)
         
        #===============Supplier combo box==================          
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_sup.place(x=150,y=100,width=300)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="light yellow")
        txt_name.place(x=150,y=150,width=300)
        

        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15,"bold"),bg="light yellow")
        txt_price.place(x=150,y=200,width=300)
         
        txt_quantity=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15,"bold"),bg="light yellow")
        txt_quantity.place(x=150,y=250,width=300) 

        # txt_status=Entry(product_Frame,textvariable=self.var_status,font=("goudy old style",15,"bold"),bg="light yellow")
        # txt_status.place(x=150,y=300,width=270)
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_status.place(x=150,y=300,width=300)
        cmb_status.current(0)
 
        #===================================button=====================================================================================
        #________button_Save_________________
        btn_Save=Button(product_Frame,text="Save",command=self.add,font=('goudy old style',20,"bold"),bg="#00C5FF",cursor="hand2")
        btn_Save.place(x=10,y=360,width=220,height=50) 

        #_______button_update_________________
        btn_Update=Button(product_Frame,text="Update",command=self.update,font=('goudy old style',15,"bold"),bg="light green",cursor="hand2")
        btn_Update.place(x=240,y=360,width=210,height=50)

        #_______________delete_button___________________________
        btn_delete=Button(product_Frame,text="Delete",command=self.delete1,font=('goudy old style',15,"bold"),bg="#FF3600",cursor="hand2")
        btn_delete.place(x=10,y=420,width=220,height=50)

        #_______________Clear_button___________________________
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=('goudy old style',15,"bold"),bg="#C4C4C4",cursor="hand2")
        btn_clear.place(x=240,y=420,width=210,height=50)

        

        #===================================================================+++++++++++++++++++++
         #Search frame=======
        SearchFrame=LabelFrame(self.root,text="Search Employee ",font=("goudy old style",12,"bold"),bg="white")
        SearchFrame.place(x=520,y=10,width=700,height=70)

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15,"bold"))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)



        #text_search=====
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxtx,font=('goudy old style',15,"bold"),bg="light yellow")
        txt_search.place(x=200,y=10,width=330)
        
        #button
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=('goudy old style',15,"bold"),bg="light green",cursor="hand2")
        btn_search.place(x=550,y=10,width=100,height=29)


        #=============================tree view=========================================
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=520,y=100,width=700,height=490)

        #_________scrolling____________________________

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid",text="Product_ID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Quantity")
        self.product_table.heading("status",text="Status")
    
        self.product_table["show"]="headings"
        #=============================================================
        self.product_table.column("pid",width=70)
        self.product_table.column("Category",width=100,anchor=CENTER)
        self.product_table.column("Supplier",width=100,anchor=CENTER)
        self.product_table.column("name",width=100,anchor=CENTER)
        self.product_table.column("price",width=100,anchor=CENTER)
        self.product_table.column("qty",width=100,anchor=CENTER)
        self.product_table.column("status",width=100,anchor=CENTER)
        
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.show()
        # self.fetch_cat_sup()
#=============================================================================================
    def fetch_cat_sup(self):
         self.cat_list.append("Empty")
         self.sup_list.append("Empty")
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
                cur.execute("Select name from category")
                cat=cur.fetchall()
                
                if len(cat)>0:
                  del self.cat_list[:]  
                  self.cat_list.append("Select")
                  for i in cat:
                    self.cat_list.append(i[0])
                
                cur.execute("Select name from supplier")
                sup=cur.fetchall()
                if len(sup)>0:  
                 del self.sup_list[:]  
                 self.sup_list.append("Select")
                 for i in sup:
                    self.sup_list.append(i[0])
                   

         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def add(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="Select":
                messagebox.showerror("Error","All fields must be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))   
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, try another one!!!",parent=self.root) 
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status)values(?,?,?,?,?,?)",(
                          self.var_cat.get(),
                          self.var_sup.get(),
                          self.var_name.get(),
                          self.var_price.get(),
                          self.var_qty.get(),
                          self.var_status.get(),
                         
                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Product Addedd Successfully....Done✅",parent=self.root)
                    self.show()

         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())   
            for row in rows:
               self.product_table.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
   
    def get_data(self,ev):
           f=self.product_table.focus()
           content=(self.product_table.item(f))
           row=content['values']
           self.var_pid.set(row[0])
           self.var_sup.set(row[1])
           self.var_cat.set(row[2])
           self.var_name.set(row[3])
           self.var_price.set(row[4])
           self.var_qty.set(row[5])
           self.var_status.set(row[6])
        
           
    
    def update(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
            
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from List",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID!",parent=self.root) 
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                          
                          self.var_cat.get(),
                          self.var_sup.get(),
                          self.var_name.get(),
                          self.var_price.get(),
                          self.var_qty.get(),
                          self.var_status.get(),
                          self.var_pid.get()

                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Product Table Updated Successfully....Done✅",parent=self.root)
                    self.show()
                       


         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete1(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))   
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID!",parent=self.root) 
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to Delete",parent=self.root)
                    if op==TRUE:
                      cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                      con.commit()
                      messagebox.showinfo("Delete","Successfully Deleted Data...!!",parent=self.root)
                      self.clear()
                    


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

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
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxtx.get()=="":
                messagebox.showerror("Error","Search input should be required...!!!!",parent=self.root)
            else:    

             cur.execute("Select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxtx.get()+"%'")
             rows=cur.fetchall()
             if len(rows)!=0:

                self.product_table.delete(*self.product_table.get_children())   
                for row in rows:
                  self.product_table.insert('',END,values=row)
             else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()       