from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
from tkcalendar import DateEntry
from datetime import datetime
import sqlite3

conn=sqlite3.connect('taxiwala_maatevinatuga')
c=conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS user(emailid text, username text, password text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS cab(username text, user_from text, user_to text, user_date text, cabtype text,
              base_fare int, total int)''')
c.execute(''' CREATE TABLE IF NOT EXISTS cab1(username text, user_from text, user_to text, user_date text, cabtype text,
              base_fare int, total int)''')



def main():
    win=Tk()
    app=main_window(win)
    win.mainloop()
    
    
    
class main_window:
    def __init__(self,root):
        self.root=root
        self.root.title("CAB BOOKING MANAGEMENT SYSTEM")
        self.root.geometry("1600x900+0+0")

        self.txtReceipt1=StringVar()
        self.txtReceipt2=StringVar()
        

        
        #create canvas
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)

        Login_frame=Frame(self.root,bg='black')
        Login_frame.place(x=550,y=170,height=400,width=350)

        welcome_frame=Frame(self.root,bg="black")
        welcome_frame.place(x=350,y=60,width=800,height=70)

        canvas_logo=Canvas(welcome_frame,width=10,height=10,bg="black")
        canvas_logo.pack(fill=BOTH, expand=True)
        
        welcome_label=Label(welcome_frame,text="WELCOME TO OLA CAB SERVICES!!",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label.place(x=100,y=10)

        
        login_label=Label(Login_frame,text="LOGIN HERE",font=("comic sans MS","22","bold"),fg="red",bg="black")
        login_label.place(x=75,y=15)

        #username label
        username_label=Label(Login_frame,text="USERNAME",font=("GOUDY OLD STYLE","15"),fg="white",bg="black")
        username_label.place(x=25 ,y=90)

        #entry for getting the username from the user
        self.username_entry=Entry(Login_frame,font=("times new roman","12","bold"),bg="lightgray")
        self.username_entry.place(x=25,y=125,width=270,height=25)

        #password label
        password_label=Label(Login_frame,text="PASSWORD",font=("GOUDY OLD STYLE","15"),fg="white",bg="black")
        password_label.place(x=25 ,y=190)

        #entry for getting password from the user
        self.password_entry=Entry(Login_frame,font=("times new roman","12","bold"),bg="lightgray",show="*")
        self.password_entry.place(x=25,y=225,width=270,height=25)

        btn1=Button(Login_frame,text="FORGOT PASSWORD?",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.forgot_password_window)
        btn1.place(x=35,y=340)

        btn2=Button(Login_frame,text="Login",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=1,command=self.login)
        btn2.place(x=100,y=300)

        btn3=Button(Login_frame,text="NOT REGISTERED? REGISTER",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.register_window)
        btn3.place(x=35,y=360)

    def register_window(self):
        self.new_window=Toplevel()
        self.app=Register(self.new_window)


# ========================================================================================================================
# =================================================LOGIN DATA=============================================================
# ========================================================================================================================
    def login(self):
        if self.username_entry.get()=='' or self.password_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required')

        else:
            
            c.execute('select * from user where username= ? and password= ?',(self.username_entry.get(),self.password_entry.get()))
            row=c.fetchone()

            
            if row==None:
                messagebox.showerror('Error','Invalid Username And Password')
                

            else:
                
                conn.commit()
                #c.close()
                messagebox.showinfo('Success','WELCOME TO CAB SERVICES')
                self.cab_page()



# ========================================================================================================================
# =================================================RESET PASSWORD=============================================================
# ========================================================================================================================
    def reset_password(self):
        if self.new_password_entry.get()=='' or self.new_confirm_password_entry.get() :
            messagebox.showerror('Error','All Fields Are Required')
        elif self.new_password_entry.get()!=self.new_confirm_password_entry.get():
            messagebox.showerror('Error','Password Does Not Match')

        else:
            
            value=(self.username_entry.get())
            c.execute("Select * from user where username =?",(value))
            row=c.fetchone()
            query=('update user set password=? where username=?')
            value=(self.new_password_entry.get(),self.username_entry.get())
            c.execute(query,value)
            conn.commit()
            c.close()
            messagebox.showinfo('Successful','Your Password Has Been Reset,Please Login Again')

       

# ========================================================================================================================
# =================================================FORGOT PASSWORD=============================================================
# ========================================================================================================================
    def forgot_password_window(self):
        self.var_password_entry=StringVar()
        self.var_new_password_entry=StringVar()
        self.var_confirm_password_entry=StringVar()

        
        if self.username_entry.get()=='':
            messagebox.showerror('Error','Please Enter Valid Username')
        else:
            
            value=(self.username_entry.get(),)
            c.execute('Select * from user where username = ?',(value))
            row=c.fetchone()
            print(row)

            if row==None:
                messagebox.showerror('Error','Invalid Username')

            else:
                c.close()
                self.root2=Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('340x450+610+170')

                self.root2['bg']='black'
                l=Label(self.root2,text='Forgot Password',font=("comic sans MS","22","bold"),fg="red",bg='black')
                l.place(x=0,y=10,relwidth=1)
                self.new_password_label=Label(self.root2,text='NEW PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=80)
                self.new_password_entry=Entry(self.root2,font=("times new roman","12","bold"),bg="lightgray",textvariable=self.var_new_password_entry,show="*")
                self.new_password_entry.place(x=25,y=110,width=300,height=25)
                self.new_confirm_password_label=Label(self.root2,text='CONFIRM PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=140)
                self.new_confirm_password_entry=Entry(self.root2,font=("times new roman","12","bold"),bg="lightgray",textvariable=self.var_confirm_password_entry,show="*")
                self.new_confirm_password_entry.place(x=25,y=170,width=300,height=25)
                self.submit_button=Button(self.root2,text="SUBMIT",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=2,command=self.reset_password).place(x=100,y=250)

    def cab_page(self):
        #create canvas
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)
        Frm=Frame(self.root,bg="yellow")
        Frm.place(x=550,y=170,height=400,width=350)
        
        self.cabs_frame1=Frame(self.root,bg="Red")
        self.cabs_frame1.place(x=630,y=250,width=200,height=100)
        search_btn=Button(self.cabs_frame1,text="Daily",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.from_drop1)
        search_btn.place(x=60,y=20)
        self.cabs_frame1=Frame(self.root,bg="Red")
        self.cabs_frame1.place(x=630,y=400,width=200,height=100)
        search_btn=Button(self.cabs_frame1,text="Outstation",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.from_drop)
        search_btn.place(x=30,y=20)
        
    def from_drop_data1(self):

        if self.L6_combo.get()=='' or self.L7_combo.get()=='':
            messagebox.showerror('Error','All fields are required')

        if self.L6_combo.get()=='Thiruvanmiyur' or self.L7_combo.get()=='Thiruvanmiyur':
            messagebox.showerror('Error','Please select your cities')

        if self.L6_combo.get()=='Adyar' and self.L7_combo.get()=='Adyar':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        if self.L6_combo.get()=='Airport' and self.L7_combo.get()=='Airport':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')
        
        if self.L6_combo.get()=='Railway Station' and self.L7_combo.get()=='Railway Station':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        else:
            try:
                c.execute("insert into cab1(username,user_from,user_to,user_date,cabtype,base_fare,total)values(?,?,?,?,?,?,?)",
                                 [self.username_entry.get(),self.L6_combo.get(),self.L7_combo.get(),self.cal.get(),self.cabtypefun1(),
                                 self.from_to_fare1(),self.sumoffare1()])
                conn.commit()
                c.close()
                messagebox.showinfo('Success',"BOOKING SUCCESSFUL, ENJOY YOUR RIDE!!",parent=self.root)
                

            except Exception as es:
                messagebox.showerror('Error',f'Error due to: {str(es)}',parent=self.root)




    def from_drop1(self):

        self.root=Toplevel(self.root)
        self.root.title("Search Cabs")
        self.root.geometry("1600x900+0+0")

 
        self.var_from_entry=StringVar()
        self.var_drop_entry=StringVar()
        self.var_date_entry=IntVar()
        #self.ac_check=IntVar()
        self.var_check1=IntVar()
        #self.var_check2=IntVar()
        #self.var_check3=IntVar()
        self.var1 = IntVar()
        #self.tip_price=IntVar()
       
        
        
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)

       
        self.cabs_frame=Frame(self.root,bg="Pink")
        self.cabs_frame.place(x=500,y=200,width=925,height=200)

        self.cabs_frame1=Frame(self.root,bg="Blue")
        self.cabs_frame1.place(x=500,y=400,width=925,height=200)

        self.cab_frame=Frame(self.root,bg="Yellow")
        self.cab_frame.place(x=70,y=200,width=350,height=400)

        L1=Label(self.cab_frame,text="Your everyday travel partner",font=("ariel","15","bold"),fg="black",bg="white")
        L1.place(x=40,y=10)

        L2=Label(self.cab_frame,text="AC cabs for point to point travel",font=("calibri","12"),fg="black",bg="white")
        L2.place(x=70,y=50)

        self.L6=Label(self.cab_frame,text="PICK UP :",font=("calibri","12",'bold'),fg="black",bg="white")
        self.L6.place(x=20,y=80)

        options1=['Thiruvanmiyur','Adyar','Airport','Railway Station']
        self.L6_combo=ttk.Combobox(self.cab_frame,value=options1,textvariable=self.var_from_entry,state='readonly')
        self.L6_combo.place(x=20,y=110,width=300,height=35)
        self.L6_combo.current(0)

        self.L7=Label(self.cab_frame,text="DROP:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L7.place(x=20,y=170)

        options2=['Thiruvanmiyur','Adyar','Airport','Railway Station']

        self.L7_combo=ttk.Combobox(self.cab_frame,value=options2,textvariable=self.var_drop_entry,state='readonly')
        self.L7_combo.place(x=20,y=200,width=300,height=35)
        self.L7_combo.current(0)

        self.L8=Label(self.cab_frame,text="WHEN:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L8.place(x=20,y=240)
        self.cal_frame=Frame(self.root,bg="black",borderwidth=1)
        self.cal_frame.place(x=90,y=470,width=300,height=35)
        self.today=datetime.now()
        self.cal = DateEntry(self.cal_frame,mindate=self.today,width=12,height=2,disabledbackground="olivedrab2" ,bordercolor='black',date_pattern='yyyy/mm/dd',headersbackground= 'olivedrab2',bd=3,Variable=self.var_date_entry)
        self.cal.place(x=5,y=5,width=285,height=20)
        
        search_btn=Button(self.cabs_frame1,text="BOOK MY CAB",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.from_drop_data1)
        search_btn.place(x=30,y=20)

        logout_btn=Button(self.cabs_frame1,text="LOG OUT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.root.destroy)
        logout_btn.place(x=700,y=120)
        self.R1 = Radiobutton(self.cabs_frame, text="OLA MINI", variable=self.var1, value=1)
        self.R1.place(x=35,y=35)
        self.R2 = Radiobutton(self.cabs_frame, text="OLA PRIME SEDAN", variable=self.var1, value=2)
        self.R2.place(x=335,y=80)
        self.R3 = Radiobutton(self.cabs_frame, text="OLA SUV", variable=self.var1, value=3)
        self.R3.place(x=635,y=120)
        
        self.radio_1=IntVar()
        self.radio_3=IntVar()
        self.fare_button1=Button(self.cabs_frame1,text="GENERATE RECEIPT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.Receiptt1)
        self.fare_button1.place(x=350,y=70)


    def cabtypefun1(self):

        self.radiobtn_var= self.var1.get()

        if self.radiobtn_var==1:
            self.sqlcabtype= 'Ola Mini'

        if self.radiobtn_var==2:
            self.sqlcabtype= 'Ola Prime Sedan'
        if self.radiobtn_var==3:
            self.sqlcabtype= 'Ola SUV'
        
        return self.sqlcabtype
    
    def from_to_fare1(self):
        dist=IntVar()

        if self.L6_combo.get()=='Thiruvanmiyur' and self.L7_combo.get()=='Adyar':
            # km1=5
            dist=250
            return dist

        if self.L6_combo.get()=='Thiruvanmiyur' and self.L7_combo.get()=='Airport':
            # km1=7
            dist=350
            return dist

        if self.L6_combo.get()=='Thiruvanmiyur' and self.L7_combo.get()=='Railway Station':
            # km1=10
            dist=500
            return dist
        
        if self.L6_combo.get()=='Adyar' and self.L7_combo.get()=='Thiruvanmiyur':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Adyar' and self.L7_combo.get()=='Airport':
            # km1=7
            dist=350
            return dist

        if self.L6_combo.get()=='Adyar' and self.L7_combo.get()=='Railway Station':
            # km1=10
            dist=500
            return dist
        
        if self.L6_combo.get()=='Airport' and self.L7_combo.get()=='Thiruvanmiyur':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Airport' and self.L7_combo.get()=='Adyar':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Airport' and self.L7_combo.get()=='Railway Station':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Railway Station' and self.L7_combo.get()=='Thiruvanmiyur':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Railway Station' and self.L7_combo.get()=='Adyar':
            # km1=10
            dist=500
            return dist

        if self.L6_combo.get()=='Railway Station' and self.L7_combo.get()=='Airport':
            # km1=10
            dist=500
            return dist
        
    def sumoffare1(self):
        self.total1=(self.from_to_fare1())
        return self.total1
    
    def Receiptt1(self):
    
        self.root=Toplevel(self.root)
        self.root.title("Receipt")
        self.root.geometry("350x450")

        self.txtReceipt1=StringVar()
        self.txtReceipt2=StringVar()
        self.Receipt_Ref=StringVar()

        self.ReceiptFrame=Frame(self.root,bg='Blue')
        self.ReceiptFrame.place(x=0,y=0,height=450,width=450)

        welcome_label1=Label(self.ReceiptFrame,text="Receipt",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label1.place(x=100,y=10)

        self.txtReceipt1 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="Blue")
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)

        self.txtReceipt2 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="Blue")
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)

        self.txtReceipt1.delete("1.0",END)
        self.txtReceipt2.delete("1.0",END)
        x=random.randint(10853,500831)
        randomRef = str(x)
        self.Receipt_Ref.set(randomRef)
        self.txtReceipt1.insert(END,"RECEIPT NUMBER:\n")
        self.txtReceipt2.insert(END, self.Receipt_Ref.get() + "\n")
        self.txtReceipt1.insert(END,"USERNAME:\n")
        self.txtReceipt2.insert(END, self.username_entry.get() + "\n")
        self.txtReceipt1.insert(END,'FROM:\n')
        self.txtReceipt2.insert(END, self.L6_combo.get() + "\n")
        self.txtReceipt1.insert(END,'TO:\n')
        self.txtReceipt2.insert(END, self.L7_combo.get() + " \n")
        self.txtReceipt1.insert(END,'DATE:\n')
        self.txtReceipt2.insert(END, self.cal.get() + "\n")
        self.txtReceipt1.insert(END,'CABTYPE:\n')
        self.txtReceipt2.insert(END, self.cabtypefun() + "\n")
        self.txtReceipt1.insert(END,'FARE:\n')
        self.txtReceipt2.insert(END, str(self.from_to_fare1()) + "\n")
        #self.txtReceipt1.insert(END,'TOTAL AMOUNT:\n')
        #self.txtReceipt2.insert(END, str(self.sumoffare1()) + "\n")
        

# ========================================================================================================================
# =================================================FROM DROP=============================================================
# ========================================================================================================================    

    def from_drop(self):

        self.root=Toplevel(self.root)
        self.root.title("Search Cabs")
        self.root.geometry("1600x900+0+0")

 
        self.var_from_entry=StringVar()
        self.var_drop_entry=StringVar()
        self.var_date_entry=IntVar()       
        self.var_check1=IntVar()
        self.var1 = IntVar()
        
        #create canvas
        canvas=Canvas(self.root,width=500,height=500)
        canvas.pack(fill=BOTH, expand=True)

       
        self.cabs_frame=Frame(self.root,bg="Pink")
        self.cabs_frame.place(x=500,y=200,width=925,height=200)

        self.cabs_frame1=Frame(self.root,bg="Blue")
        self.cabs_frame1.place(x=500,y=400,width=925,height=200)

        self.cab_frame=Frame(self.root,bg="Yellow")
        self.cab_frame.place(x=70,y=200,width=350,height=400)

        L1=Label(self.cab_frame,text="Your everyday travel partner",font=("ariel","15","bold"),fg="black",bg="white")
        L1.place(x=40,y=10)

        L2=Label(self.cab_frame,text="AC cabs for point to point travel",font=("calibri","12"),fg="black",bg="white")
        L2.place(x=70,y=50)

        self.L3=Label(self.cab_frame,text="PICK UP :",font=("calibri","12",'bold'),fg="black",bg="white")
        self.L3.place(x=20,y=80)

        options1=['Coimbatore','Chennai','Madurai','Trichy']
        self.L3_combo=ttk.Combobox(self.cab_frame,value=options1,textvariable=self.var_from_entry,state='readonly')
        self.L3_combo.place(x=20,y=110,width=300,height=35)
        self.L3_combo.current(0)

        self.L4=Label(self.cab_frame,text="DROP:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L4.place(x=20,y=170)

        options2=['Coimbatore','Chennai','Madurai','Trichy']
        self.L4_combo=ttk.Combobox(self.cab_frame,value=options2,textvariable=self.var_drop_entry,state='readonly')
        self.L4_combo.place(x=20,y=200,width=300,height=35)
        self.L4_combo.current(0)

        self.L5=Label(self.cab_frame,text="WHEN:",font=("calibri","12","bold"),fg="black",bg="white")
        self.L5.place(x=20,y=240)
        self.cal_frame=Frame(self.root,bg="black",borderwidth=1)
        self.cal_frame.place(x=90,y=470,width=300,height=35)
        self.today=datetime.now()
        self.cal = DateEntry(self.cal_frame,mindate=self.today,width=12,height=2,disabledbackground="olivedrab2" ,bordercolor='black',date_pattern='yyyy/mm/dd',headersbackground= 'olivedrab2',bd=3,Variable=self.var_date_entry)
        self.cal.place(x=5,y=5,width=285,height=20)
        
        search_btn=Button(self.cabs_frame1,text="BOOK MY CAB",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.from_drop_data)
        search_btn.place(x=30,y=20)

        logout_btn=Button(self.cabs_frame1,text="LOG OUT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.root.destroy)
        logout_btn.place(x=700,y=120)


        

        self.R1 = Radiobutton(self.cabs_frame, text="OLA MINI", variable=self.var1, value=1)
        self.R1.place(x=35,y=35)
        self.R2 = Radiobutton(self.cabs_frame, text="OLA PRIME SEDAN", variable=self.var1, value=2)
        self.R2.place(x=335,y=80)
        self.R3 = Radiobutton(self.cabs_frame, text="OLA SUV", variable=self.var1, value=3)
        self.R3.place(x=635,y=120)
        

        self.radio_1=IntVar()
        self.radio_3=IntVar()

        
        self.fare_button1=Button(self.cabs_frame1,text="GENERATE RECEIPT",cursor="hand2",font=("verdana","15","bold"),bg="white",fg="black",command=self.Receiptt)
        self.fare_button1.place(x=350,y=70)


    def cabtypefun(self):

        self.radiobtn_var= self.var1.get()

        if self.radiobtn_var==1:
            self.sqlcabtype= 'Ola Mini'

        if self.radiobtn_var==2:
            self.sqlcabtype= 'Ola Prime Sedan'
        if self.radiobtn_var==3:
            self.sqlcabtype= 'Ola SUV'
        
        return self.sqlcabtype


    def sumoffare(self):
        self.total=(self.from_to_fare())
        return self.total



    def from_to_fare(self):
        dist=IntVar()

        if self.L3_combo.get()=='Chennai' and self.L4_combo.get()=='Coimbatore':
            # km1=5
            dist=250
            return dist

        if self.L3_combo.get()=='Chennai' and self.L4_combo.get()=='Madurai':
            # km1=7
            dist=350
            return dist

        if self.L3_combo.get()=='Chennai' and self.L4_combo.get()=='Trichy':
            # km1=10
            dist=500
            return dist
        
        if self.L3_combo.get()=='Coimbatore' and self.L4_combo.get()=='Chennai':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Coimbatore' and self.L4_combo.get()=='Madurai':
            # km1=7
            dist=350
            return dist

        if self.L3_combo.get()=='Coimbatore' and self.L4_combo.get()=='Trichy':
            # km1=10
            dist=500
            return dist
        
        if self.L3_combo.get()=='Madurai' and self.L4_combo.get()=='Chennai':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Madurai' and self.L4_combo.get()=='Coimbatore':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Madurai' and self.L4_combo.get()=='Trichy':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Trichy' and self.L4_combo.get()=='Chennai':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Trichy' and self.L4_combo.get()=='Coimbatore':
            # km1=10
            dist=500
            return dist

        if self.L3_combo.get()=='Trichy' and self.L4_combo.get()=='Madurai':
            # km1=10
            dist=500
            return dist

    def Receiptt(self):
        R_frame=Frame(self.root,bg='Grey')
        R_frame.place(x=0,y=0,height=900,width=1700)

        self.root=Toplevel(self.root)
        self.root.title("Receipt")
        self.root.geometry("350x450")

        self.txtReceipt1=StringVar()
        self.txtReceipt2=StringVar()
        self.Receipt_Ref=StringVar()

        self.ReceiptFrame=Frame(self.root,bg='Pink')
        self.ReceiptFrame.place(x=0,y=0,height=450,width=450)

        welcome_label1=Label(self.ReceiptFrame,text="Receipt",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label1.place(x=100,y=10)

        self.txtReceipt1 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="Pink")
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)

        self.txtReceipt2 = Text(self.ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0,bg="Pink")
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)

        self.txtReceipt1.delete("1.0",END)
        self.txtReceipt2.delete("1.0",END)
        x=random.randint(10853,500831)
        randomRef = str(x)
        self.Receipt_Ref.set(randomRef)
        self.txtReceipt1.insert(END,"RECEIPT NUMBER:\n")
        self.txtReceipt2.insert(END, self.Receipt_Ref.get() + "\n")
        self.txtReceipt1.insert(END,"USERNAME:\n")
        self.txtReceipt2.insert(END, self.username_entry.get() + "\n")
        self.txtReceipt1.insert(END,'FROM:\n')
        self.txtReceipt2.insert(END, self.L3_combo.get() + "\n")
        self.txtReceipt1.insert(END,'TO:\n')
        self.txtReceipt2.insert(END, self.L4_combo.get() + " \n")
        self.txtReceipt1.insert(END,'DATE:\n')
        self.txtReceipt2.insert(END, self.cal.get() + "\n")
        self.txtReceipt1.insert(END,'CABTYPE:\n')
        self.txtReceipt2.insert(END, self.cabtypefun() + "\n")
        self.txtReceipt1.insert(END,'FARE:\n')
        self.txtReceipt2.insert(END, str(self.from_to_fare()) + "\n")
        #self.txtReceipt1.insert(END,'TOTAL AMOUNT:\n')
        #self.txtReceipt2.insert(END, str(self.sumoffare()) + "\n")
        

# ========================================================================================================================
# =================================================FROM DROP DATA=============================================================
# ========================================================================================================================
    def from_drop_data(self):

        if self.L3_combo.get()=='' or self.L4_combo.get()=='':
            messagebox.showerror('Error','All fields are required')

        if self.L3_combo.get()=='Coimbatore' or self.L4_combo.get()=='Coimbatore':
            messagebox.showerror('Error','Please select your cities')

        if self.L3_combo.get()=='Chennai' and self.L4_combo.get()=='Chennai':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        if self.L3_combo.get()=='Madurai' and self.L4_combo.get()=='Madurai':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')
        
        if self.L3_combo.get()=='Trichy' and self.L4_combo.get()=='Trichy':
            messagebox.showerror('Error','You cannot select same cities for both from and drop')

        else:
            try:
                c.execute("insert into cab(username,user_from,user_to,user_date,cabtype,base_fare,total)values(?,?,?,?,?,?,?)",
                                 [self.username_entry.get(),self.L3_combo.get(),self.L4_combo.get(),self.cal.get(),self.cabtypefun(),
                                 self.from_to_fare(),self.sumoffare()])
                conn.commit()
                c.close()
                messagebox.showinfo('Success',"BOOKING SUCCESSFUL, ENJOY YOUR RIDE!!",parent=self.root)
                

            except Exception as es:
                messagebox.showerror('Error',f'Error due to: {str(es)}',parent=self.root)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #===================variables=============================

        self.var_email_entry=StringVar()
        self.var_username_entry=StringVar()
        self.var_password_entry=StringVar()
        self.var_new_password_entry=StringVar()
        self.var_confirm_password_entry=StringVar()
        self.var_check=IntVar()
        
        #=================bgimage=================================

        canvas2=Canvas(self.root,width=500,height=500)
        canvas2.pack(fill=BOTH, expand=True)

        Login_frame2=Frame(self.root,bg='black')
        Login_frame2.place(x=550,y=170,height=400,width=350)

        Welcome_frame2=Frame(self.root,bg="black")
        Welcome_frame2.place(x=350,y=60,width=800,height=70)

        canvas_logo2=Canvas(Welcome_frame2,width=10,height=10,bg="black")
        canvas_logo2.pack(fill=BOTH, expand=True)
        
        welcome_label=Label(Welcome_frame2,text="WELCOME TO OLA CAB SERVICES!!",font=("GOUDY OLD STYLE","28","bold"),fg="yellow",bg="black")
        welcome_label.place(x=100,y=10)

        
        self.Login_frame2=Frame(self.root,bg='black')
        self.Login_frame2.place(x=510,y=170,height=450,width=400)
        reg_btn=Label(self.Login_frame2,text="REGISTER",font=("comic sans MS","22","bold"),fg="red",bg="black")
        reg_btn.place(x=65 ,y=15)

        #=====================label and entry==============================
        self.email_label=Label(self.Login_frame2,text='EMAIL',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=70)
        self.email_entry=Entry(self.Login_frame2,textvariable=self.var_email_entry,font=("times new roman","12","bold"),bg="lightgray")
        self.email_entry.place(x=25,y=100,width=300,height=25)
        self.username_label=Label(self.Login_frame2,text='USERNAME',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=140)
        self.username_entry=Entry(self.Login_frame2,textvariable=self.var_username_entry,font=("times new roman","12","bold"),bg="lightgray")
        self.username_entry.place(x=25,y=170,width=300,height=25)
        self.password_label=Label(self.Login_frame2,text='PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25 ,y=210)
        self.password_entry=Entry(self.Login_frame2,textvariable=self.var_password_entry,font=("times new roman","12","bold"),bg="lightgray",show="*")
        self.password_entry.place(x=25,y=240,width=300,height=25)
        self.confirm_password_label=Label(self.Login_frame2,text='CONFIRM PASSWORD',font=("GOUDY OLD STYLE","10"),fg="white",bg="black").place(x=25,y=280)
        self.confirm_password_entry=Entry(self.Login_frame2,textvariable=self.var_confirm_password_entry,font=("times new roman","10","bold"),bg="lightgray",show="*")
        self.confirm_password_entry.place(x=25,y=310,width=300,height=25)
        #==========================checkbtn==============================
        self.checkbox=Checkbutton(self.Login_frame2,text='I Agree To Your Terms And Conditions ',variable=self.var_check,onvalue=1,offvalue=0,bg="black",fg="red",font=("times new roman","10","bold"))
        self.checkbox.place(x=25,y=350)
        #==========================btn=====================================
        self.register_button=Button(self.Login_frame2,command=self.register_data,text="REGISTER",cursor="hand2",font=("times new roman","10"),bg="grey",fg="black",bd=0,width=15,height=1).place(x=130,y=380)
        self.logg=Button(self.Login_frame2,text="click here to go back to login page",cursor="hand2",font=("calibri","10"),bg="black",fg="white",bd=0,command=self.login_window).place(x=90,y=410)


# ========================================================================================================================
# =================================================REGISTER DATA=============================================================
# ========================================================================================================================
    def register_data(self):
        if self.var_email_entry.get()=="" or self.var_username_entry.get()=="" or self.var_password_entry.get()=="" or self.var_confirm_password_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password_entry.get()!= self.var_confirm_password_entry.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            try:
                user_verification = self.var_email_entry.get()
                sql="select * from user where emailid = ?"
                c.execute(sql,[user_verification])
                row=c.fetchone()
                print(row)
                if row!=None:
                    messagebox.showinfo('Error','User already exists,try using another email',parent=self.root)
                else:
                    c.execute("insert into user(emailid,username,password)values(?,?,?)",
                                     (self.var_email_entry.get(),
                                      self.var_username_entry.get(),
                                      self.var_password_entry.get()
                                      ))
                    conn.commit()
                    c.close()
                    messagebox.showinfo('Success','REGISTRATION SUCCESSFUL',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Error due to: {str(es)}',parent=self.root)

    def login_window(self):
        self.new_window3=Toplevel(self.root)
        self.app=main_window(self.new_window3)





if __name__=="__main__":
    main()
 

 
