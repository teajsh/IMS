from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkinter import ttk,messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
# from billing import BillClass
# from sales import salesClass
from product import productClass
import os
import sqlite3
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Sales Page | Developed by Vidyalankar Institute of Technology ")
        self.root.config(bg="white")
        self.root.focus_force()
        # self.root.resizable(width=False,height=False) 
      #===================================================================================
        self.bill_list=[]
        self.var_invoice=StringVar()

    #======title================================
        lbl_title=Label(self.root,text=" View Customer Bill ",bd=3,relief=RIDGE,font=("goudy old style",30,"bold"),bg="#184a45",fg="white")   
        lbl_title.pack(side=TOP,fill=X) 

        lbl_invoice=Label(self.root,text="Invoice Number :",font=("times new roman",12,"bold"),bg="white")
        lbl_invoice.place(x=50,y=100)

        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",12,"bold"),bg="light yellow")
        txt_invoice.place(x=175,y=100)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2")
        btn_search.place(x=360,y=100,width=120,height=28) 
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgrey",fg="black",cursor="hand2")
        btn_clear.place(x=490,y=100,width=120,height=28)


        #==================Frame==========================

        sales_Frame=Frame(self.root,bd=3,relief=RIDGE,)
        sales_Frame.place(x=700,y=100,width=200,height=330)

        
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        #=================bill area=================

        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=950,y=100,width=520,height=330)
        
        #============title in bill area====================
        lbl_title=Label(bill_Frame,text="Customer Bill Area ",font=("goudy old style",20,"bold"),bg="light green")   
        lbl_title.pack(side=TOP,fill=X)
        #================scroll bar in  bill area==================
        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("goudy old style",15),bg="light yellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
       
        # ================frame===========================================================
        sal_frame=Frame(self.root,bd=3,relief=RIDGE)
        sal_frame.place(x=0,y=450,relwidth=1,height=290)

         #_________scrolling____________________________

        scrolly=Scrollbar(sal_frame,orient=VERTICAL)
        scrollx=Scrollbar(sal_frame,orient=HORIZONTAL)
    #     cur.execute("CREATE TABLE IF NOT EXISTS sales(sid INTEGER PRIMARY KEY AUTOINCREMENT,invoice text,product_ID text,Product_Name text,Product_Price text,Quantity text,cname text,cphone text,netprice text)")
    # # con.commit() 
        self.salesTable=ttk.Treeview(sal_frame,columns=("sid","invoice","product_ID","Product_Name","Product_Price","Quantity","cname","cphone","netprice","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.salesTable.xview)
        scrolly.config(command=self.salesTable.yview)
        self.salesTable.heading("sid",text="SID")
        self.salesTable.heading("invoice",text="INVOICE")
        self.salesTable.heading("product_ID",text="Product ID")
        self.salesTable.heading("Product_Name",text="product Name")
        self.salesTable.heading("Product_Price",text="Price")
        self.salesTable.heading("Quantity",text="Quantity")
        self.salesTable.heading("cname",text="Name")
        self.salesTable.heading("cphone",text="Phone")
        self.salesTable.heading("netprice",text="Total_Price")
        self.salesTable.heading("date",text="Date")

        self.salesTable["show"]="headings"
        #=============================================================
        self.salesTable.column("sid",width=70,anchor="center")
        self.salesTable.column("invoice",width=100,anchor="center")
        self.salesTable.column("product_ID",width=100,anchor="center")
        self.salesTable.column("Product_Name",width=100,anchor="center")

        self.salesTable.column("Product_Price",width=100,anchor="center")
        self.salesTable.column("Quantity",width=100,anchor="center")
        self.salesTable.column("cname",width=100,anchor="center")
        self.salesTable.column("cphone",width=100,anchor="center")
        self.salesTable.column("netprice",width=100,anchor="center")
        self.salesTable.column("date",width=100,anchor="center")
        # self.salesTable.column("utype",width=100)
        # self.salesTable.column("salary",width=100)
        self.salesTable.bind("<ButtonRelease-1>",self.get_data)
        self.salesTable.pack(fill=BOTH,expand=1)

        self.shows()
        self.show()
              
#==============================================================================
    def show(self):
       del self.bill_list[:] 
       self.Sales_list.delete(0,END)
       for i in os.listdir('bill'):
           if i.split('.')[-1]=='txt':
              self.Sales_list.insert(END,i)
              self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        # self.bill_frame=file_name
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close() 
    def shows(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from sales")
            rows=cur.fetchall()
            self.salesTable.delete(*self.salesTable.get_children())   
            for row in rows:
               self.salesTable.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice Number should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
              fp=open(f'bill/{self.var_invoice.get()}.txt','r')
              self.bill_area.delete('1.0',END)
              for i in fp:
               self.bill_area.insert(END,i)
              fp.close() 
            else:
                messagebox.showerror("Error","Invoice number is Invalid",parent=self.root)         


    def clear(self):
        self.show()
        self.bill_area.delete("1.0",END)











if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()     