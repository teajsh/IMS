import smtplib
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from sales import *
import time
import datetime
# import re
import sqlite3
import os
import tempfile   #temperory file generate karega
# from employee import employeeClass
# from supplier import supplierClass
# from category import categoryClass
from sales import *
import re


# from product import productClass
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1520x790+0+0")
        self.root.title("Inventory Management System | Developed by Vidyalankar Institute of Technology ")
        self.root.config(bg="white")
        self.cart_list=[]
        self.invoice:int
        self.chk_print =0
        self.pro_list =[]
        #title=========
        self.icon_title=PhotoImage(file="Images/icons8-in-inventory_logo-64.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="Light Blue",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=70)
       


        #button_logout======
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="Yellow",cursor="hand2").place(x=1340,y=12,height=45,width=150)

        #clock======
        self.Ibl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time : HH:MM:SS",font=("times new roman",15),bg="#0000FF",fg="white")
        self.Ibl_clock.place(x=0,y=71,relwidth=1,height=30)
        

        #=============product frame=========================
        self.var_search=StringVar()
       
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
        ProductFrame1.place(x=7,y=110,height=620,width=500)

 
        ptitle=Label(ProductFrame1,text="All Product",font=("goudy old style",20,"bold"),bg="light blue")
        ptitle.pack(side=TOP,fill=X)

        #==========product search frame==============
        ProductFrame2=Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=43,height=90,width=487)
       
        lbl_search=Label(ProductFrame2,text="Search Product | By name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5) 

        lbl_search=Label(ProductFrame2,text="Product Name :",font=("times new roman",15,"bold"),bg="white").place(x=2,y=40)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",12),bg="light yellow").place(x=140,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",font=("goudy old style",15),command = self.search,bg="#2196f3",fg="white",cursor="hand2").place(x=300,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",font=("goudy old style",15),command = self.show,bg="#083531",fg="white",cursor="hand2").place(x=300,y=10,width=100,height=25)

        #==========product details frame=======================
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=487,height=444)

        #_________scrolling____________________________

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="PID",anchor=CENTER)
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        #_____________________________________________________________
        self.product_Table["show"]="headings"
        #=============================================================
        self.product_Table.column("pid",width=30,anchor=CENTER)
        self.product_Table.column("name",width=100,anchor=CENTER)
        self.product_Table.column("price",width=100,anchor=CENTER)
        self.product_Table.column("qty",width=30,anchor=CENTER)
        self.product_Table.column("status",width=100,anchor=CENTER)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,anchor='w',text="Note : 'Entry 0 quantity to remove from product from the Cart'",font=("goudy old style",10,"bold"),fg="red")
        lbl_note.pack(side=BOTTOM,fill=X)


        #====================Customer frame ====================================

        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.var_malling = StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=510,y=110,height=150,width=500)
        

        ctitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",20,"bold"),bg="light blue")
        ctitle.pack(side=TOP,fill=X)

        
        lbl_name=Label(CustomerFrame,text="Name :",font=("times new roman",15,"bold"),bg="white").place(x=6,y=40)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",12),bg="light yellow").place(x=140,y=47,width=160,height=22)


        lbl_contact=Label(CustomerFrame,text="Contact :",font=("times new roman",15,"bold"),bg="white").place(x=6,y=80)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",12),bg="light yellow").place(x=140,y=87,width=160,height=20)

        lbl_mail=Label(CustomerFrame,text="E-Mail :",font=("times new roman",15,"bold"),bg="white").place(x=6,y=80+30)

        txt_mail=Entry(CustomerFrame,textvariable=self.var_malling,font=("times new roman",12),bg="light yellow").place(x=140,y=87+30,width=240,height=20)

        #======== cal cart frame==================== 
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=510,y=260,height=360,width=500)

        #========Calculator frame==================== 
        self.var_cal_input = StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=2,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,height=340,width=261)

        txt_cal_input = Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width="22",bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

       
        btn_7 = Button(Cal_Frame,text = "7",font=("arial",14,"bold",),command = lambda:self.get_input(7),bd=3,width=4,pady=13,cursor="hand2").grid(row=1,column=0)
        btn_8 = Button(Cal_Frame,text = "8",font=("arial",14,"bold",),command = lambda:self.get_input(8),bd=3,width=4,pady=13,cursor="hand2").grid(row=1,column=1)
        btn_9 = Button(Cal_Frame,text = "9",font=("arial",14,"bold",),command = lambda:self.get_input(9),bd=3,width=4,pady=13,cursor="hand2").grid(row=1,column=2)
        btn_sum = Button(Cal_Frame,text = "+",font=("arial",14,"bold",),command = lambda:self.get_input('+'),bd=3,width=4,pady=13,cursor="hand2").grid(row=1,column=3)
        #====================w====================
        btn_4 = Button(Cal_Frame,text = "4",font=("arial",14,"bold",),command = lambda:self.get_input(4),bd=5,width=4,pady=13,cursor="hand2").grid(row=2,column=0)
        btn_5 = Button(Cal_Frame,text = "5",font=("arial",14,"bold",),command = lambda:self.get_input(5),bd=5,width=4,pady=13,cursor="hand2").grid(row=2,column=1)
        btn_6 = Button(Cal_Frame,text = "6",font=("arial",14,"bold",),command = lambda:self.get_input(6),bd=5,width=4,pady=13,cursor="hand2").grid(row=2,column=2)
        btn_sub = Button(Cal_Frame,text = "-",font=("arial",14,"bold",),command = lambda:self.get_input('-'),bd=5,width=4,pady=13,cursor="hand2").grid(row=2,column=3)
        #=====================w===================
        btn_1 = Button(Cal_Frame,text = "1",font=("arial",14,"bold",),command = lambda:self.get_input(1),bd=5,width=4,pady=13,cursor="hand2").grid(row=3,column=0)
        btn_2 = Button(Cal_Frame,text = "2",font=("arial",14,"bold",),command = lambda:self.get_input(2),bd=5,width=4,pady=13,cursor="hand2").grid(row=3,column=1)
        btn_3= Button(Cal_Frame,text = "3",font=("arial",14,"bold",),command = lambda:self.get_input(3),bd=5,width=4,pady=13,cursor="hand2").grid(row=3,column=2)
        btn_mul = Button(Cal_Frame,text = "x",font=("arial",14,"bold",),command = lambda:self.get_input('*'),bd=5,width=4,pady=13,cursor="hand2").grid(row=3,column=3)
        #====================w====================
        btn_0 = Button(Cal_Frame,text = "0",font=("arial",14,"bold",),command = lambda:self.get_input(0),bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=0)
        btn_c = Button(Cal_Frame,text = "c",font=("arial",14,"bold",),command = self.clear_cal,bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=1)
        btn_eq= Button(Cal_Frame,text = "=",font=("arial",14,"bold",),command = self.perform_cal,bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=2)
        btn_div = Button(Cal_Frame,text = "/",font=("arial",14,"bold",),command = lambda:self.get_input('/'),bd=5,width=4,pady=13,cursor="hand2").grid(row=4,column=3)
       
       
        

        #======== cart frame==================== 
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=270,y=10,width=220,height=340)
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Product : [0]",font=("goudy old style",12,"bold"),bg="light blue")
        self.cartTitle.pack(side=TOP,fill=X)

        #_________scrolling____________________________

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        # self.CartTable.heading("status",text="Status")
        #_____________________________________________________________
        self.CartTable["show"]="headings"
        #=============================================================
        self.CartTable.column("pid",width=50,anchor=CENTER)
        self.CartTable.column("name",width=100,anchor=CENTER)
        self.CartTable.column("price",width=90,anchor=CENTER)
        self.CartTable.column("qty",width=90,anchor=CENTER)
        # self.CartTable.column("status",width=90,anchor=CENTER)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #========ADD cart widgets frame==================== 
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        # self.invoice = StringVar()

        

        Add_CartWidgetsFrame=Frame(self.root,bd=3,relief=RIDGE)
        Add_CartWidgetsFrame.place(x=510,y=620,width=500,height=110)
        
        
        lbl_p_name = Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15,"bold"),bg="light grey").place(x=5,y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",10,"bold"),bg="light yellow",state='readonly').place(x=5,y=35,width=180,height=22)

        lbl_p_price = Label(Add_CartWidgetsFrame,text="Price per qty",font=("times new roman",15,"bold"),bg="light grey").place(x=200,y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",10,"bold"),bg="light yellow",state='readonly').place(x=190,y=35,width=180,height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15,"bold"),bg="light grey").place(x=390,y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",10,"bold"),bg="lightyellow").place(x=380,y=35,width=100,height=22)
        
        self.lbl_inStock = Label(Add_CartWidgetsFrame,text="In stock [0]",font=("times new roman",15,"bold"))
        self.lbl_inStock.place(x=5,y=70)
        
        btn_clear_cart = Button(Add_CartWidgetsFrame,command=self.clear_cart,text="Clear",font=("times new roman",15,"bold"),cursor="hand2",bg="light green").place(x=150,y=70,width="103",height="23")
        btn_add_cart = Button(Add_CartWidgetsFrame,text="Add",command=self.add_update_cart,font=("times new roman",15,"bold"),cursor="hand2",bg="light green").place(x=260,y=70,width="103",height="23")
        # btn_update_cart = Button(Add_CartWidgetsFrame,text="Update",font=("times new roman",15,"bold"),cursor="hand2",bg="light green").place(x=370,y=70,width="103",height="23")
       

        #========================billing area ======================================

        billFrame = Frame(self.root,bd=3,relief=RIDGE,bg='white')
        billFrame.place(x=1015,y=110,width=500,height=470)

        BTitle = Label(billFrame,text ="Customer Bill Area",font=("goudy old style",20,"bold"),bg="light blue")
        BTitle.pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area = Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        
        #==================billing buttons====================
        billMenuFrame = Frame(self.root,bd=3,relief=RIDGE,bg='white')
        billMenuFrame.place(x=1015,y=584,width=500,height=147)

        self.lbl_amnt = Label(billMenuFrame,text="Bill amount\n[0]",font=("goudy old style",15,"bold"),bg="light green",bd="7",fg="Black")
        self.lbl_amnt.place(x=2,y=5,width=160,height=70)
        
        self.lbl_discount = Label(billMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="light grey")
        self.lbl_discount.place(x=164,y=5,width=160,height=70)
        
        self.lbl_net_pay = Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#FE6244",fg="white")
        self.lbl_net_pay.place(x=326,y=5,width=160,height=70)
        #============button===============
        btn_print = Button(billMenuFrame,text="Print",command=self.print_bill,font=("goudy old style",14,"bold"),bg="#57C5B6",fg="Black",cursor="hand2")
        btn_print.place(x=2,y=78,width=160,height=60)
        
        btn_clear_all = Button(billMenuFrame,text="Clear ALL",command=self.clear_all,font=("goudy old style",14,"bold"),bg="#D61355",cursor="hand2",fg="white")
        btn_clear_all.place(x=164,y=78,width=160,height=60)
        
        btn_generate = Button(billMenuFrame,command=self.generate_bill,text="Generate Bill/\nSave Bill",font=("goudy old style",14,"bold"),bg="#FFED00",fg="black",cursor="hand2")
        btn_generate.place(x=326,y=78,width=160,height=60)






    #=====================Footer Part +===================================
        Ibl_footer=Label(self.root,text="IMS-Inventory Management System | Developed by Vidyalankar Institute of Technology \n For any Technical issues : contact :- +91 9619659103",font=("times new roman",15),bg="#959594",fg="black")
        Ibl_footer.pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_top()
        self.update_date_time()



    #all functions=========== #======================================
    def get_input(self,num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)
    def clear_cal(self):
        self.var_cal_input.set('')
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    #  self.product_table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,price,qty,status from product where status = 'Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())   
            for row in rows:
               self.product_Table.insert('',END,values=row)
           
              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
           
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required...!!!!",parent=self.root)
            else:    

             cur.execute("Select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status = 'Active'")
             rows=cur.fetchall()
             if len(rows)!=0:

                self.product_Table.delete(*self.product_Table.get_children())   
                for row in rows:
                  self.product_Table.insert('',END,values=row)
             else:
                messagebox.showerror("Error","No record found",parent=self.root)

              
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
           f=self.product_Table.focus()
           content=(self.product_Table.item(f))
           row=content['values']
           self.var_pid.set(row[0])
           self.var_pname.set(row[1]) 
           self.var_price.set(row[2]) 
           self.lbl_inStock.config(text=f'In stock [{str(row[3])}]')
           self.var_stock.set(row[3])
           self.var_qty.set('1')

    def get_data_cart(self,ev):
           f=self.CartTable.focus()
           content=(self.CartTable.item(f))
           row=content['values']
           self.var_pid.set(row[0])
           self.var_pname.set(row[1]) 
           self.var_price.set(row[2]) 
           self.var_qty.set(row[3])
           self.lbl_inStock.config(text=f'In stock [{str(row[4])}]')
           self.var_stock.set(row[4])
           
    def add_update_cart(self):
           if self.var_pid.get() =='':
               messagebox.showerror("Error","please entry the price.",parent=self.root)
           elif self.var_qty.get() == '':
               messagebox.showerror("Error","Please entry the quantity and Price.",parent=self.root)
           elif int(self.var_qty.get())>int(self.var_stock.get()):
               messagebox.showerror("Error","OUt of stock..",parent=self.root)
           else:   
            #    price_cal = int(self.var_qty.get())*float(self.var_price.get())  
            #    price_cal = float(price_cal)
               price_cal = self.var_price.get()  
            
               cart_data =[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #    self.cart_list.append(cart_data)
               #======update cart====================
               present = 'no'
               index_ = 0
               for row in self.cart_list:
                   if self.var_pid.get()==row[0]:
                       present='yes'
                       break
                   index_+=1   
               if present=='yes':
                   op=messagebox.askyesno('Confirm',"Product already present \n Do you want to update | Remove from the cart list?",parent=self.root)
                   if op == True:
                       if self.var_qty.get()=="0":
                           self.cart_list.pop(index_)
                       else:
                        #    self.cart_list[index_][2]=price_cal
                           self.cart_list[index_][3]=self.var_qty.get()
               else:            
                     self.cart_list.append(cart_data)
                     self.pro_list.append(self.var_pname.get())    
               self.show_cart()
               self.bill_update()
    def bill_update(self):
        self.bill_amnt =0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount =  (self.bill_amnt*5)/100  
        self.net_pay = (self.bill_amnt)-(self.discount)
        self.lbl_amnt.config(text=f'Bill Amount(Rs.)\n[{str(self.bill_amnt)}]')    
        self.lbl_net_pay.config(text=f'Net Pay(Rs.)\n[{str(self.net_pay)}]')    
        self.cartTitle.config(text=f"Cart \t Total Product : [{str(len(self.cart_list))}]")


    def show_cart(self):
           
            try:
              self.CartTable.delete(*self.CartTable.get_children())   
              for row in self.cart_list:
               self.CartTable.insert('',END,values=row)
           
              
            except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_cname.get() == '':
            messagebox.showerror("Error", f"Enter the Customer Name !! ", parent=self.root)
        elif not self.var_contact.get().isdigit() or len(self.var_contact.get()) != 10:
            messagebox.showerror("Error", f"Enter a valid 10-digit Contact Number!!", parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", f"Please select the product..", parent=self.root)
        elif self.var_malling.get() == '':
            messagebox.showerror("Error", f"mail ID is required", parent=self.root)
        elif not self.is_valid_email(self.var_malling.get()) :
            messagebox.showerror("Error", f"mail ID is not valid", parent=self.root)

        else:
            # rest of the code to generate the bill
            # ==============top bill=============
            self.bill_top()
            # ============middle bill=============
            self.bill_middle()
            # ===============down bill==============
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo("Saved", "SuccessFully Saved", parent=self.root)
            self.chk_print = 1
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            cur.execute(
                "Insert into sales (invoice,product_ID,Product_Name,Product_Price,Quantity,cname,cphone,netprice,date)values(?,?,?,?,?,?,?,?,?)",
                (
                    str(self.invoice),
                    self.var_pid.get(),
                    str(self.pro_list),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_cname.get(),
                    self.var_contact.get(),
                    str(self.net_pay),
                    str(datetime.date(2023, 4, 20))
                ))
            con.commit()
            self.show()
            self.check_quantity()
            self.send_email_to_c()

    def is_ten_digit(num):
        """
        Returns True if the given number is exactly 10 digits long, else returns False.
        """
        if not isinstance(num, int):
            # Check if the input is an integer
            return False
        elif len(str(num)) != 10:
            # Check if the integer has exactly 10 digits
            return False
        else:
            return True

    import smtplib

    def check_quantity(self):

        if (int(self.var_stock.get()) - int(self.var_qty.get())) < 50:
                print(f"this is stock{self.var_stock.get()}")
                print(f"this is qty{self.var_qty.get()}")

                # Quantity is less than 0, send email to admin
                sender_email = "tkamble1902@gmail.com"
                receiver_email = "tejas.kamble@vit.edu.in"
                password = "lktktpokobcgpfdh"
                message = f"Subject: Quantity Error\n\nProduct {self.var_pname.get()} quantity is  {int(self.var_stock.get()) - int(self.var_qty.get())} ."
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(sender_email, password)
                    smtp.sendmail(sender_email, receiver_email, message)
                # messagebox.showerror("Error", f"Product {item[1]} quantity is less than 0.", parent=self.root)
                # return False
        # return True

        # for item in self.cart_list:
    def send_email_to_c(self):
        # Quantity is less than 0, send email to admin
        sender_email = "tkamble1902@gmail.com"
        receiver_email = self.var_malling.get()
        password = "lktktpokobcgpfdh"
        message = f"Subject: Thank you \n\nProduct {self.var_pname.get()} quantity is  {self.var_qty.get()} ."
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, message)

    def is_valid_email(self, email):
        """
        Returns True if the given string is a valid email address, else returns False.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S"))+ int(time.strftime("%d%m%Y"))
        bill_top_temp= f'''    
\t\tInventory Management
\tPhone No. 9834938*** , Mumbai-400018
{str("="*47)}
Customer Name : {self.var_cname.get()}
Phone No. : {self.var_contact.get()}
Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
Product Name\t\t\tQTY\tPrice
{str("="*47)}    
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
    
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                pid = row[0]
                name = row[1]
                qty = int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status = 'Inactive'
                if int(row[3])!=int(row[4]):
                    status = 'Active'    
                price = float(row[2])*int(row[3])
                price = str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+price)
                #update qty in product table================================
                cur.execute('Update product set qty=?,status=? where pid=?',(
                  qty,
                  status,
                  pid
                ))
                con.commit()
            con.close()     
            # self.shows()
        except Exception as ex:
                 messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)         

            # self.txt_bill_area.insert()

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tRs.{self.bill_amnt}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n          
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)


    def clear_cart(self):    
        self.var_pid.set('')
        self.var_pname.set('') 
        self.var_price.set('') 
        self.var_qty.set('')
        self.lbl_inStock.config(text=f'In stock ')
        self.var_stock.set('')
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product : [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.Ibl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{str(date_)}\t\t Time : {str(time_)}") 
        self.Ibl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing..",parent=self.root)
            new_file =tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')  
        else:
            messagebox.showerror("Error","Bill is Not Generated....!",parent=self.root)
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
            
                 
if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()        