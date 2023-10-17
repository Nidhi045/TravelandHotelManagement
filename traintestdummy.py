from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
import time
from tkcalendar import DateEntry
from datetime import datetime
import random
import sqlite3
global  x1,x2,x3,x4,s1,s2,s3
import tkinter.ttk as ttk

global conn, cursor
conn = sqlite3.connect('Train.db')
c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS Rail999( pnr integer,Name Text, Gender Text, Age real,class Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail88( Trainnumber integer, Source Text, Destination Text,Departuretime Text,Arrival Text,Trainname Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail99( Trainnumber real,Name Text, Gender Text, Age real,class Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail8( Trainnumber integer, Source Text, Destination Text,Departuretime Text,Arrival Text,Trainname Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail7( Trainnumber real,Name Text, Gender Text, Age real,class Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail6( Trainnumber real, Source Text, Destination Text,Departuretime Text,Arrival Text,Trainname Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail111( Trainnumber real, Source Text, Destination Text,Departuretime Text,Arrival Text,Trainname Text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail11( Trainnumber real, Source Text, Destination Text,Departuretime Text,Arrival Text,Trainname Text, class text)''')
c.execute(''' CREATE TABLE IF NOT EXISTS Rail( Name Text, Gender Text, Age Text)''')
insert_qry=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12235, 'Banglore', 'Hyderabad', '14:30', '7:55', 'Shatabadi Express')'''
insert_qry1=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12236, 'Banglore', 'Hyderabad', '16:30', '5:50', 'Yelahanka Junction')'''

insert_qry2=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12237, 'Banglore', 'Hyderabad', '8:35', '15:50', 'Kacheguda Express')'''

insert_qry3=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12238, 'Banglore', 'Hyderabad', '12:30', '7:20', 'Sampark Kranti')'''

insert_qry4=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12239, 'Banglore', 'Kerala', '6:30', '18:20', 'Kochuveli Express')'''

insert_qry5=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12240, 'Banglore', 'Kerala', '14:30', '23:30', 'Ernakulam Express')'''

insert_qry6=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12241, 'Banglore', 'Kerala', '12:30', '8:40', 'Trivandrum Express')'''

insert_qry7=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12242, 'Banglore', 'Kerala', '8:30', '16:20', 'Kanyakumari Express')'''

insert_qry8=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12243, 'Chennai', 'Kerala', '9:30', '14:40', 'Trivandrum Express')'''

insert_qry9=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12244, 'Chennai', 'Kerala', '1:00', '00:45', 'Guruvayur Express')'''

insert_qry10=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12245, 'Chennai', 'Kerala', '11:05', '3:00', 'Anantapuri Express')'''

insert_qry11=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12246, 'Chennai', 'Kerala', '14:05', '6:45', 'Raptisagar Express')'''

insert_qry12=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12247, 'Chennai', 'Hyderabad', '1:40', '10:40', 'Charminar Express')'''

insert_qry13=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12248, 'Chennai', 'Hyderabad', '6:30', '10:45', 'CGL KCG Express')'''

insert_qry14=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12249, 'Chennai', 'Hyderabad', '11:05', '20:00', 'MAS NSL Express')'''

insert_qry15=''' INSERT INTO Rail88(Trainnumber , Source , Destination ,Departuretime ,Arrival ,Trainname) VALUES(12250, 'Chennai', 'Hyderabad', '12:10', '21:10', 'MAS HYB Express')'''
cnt=conn.execute(insert_qry)

cnt1=conn.execute(insert_qry1)

cnt2=conn.execute(insert_qry2)

cnt3=conn.execute(insert_qry3)

cnt4=conn.execute(insert_qry4)

cnt5=conn.execute(insert_qry5)

cnt6=conn.execute(insert_qry6)

cnt7=conn.execute(insert_qry7)

cnt8=conn.execute(insert_qry8)

cnt9=conn.execute(insert_qry9)

cnt10=conn.execute(insert_qry10)

cnt11=conn.execute(insert_qry11)

cnt12=conn.execute(insert_qry12)

cnt13=conn.execute(insert_qry13)

cnt14=conn.execute(insert_qry14)

cnt15=conn.execute(insert_qry15)

conn.commit()

global LoginId,count
global Password
global Source
global Destination
global Date
global Name
global Age,Gender,IdProof
global variable,variable1,variable2,v2,var
global DepartureTime, TrainNumber, Number
#root = Tk()
#root.title("Railway reservation")

def main():
    win=Tk()
    app=main_window(win)
    win.mainloop()

    
class main_window:
    def __init__(self,root):
        self.root=root
        self.root.title("RAILWAY RESERVATIONS")
        self.root.geometry("1600x900+0+0")  
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 400
        height = 400
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        root.resizable(0, 0)

        w = 400
        h = 400
        canvas = Canvas(self.root, width=w, height=h)
        canvas.config(bg='light blue')
        canvas.pack()

        Label(self.root, text="INDIAN RAILWAYS",font=('Slab Serif',17),bg='Orange').place(x=100,y=150)
        Label(self.root, text="LoginId",font=('Slab Serif',15),bg='green').place(x=60,y=200)
        Label(self.root, text="Password",font=('Slab Serif',15), bg='green').place(x=60,y=240)

        self.entry_1 = Entry(self.root, font=('Slab Serif',10))
        self.entry_1.place(x=160,y=200,height=30)

        self.entry_2 = Entry(self.root, font=('Slab Serif',10),show="*")
        self.entry_2.place(x=160,y=240,height=30)
        self.button_1 = Button(self.root, text="Login",font=('Slab Serif',15),bg='blue',fg='white', command=self.printMsg).place(x=120,y=290)
        self.button_2 = Button(self.root, text="Quit",font=('Slab Serif',15),bg='blue',fg='white', command=self.root.destroy).place(x=220,y=290)

    
    def printMsg(self):
        if((self.entry_1.get()=='madhu' and self.entry_2.get()=='2108') or (self.entry_1.get()=='padma' and self.entry_2.get()=='2008') or (self.entry_1.get()=='nidhi' and self.entry_2.get()=='0402') ):
            tkinter.messagebox.showinfo('login result', 'CONGRATULATIONS!! LOGIN SUCCESSFUL')
            self.createWindow()
        else:
            tkinter.messagebox.showinfo('login result', 'LOGIN FAILED!:( TRY AGAIN')

    def createWindow(self):
        global s1,s2,s3
        self.var_date_entry=StringVar()
        self.root.destroy()
        self.window = Tk()
        self.window.title("Login frame")
        customFont = tkFont.Font(family="Helvetica", size=14)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = 410
        height = 400
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window.resizable(0, 0)

        self.window.config(bg='purple')

        self.entry1 =Entry(self.window,justify='center',font=('Slab Serif',3))
        self.entry1.place(x=210,y=70)

        self.entry2 = Entry(self.window, justify='center',font=('Slab Serif', 3))
        self.entry2.place(x=210, y=115)

        self.entry3 = Entry(self.window, justify='center',font=('Slab Serif', 3))
        self.entry3.place(x=210, y=205)


        def fun_1(*args):
            self.entry1.insert(10,self.variable.get())
        def fun_2(*args):
            self.entry2.insert(10,self.variable1.get())
        def fun_3(*args):
            self.entry3.insert(10,self.variable2.get())

        self.variable = StringVar(self.window)
        choices = ['Banglore', 'Chennai']
        self.variable.set('Select')
        #self.variable.trace("w", fun_1)
        self.popupMenu = OptionMenu(self.window, self.variable, *choices)
        self.popupMenu.place(x=210, y=70,width=100)
        self.popupMenu.config(font=('Slab Serif',15),bg="yellow")
        Label(self.window, text="Source",font=('Slab Serif',14), bg="cyan").place(x=110,y=70,width=80)
        #print self.variable.get()
        self.entry1.insert(10,self.variable.get())

        self.variable1 = StringVar(self.window)
        trains = ['Hyderabad','Kerala']
        self.variable1.set('Select')
        #self.variable1.trace("w", fun_2)

        self.popupMenu1 = OptionMenu(self.window, self.variable1, *trains)
        Label(self.window, text="Destination",font=('Slab Serif',15), bg="cyan").place(x=100,y=115,width=100)
        self.popupMenu1.config(font=('Slab Serif',14),bg="yellow")
        self.popupMenu1.place(x=210,y=115,width=130)
        #print self.variable1.get()
        self.entry2.insert(10,self.variable1.get())

        self.variable2 = StringVar(self.window)
        classes = ['1A','2A','3A']
        self.variable2.set('Select')
        #self.variable2.trace("w", fun_3)

        self.popupMenu1 = OptionMenu(self.window, self.variable2, *classes)
        Label(self.window, text="class", font=('Slab Serif', 15), bg="cyan").place(x=100, y=205, width=100)
        self.popupMenu1.config(font=('Slab Serif', 14), bg="yellow")
        self.popupMenu1.place(x=210, y=205, width=130)
        Label(self.window,text="Date",font=('Slab Serif',15), bg="cyan").place(x=110,y=160,width=80)
        #print self.variable2.get()
        self.entry3.insert(10,self.variable2.get())

        self.today=datetime.now()
        self.cal=DateEntry(self.window,mindate=self.today,width=12,height=2,disabledbackground="olivedrab2",bordercolor='black',date_pattern='yyyy/mm/dd',headerbackground='olivedrab2',bd=3,Variable=self.var_date_entry)
        self.cal.place(x=210,y=160,width=100,height=30)
        s1=StringVar()
        s2=StringVar()
        s3=StringVar()

        
        #Date=StringVar()

        self.e1=self.var_date_entry.get()

        Button(self.window,text="Search trains",font=('Slab Serif',15), bg="green",fg="white",command=self.Check).place(x=80,y=250,width=120)

        Button(self.window, text="Cancellation",font=('Slab Serif',15), bg="green",fg="white",command=self.Cancellation).place(x=220,y=250,width=120)
        

    def Check(self):
            if len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0 or len(self.entry3.get()) == 0:
                tkinter.messagebox.showinfo('Error','enter all required fields!')
            else:
                self.Checks()
    def Checks(self):
            if (self.entry1.get() == "Chennai" and self.entry2.get() == "Kerala" and self.entry3.get() == "3A") or (self.entry1.get() == "Chennai" and self.entry2.get() == "Hyderabad" and self.entry3.get() == "3A"):
                tkinter.messagebox.showinfo('Error','Sorry Train Unavailable!')
            else:
                self.Search()

                 
    def Search(self):
        global x1
        #self.root.destroy()   
        self.window1=Tk()
        self.window1.title("RAILWAY SCHEDULE")
        self.window1.config(bg='purple')
        
        screen_width = self.window1.winfo_screenwidth()
        screen_height = self.window1.winfo_screenheight()
        
        width = 1160
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window1.resizable(0, 0)

        height = 5
        width = 7
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.e1 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue",fg="white")
                self.e2 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                self.e3 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                self.e4 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                self.e5 = Entry(self.window1, justify="center",font=('Slab Serif',10),bg="blue", fg="white")
                self.e6 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")
                self.e7 = Entry(self.window1, justify="center",font=('Slab Serif',10), bg="blue", fg="white")

                self.en8 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e9 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e10 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e11 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e12 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e13 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e14 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")

                self.en15 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e16 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e17 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e18 = Entry(self.window1, justify="center",font=('Slab Serif',9),bg="light pink")
                self.e19 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e20 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e21 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")

                self.en22 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e23 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e24 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e25 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e26 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e27 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e28 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")

                self.en29 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e30 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e31 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e32 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e33 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e34 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")
                self.e35 = Entry(self.window1, justify="center",font=('Slab Serif',9), bg="light pink")

                self.e1.grid(row=0, column=0)
                self.e2.grid(row=0, column=1)
                self.e3.grid(row=0, column=2)
                self.e4.grid(row=0, column=3)
                self.e5.grid(row=0, column=4)
                self.e6.grid(row=0, column=5)
                self.e7.grid(row=0, column=6)
                self.en8.grid(row=1, column=0)
                self.e9.grid(row=1, column=1)
                self.e10.grid(row=1, column=2)
                self.e11.grid(row=1, column=3)
                self.e12.grid(row=1, column=4)
                self.e13.grid(row=1, column=5)
                self.e14.grid(row=1, column=6)
                self.en15.grid(row=2, column=0)
                self.e16.grid(row=2, column=1)
                self.e17.grid(row=2, column=2)
                self.e18.grid(row=2, column=3)
                self.e19.grid(row=2, column=4)
                self.e20.grid(row=2, column=5)
                self.e21.grid(row=2, column=6)
                self.en22.grid(row=3, column=0)
                self.e23.grid(row=3, column=1)
                self.e24.grid(row=3, column=2)
                self.e25.grid(row=3, column=3)
                self.e26.grid(row=3, column=4)
                self.e27.grid(row=3, column=5)
                self.e28.grid(row=3, column=6)
                self.en29.grid(row=4, column=0)
                self.e30.grid(row=4, column=1)
                self.e31.grid(row=4, column=2)
                self.e32.grid(row=4, column=3)
                self.e33.grid(row=4, column=4)
                self.e34.grid(row=4, column=5)
                self.e35.grid(row=4, column=6)

                self.e1.insert(10, "Train number")
                self.e2.insert(10, "Train name")
                self.e3.insert(10, "Source")
                self.e4.insert(10, "Departure time")
                self.e5.insert(10, "Destination")
                self.e6.insert(10, "Arrival")
                self.e7.insert(10, "class")
                
           
            
            if self.variable.get() == "Banglore" and self.variable1.get()== "Hyderabad":
                    self.en8.insert(10, "12235")

                    self.e9.insert(10, "Shatabadi Express")
                    self.e10.insert(10, "Banglore")
                    self.e11.insert(10, "14:30")
                    self.e12.insert(10, "Hyderabad")
                    self.e13.insert(10, "7:55")
                    self.e14.insert(10, "1A,2A,3A")

                    self.en15.insert(10, "12236")

                    self.e16.insert(10, "Yelahanka  Juntion")
                    self.e17.insert(10, "Banglore")
                    self.e18.insert(10, "16:30")
                    self.e19.insert(10, "Hyderabad")
                    self.e20.insert(10, "5:50")
                    self.e21.insert(10, "1A,2A,3A")

                    self.en22.insert(10, "12237")
                    self.e23.insert(10, "Kacheguda Express")
                    self.e24.insert(10, "Banglore")
                    self.e25.insert(10, "8:35")
                    self.e26.insert(10, "Hyderabad")
                    self.e27.insert(10, "15:50")
                    self.e28.insert(10, "1A,2A,3A")

                    self.en29.insert(10, "12238")
                    self.e30.insert(10, "Sampark Kranti")
                    self.e31.insert(10, "Banglore")
                    self.e32.insert(10, "12:30")
                    self.e33.insert(10, "Hyderabad")
                    self.e34.insert(10, "7:20")
                    self.e35.insert(10, "1A,2A,3A")


            if self.variable.get() == "Banglore" and self.variable1.get()== "Kerala":
                    self.en8.insert(10, "12239")

                    self.e9.insert(10, "Kochuveli Express")
                    self.e10.insert(10, "Banglore")
                    self.e11.insert(10, "6:30")
                    self.e12.insert(10, "Kerala")
                    self.e13.insert(10, "18:20")
                    self.e14.insert(10, "1A,2A,3A")

                    self.en15.insert(10, "12240")
                    self.e16.insert(10, "Ernakulam Express")
                    self.e17.insert(10, "Banglore")
                    self.e18.insert(10, "14:30")
                    self.e19.insert(10, "Kerala")
                    self.e20.insert(10, "23:30")
                    self.e21.insert(10, "1A,2A,3A")

                    self.en22.insert(10, "12241")
                    self.e23.insert(10, "Trivandrum Express")
                    self.e24.insert(10, "Banglore")
                    self.e25.insert(10, "12:30")
                    self.e26.insert(10, "Kerala")
                    self.e27.insert(10, "8:40")
                    self.e28.insert(10, "1A,2A,3A")

                    self.en29.insert(10, "12242")
                    self.e30.insert(10, "Kanyakumari Express")
                    self.e31.insert(10, "Banglore")
                    self.e32.insert(10, "8:30")
                    self.e33.insert(10, "Kerala")
                    self.e34.insert(10, "16:20")
                    self.e35.insert(10, "1A,2A,3A")

            if self.variable.get() == "Chennai" and self.variable1.get()== "Kerala":
                    self.en8.insert(10, "12243")
                    #ach12243=12243
                    self.e9.insert(10, "Trivandrum Express")
                    self.e10.insert(10, "Chennai")
                    self.e11.insert(10, "9:30")
                    self.e12.insert(10, "Kerala")
                    self.e13.insert(10, "14:40")
                    self.e14.insert(10, "1A,2A")

                    self.en15.insert(10, "12244")
                    self.e16.insert(10, "Guruvayur Express")
                    self.e17.insert(10, "Chennai")
                    self.e18.insert(10, "1:00")
                    self.e19.insert(10, "Kerala")
                    self.e20.insert(10, "00:45")
                    self.e21.insert(10, "1A,2A")

                    self.en22.insert(10, "12245")
                    self.e23.insert(10, "Anantapuri Express")
                    self.e24.insert(10, "Chennai")
                    self.self.e25.insert(10, "11:05")
                    self.e26.insert(10, "Kerala")
                    self.e27.insert(10, "3:00")
                    self.e28.insert(10, "1A,2A")

                    self.en29.insert(10, "12246")
                    self.e30.insert(10, "Raptisagar Express")
                    self.self.e31.insert(10, "Chennai")
                    self.e32.insert(10, "14:05")
                    self.e33.insert(10, "Kerala")
                    self.e34.insert(10, "6:45")
                    self.e35.insert(10, "1A,2A")

            if self.variable.get() == "Chennai" and self.variable1.get()== "Hyderabad":
                    self.en8.insert(10, "12247")
                    #and12247=12247
                    self.e9.insert(10, "Charminar Express")
                    self.e10.insert(10, "Chennai")
                    self.e11.insert(10, "1:40")
                    self.e12.insert(10, "Hyderabad")
                    self.e13.insert(10, "10:40")
                    self.e14.insert(10, "1A,2A")

                    self.en15.insert(10, "12248")
                    self.e16.insert(10, "CGL KCG Express")
                    self.e17.insert(10, "Chennai")
                    self.e18.insert(10, "6:30")
                    self.e19.insert(10, "Hyderabad")
                    self.e20.insert(10, "10:45")
                    self.e21.insert(10, "1A,2A")

                    self.en22.insert(10, "12249")
                    self.e23.insert(10, "MAS NSL Express")
                    self.e24.insert(10, "Chennai")
                    self.e25.insert(10, "11:05")
                    self.e26.insert(10, "Hyderabad")
                    self.e27.insert(10, "20:00")
                    self.e28.insert(10, "1A,2A")

                    self.en29.insert(10, "12250")
                    self.e30.insert(10, "MAS HYB Express")
                    self.e31.insert(10, "Chennai")
                    self.e32.insert(10, "12:10")
                    self.e33.insert(10, "Hyderabad")
                    self.e34.insert(10, "21:10")
                    self.e35.insert(10, "1A,2A")
        button1=Button(self.window1,text="Book",font=('Slab Serif',9),width=10,bg="yellow",command=self.PassengerDetails1)
        button1.grid(row=1,column=7)
        button2 = Button(self.window1, text="Book",font=('Slab Serif',9),width=10, bg="yellow",command=self.PassengerDetails2)
        button2.grid(row=2, column=7)
        button3 = Button(self.window1, text="Book",font=('Slab Serif',9),width=10, bg="yellow", command=self.PassengerDetails3)
        button3.grid(row=3, column=7)
        button4 = Button(self.window1, text="Book",font=('Slab Serif',9),width=10,bg="yellow", command=self.PassengerDetails4)
        button4.grid(row=4, column=7)

        button5 = Button(self.window1, text="Back",font=('Slab Serif',15),width=60, bg="cyan", command=self.Back1)
        button5.place(x=450,y=150,width=100)



    def PassengerDetails1(self):
        
        global x1

        if self.en8.get()=="12235":
            x1=12235
        elif self.en8.get()=="12239":
            x1=12239
        elif self.en8.get() == "12243":
            x1 = 12243
        else:
            x1 = 12247

            #def PassengerDetails():
        #self.root.destroy()
        self.window2 = Tk()
        self.window2.title("Passenger Details")
        self.window2.config(bg="green")
        screen_width = self.window2.winfo_screenwidth()
        screen_height = self.window2.winfo_screenheight()
        width = 700
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window2.resizable(0, 0)

        height = 5
        width = 5
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.e1 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn2 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn3 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn4 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e5 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e6 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn7 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn8 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn9 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e10 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e11 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e12 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e13 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e14 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e15 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e16 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e17 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e18 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e19 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e20 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e21 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e22 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e23 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e24 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e25 = Entry(self.window2, justify="center", font=('Slab Serif', 3))

                self.e1.insert(10, "S.no")
                self.enn2.insert(10, "Name")
                self.enn3.insert(10, "Age")
                self.enn4.insert(10, "Gender")
                self.e5.insert(10, "IdProof")
                self.e6.insert(10, "1")

                self.e11.insert(10, "2")
                self.e16.insert(10, "3")
                self.e21.insert(10, "4")

                self.e1.grid(row=0, column=0)
                self.enn2.grid(row=0, column=1)
                self.enn3.grid(row=0, column=2)
                self.enn4.grid(row=0, column=3)
                self.e5.grid(row=0, column=4)
                self.e6.grid(row=1, column=0)
                self.enn7.grid(row=1, column=1)
                self.enn8.grid(row=1, column=2)
                self.enn9.grid(row=1, column=3)
                self.e10.grid(row=1, column=4)

                self.e11.grid(row=2, column=0)
                self.e12.grid(row=2, column=1)
                self.e13.grid(row=2, column=2)
                self.e14.grid(row=2, column=3)
                self.e15.grid(row=2, column=4)

                self.e16.grid(row=3, column=0)
                self.e17.grid(row=3, column=1)
                self.e18.grid(row=3, column=2)
                self.e19.grid(row=3, column=3)
                self.e20.grid(row=3, column=4)

                self.e21.grid(row=4, column=0)
                self.e22.grid(row=4, column=1)
                self.e23.grid(row=4, column=2)
                self.e24.grid(row=4, column=3)
                self.e25.grid(row=4, column=4)

                def fun(*args):
                    self.enn9.insert(10, self.v2.get())

                def fun1(*args):
                    self.e14.insert(10, self.v3.get())

                def fun2(*args):
                    self.e19.insert(10, self.v4.get())

                def fun3(*args):
                    self.e24.insert(10, self.v5.get())

                def fun4(*args):
                    self.e10.insert(10, self.v6.get())

                def fun5(*args):
                    self.e15.insert(10, self.v7.get())

                def fun6(*args):
                    self.e20.insert(10, self.v8.get())

                def fun7(*args):
                    self.e25.insert(10, self.v9.get())

                self.v2 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v2.set('Select')
                self.v2.trace("w", fun)
                popupMenu1 = OptionMenu(self.window2, self.v2, *gender)
                popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                popupMenu1.grid(row=1, column=3)

                self.v3 = StringVar(self.window2)
                gender1 = {'Male', 'Female'}
                self.v3.set('Select')
                self.v3.trace("w", fun1)
                popupMenu2 = OptionMenu(self.window2, self.v3, *gender1)
                popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                popupMenu2.grid(row=2, column=3)

                self.v4 = StringVar(self.window2)
                gender2 = {'Male', 'Female'}
                self.v4.set('Select')
                self.v4.trace("w", fun2)
                popupMenu3 = OptionMenu(self.window2, self.v4, *gender2)
                popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                popupMenu3.grid(row=3, column=3)

                self.v5 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v5.set('Select')
                self.v5.trace("w", fun3)
                popupMenu4 = OptionMenu(self.window2, self.v5, *gender)
                popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                popupMenu4.grid(row=4, column=3)

                self.v6 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v6.set('Select')
                self.v6.trace("w", fun4)
                popup = OptionMenu(self.window2, self.v6, *proof)
                popup.config(font=('Slab Serif', 9), bg="light green")
                popup.grid(row=1, column=4)

                self.v7 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v7.set('Select')
                self.v7.trace("w", fun5)
                popup = OptionMenu(self.window2, self.v7, *proof)
                popup.config(font=('Slab Serif', 9), bg="light green")
                popup.grid(row=2, column=4)
                self.v8 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v8.set('Select')
                self.v8.trace("w", fun6)
                popup = OptionMenu(self.window2, self.v8, *proof)
                popup.config(font=('Slab Serif', 9), bg="light green")
                popup.grid(row=3, column=4)

                self.v9 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v9.set('Select')
                self.v9.trace("w", fun7)
                popup = OptionMenu(self.window2, self.v9, *proof)
                popup.config(font=('Slab Serif', 9), bg="light green")

                popup.grid(row=4, column=4)
        b = Button(self.window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=self.Check1)
        b.place(x=250, y=155, width=100)

    def Check1(self):
        global count
        count=0
        
        if len(self.enn7.get()) == 0 or len(self.enn8.get()) == 0 or len(self.enn9.get()) == 0 or len(self.e10.get()) == 0:
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e12.get()) != 0 and (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e17.get()) != 0 and (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e22.get()) != 0 and (len(self.e23.get()) == 0 or len(self.e24.get()) == 0 or len(self.e25.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.e12.get()) != 0 or len(self.e13.get()) != 0 or len(self.e14.get()) != 0 or len(
                self.e15.get()) != 0) and (
                len(self.e22.get()) != 0 or len(self.e23.get()) != 0 or len(self.e24.get()) != 0 or len(
            self.e25.get()) != 0) and (
                len(e17.get()) == 0 or (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0)):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.enn7.get()) != 0 or len(self.enn8.get()) != 0 or len(self.enn9.get()) != 0 or len(
                self.e10.get()) != 0) and (
                len(self.e17.get()) != 0 or len(self.e18.get()) != 0 or len(self.e19.get()) != 0 or len(
            self.e20.get()) != 0) and (
                len(self.e12.get()) == 0 or (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0)):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif  self.enn7.get()!="" and self.e12.get()=="" and self.e17.get()=="" and self.e22.get()=="":
            count=1
            self.Show1()
        elif self.e12.get()!="" and self.e17.get()=="":
            count=2
            self.Show1()
        elif self.e17.get()!="" and self.e22.get()=="":
            count=3
            self.Show1()
        elif self.e22.get()!="":
            count=4
            self.Show1()
        else:
            self.Show1()


    def Show1(self):

        global x1,count
        #self.root.destroy()
        self.window3 = Tk()

        self.window3.title("Ticket")
        screen_width = self.window3.winfo_screenwidth()
        screen_height = self.window3.winfo_screenheight()
        width = 580
        height = 480
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window3.resizable(0, 0)
        self.window3.config(bg='white')

        Label(self.window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
        Label(self.window3, text="Gender",bg='white', font=('Slab Serif', 11)).place(x=320, y=50)
        Label(self.window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
        Label(self.window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
        Label(self.window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
        Label(self.window3, text="Train no.",bg='white',font=('Slab Serif', 11)).place(x=90, y=130)
        Label(self.window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
        Label(self.window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
        Label(self.window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
        Label(self.window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

        Label(self.window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

        self.Number = Label(self.window3, justify="center",bg='white',text=count, font=('Slab Serif', 10)).place(x=170, y=290,  height=25)


        self.Class = Label(self.window3, justify="center",bg='white',text=self.variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
        self.TrainNumber = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10))
        self.TrainNumber.place(x=170, y=130, height=25)


        global conn, cursor, x1, x2
        if x1 == 12235:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12235")
            fetch = cursor.fetchall()


            for data in fetch:
                self.Source = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[5],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=90, height=25)
            a=111111
            b=999999
            pnr=(random.randint(a, b))

            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()),int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()


            cursor.execute("Select * from Rail999 where pnr=?  ",(pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:

                self.pnr1 = Label(self.window3, justify="center",bg='white',text=data[0],
                                    font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3,text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(x=170, y=50,height=25)
                self.Age = Label(self.window3,text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(x=380, y=90, height=25)
                self.Gender = Label(self.window3,text=data[3] ,bg='white',justify="center", font=('Slab Serif', 9)).place(x=380, y=50, height=25)



            cursor.close()
            conn.close()
        elif x1 == 12239:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12239")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2], justify="center",bg='white',
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[5], justify="center",bg='white',
                                            font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                                                font=('Slab Serif', 10)).place(x=170, y=90, height=25)
            a = 111111
            b = 999999
            pnr = (random.randint(a, b))


            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:

                self.pnr1 = Label(self.window3, justify="center", text=data[0],bg='white',
                                    font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                            x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                            x=380, y=50, height=25)

            cursor.close()
            conn.close()
        elif x1 == 12243:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12243")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                                                font=('Slab Serif', 10)).place(x=170, y=90, height=25)
            a = 111111
            b = 999999
            pnr = (random.randint(a, b))


            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:
                self.pnr1 = Label(self.window3, justify="center",bg='white',text=data[0],
                                    font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

            cursor.close()
            conn.close()
        elif x1 == 12247:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12247")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5], justify="center",bg='white', font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2], justify="center",bg='white',
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1], justify="center",bg='white',
                                            font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                                                font=('Slab Serif', 10)).place(x=170, y=90, height=25)
            a = 111111
            b = 999999
            pnr = (random.randint(a, b))


            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:


                self.pnr1 = Label(self.window3, justify="center",bg='white', text=data[0],
                                    font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

            cursor.close()
            conn.close()

        Label(self.window3, text="Have a nice trip!!",bg='white', font=('Slab Serif', 17)).place(x=200, y=340)

            #mainloop()



        #global count
        #count=0
        
    #mainloop()

    #self.PassengerDetails()

    def PassengerDetails2(self):
        global x1
        if self.en15.get()=="12236":
            x1=12236
        elif self.en15.get()=="12240":
            x1=12240
        elif self.en15.get() == "12244":
            x1 = 12244
        else:
            x1 = 12248

            #def PassengerDetails():
        #self.root.destroy()
        self.window2 = Tk()
        self.window2.title("Passenger Details")
        self.window2.config(bg="green")
        screen_width = self.window2.winfo_screenwidth()
        screen_height = self.window2.winfo_screenheight()
        width = 700
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window2.resizable(0, 0)

        height = 5
        width = 5
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.e1 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn2 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn3 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn4 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e5 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e6 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn7 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn8 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn9 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e10 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e11 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e12 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e13 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e14 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e15 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e16 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e17 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e18 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e19 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e20 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e21 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e22 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e23 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e24 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e25 = Entry(self.window2, justify="center", font=('Slab Serif', 3))

                self.e1.insert(10, "S.no")
                self.enn2.insert(10, "Name")
                self.enn3.insert(10, "Age")
                self.enn4.insert(10, "Gender")
                self.e5.insert(10, "IdProof")
                self.e6.insert(10, "1")

                self.e11.insert(10, "2")
                self.e16.insert(10, "3")
                self.e21.insert(10, "4")

                self.e1.grid(row=0, column=0)
                self.enn2.grid(row=0, column=1)
                self.enn3.grid(row=0, column=2)
                self.enn4.grid(row=0, column=3)
                self.e5.grid(row=0, column=4)
                self.e6.grid(row=1, column=0)
                self.enn7.grid(row=1, column=1)
                self.enn8.grid(row=1, column=2)
                self.enn9.grid(row=1, column=3)
                self.e10.grid(row=1, column=4)

                self.e11.grid(row=2, column=0)
                self.e12.grid(row=2, column=1)
                self.e13.grid(row=2, column=2)
                self.e14.grid(row=2, column=3)
                self.e15.grid(row=2, column=4)

                self.e16.grid(row=3, column=0)
                self.e17.grid(row=3, column=1)
                self.e18.grid(row=3, column=2)
                self.e19.grid(row=3, column=3)
                self.e20.grid(row=3, column=4)

                self.e21.grid(row=4, column=0)
                self.e22.grid(row=4, column=1)
                self.e23.grid(row=4, column=2)
                self.e24.grid(row=4, column=3)
                self.e25.grid(row=4, column=4)

                def fun(*args):
                    self.enn9.insert(10, self.v2.get())

                def fun1(*args):
                    self.e14.insert(10, self.v3.get())

                def fun2(*args):
                    self.e19.insert(10, self.v4.get())

                def fun3(*args):
                    self.e24.insert(10, self.v5.get())

                def fun4(*args):
                    self.e10.insert(10, self.v6.get())

                def fun5(*args):
                    self.e15.insert(10, self.v7.get())

                def fun6(*args):
                    self.e20.insert(10, self.v8.get())

                def fun7(*args):
                    self.e25.insert(10, self.v9.get())

                self.v2 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v2.set('Select')
                self.v2.trace("w", fun)
                self.popupMenu1 = OptionMenu(self.window2, self.v2, *gender)
                self.popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu1.grid(row=1, column=3)

                self.v3 = StringVar(self.window2)
                gender1 = {'Male', 'Female'}
                self.v3.set('Select')
                self.v3.trace("w", fun1)
                self.popupMenu2 = OptionMenu(self.window2, self.v3, *gender1)
                self.popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu2.grid(row=2, column=3)

                self.v4 = StringVar(self.window2)
                gender2 = {'Male', 'Female'}
                self.v4.set('Select')
                self.v4.trace("w", fun2)
                self.popupMenu3 = OptionMenu(self.window2, self.v4, *gender2)
                self.popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu3.grid(row=3, column=3)

                self.v5 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v5.set('Select')
                self.v5.trace("w", fun3)
                self.popupMenu4 = OptionMenu(self.window2, self.v5, *gender)
                self.popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu4.grid(row=4, column=3)

                self.v6 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v6.set('Select')
                self.v6.trace("w", fun4)
                self.popup = OptionMenu(self.window2, self.v6, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=1, column=4)

                self.v7 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v7.set('Select')
                self.v7.trace("w", fun5)
                self.popup = OptionMenu(self.window2, self.v7, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=2, column=4)

                self.v8 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v8.set('Select')
                self.v8.trace("w", fun6)
                self.popup = OptionMenu(self.window2, self.v8, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=3, column=4)

                self.v9 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v9.set('Select')
                self.v9.trace("w", fun7)
                self.popup = OptionMenu(self.window2, self.v9, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=4, column=4)
        self.b = Button(self.window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=self.Check2)
        self.b.place(x=250, y=155, width=100)

    def Check2(self):
        global count
        count=0
            
        if len(self.enn7.get()) == 0 or len(self.enn8.get()) == 0 or len(self.enn9.get()) == 0 or len(self.e10.get()) == 0:
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e12.get()) != 0 and (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e17.get()) != 0 and (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e22.get()) != 0 and (len(self.e23.get()) == 0 or len(self.e24.get()) == 0 or len(self.e25.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.e12.get()) != 0 or len(self.e13.get()) != 0 or len(self.e14.get()) != 0 or len(
                self.e15.get()) != 0) and (
                len(self.e22.get()) != 0 or len(self.e23.get()) != 0 or len(self.e24.get()) != 0 or len(
                self.e25.get()) != 0) and (
                len(self.e17.get()) == 0 or (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0)):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.enn7.get()) != 0 or len(self.enn8.get()) != 0 or len(self.enn9.get()) != 0 or len(
                self.e10.get()) != 0) and (
                len(self.e17.get()) != 0 or len(self.e18.get()) != 0 or len(self.e19.get()) != 0 or len(
                self.e20.get()) != 0) and (
                len(self.e12.get()) == 0 or (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0)):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif  self.enn7.get()!="" and self.e12.get()=="" and self.e17.get()=="" and self.e22.get()=="":
            count=1
            self.Show2()
        elif self.e12.get()!="" and self.e17.get()=="":
            count=2
            self.Show2()
        elif self.e17.get()!="" and self.e22.get()=="":
            count=3
            self.Show2()
        elif self.e22.get()!="":
            count=4
            self.Show2()
        else:
            self.Show2()



    def Show2(self):
        global x1
            #self.root.destroy
        self.window3 = Tk()
        self.window3.title("Ticket")
        screen_width = self.window3.winfo_screenwidth()
        screen_height = self.window3.winfo_screenheight()
        width = 580
        height = 480
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window3.resizable(0, 0)
        self.window3.config(bg='white')

        Label(self.window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
        Label(self.window3, text="Gender",bg='white',font=('Slab Serif', 11)).place(x=320, y=50)
        Label(self.window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
        Label(self.window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
        Label(self.window3, text="Class",bg='white',font=('Slab Serif', 11)).place(x=320, y=130)
        Label(self.window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
        Label(self.window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
        Label(self.window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
        Label(self.window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
        Label(self.window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

        Label(self.window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

        self.Name = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
        self.Gender = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
        self.DepartureTime = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,
                                                                                                           height=25)
        self.Age = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
        self.Class = Label(self.window3, justify="center",bg='white',text=self.variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
        self.TrainNumber = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10))
        self.TrainNumber.place(x=170, y=130, height=25)

        self.Source = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
        self.Destination = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,
                                                                                                         height=25)
        self.Number = Label(self.window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
        global conn, cursor, x1, x2

        if x1 == 12236:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12236")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5], justify="center", font=('Slab Serif', 10)).place(
                            x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2], justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1], justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3], justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

            a = 111111
            b = 999999
            pnr = (random.randint(a, b))
            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                    (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:

                self.pnr1 = Label(self.window3, justify="center",bg='white', text=data[0],
                                        font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

            cursor.close()
            conn.close()
        elif x1 == 12240:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12240")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                            x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                                            font=('Slab Serif', 10)).place(x=170, y=90, height=25)

            a = 111111
            b = 999999
            pnr = (random.randint(a, b))
            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:

                self.pnr1 = Label(self.window3,bg='white', justify="center", text=data[0],
                                    font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                            x=380, y=50, height=25)

            cursor.close()
            conn.close()
        elif x1 == 12244:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12244")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                            x=170, y=170, height=25)
                self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=90, height=25)

            a = 111111
            b = 999999
            pnr = (random.randint(a, b))

            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(seelf.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:
                self.pnr1 = Label(self.window3,bg='white', justify="center", text=data[0],
                                        font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

            cursor.close()
            conn.close()
        elif x1 == 12248:
            cursor = conn.cursor()
            self.TrainNumber.config(text=x1)
            cursor.execute("Select * from Rail88 where Trainnumber=12248")
            fetch = cursor.fetchall()
            for data in fetch:
                self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170,height=25)

                self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                            font=('Slab Serif', 10)).place(x=170, y=90, height=25)

            a = 111111
            b = 999999
            pnr = (random.randint(a, b))

            cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(self.enn7.get()), int(self.enn8.get()), str(self.enn9.get())))

            conn.commit()

            cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
            fetch1 = cursor.fetchall()
            for data in fetch1:
                self.pnr1 = Label(self.window3, justify="center",bg='white', text=data[0],
                                        font=('Slab Serif', 9))
                self.pnr1.place(x=380, y=170, height=25)
                self.pnr1.config(text=data[0])
                self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

            cursor.close()
            conn.close()

        Label(self.window3, text="Have a nice trip!!",bg='white', font=('Slab Serif', 17)).place(x=200, y=340)

            #mainloop()

        
    #mainloop()

    #self.PassengerDetails()

    def PassengerDetails3(self):

        global x1
        if self.en22.get() == "12237":
            x1 = 12237
        elif self.en22.get() == "12241":
            x1 = 12241
        elif self.en22.get() == "12245":
            x1 = 12245
        else:
            x1 = 12249

            #def PassengerDetails():
        #self.root.destroy()    
        
        self.window2 = Tk()
        self.window2.title("Passenger Details")
        self.window2.config(bg="green")
        screen_width = self.window2.winfo_screenwidth()
        screen_height = self.window2.winfo_screenheight()
        width = 700
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window2.resizable(0, 0)

        height = 5
        width = 5
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.e1 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn2 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn3 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn4 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e5 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e6 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn7 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn8 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn9 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e10 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e11 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e12 = Entry(self.window2, justify="center",font=('Slab Serif', 9), bg="yellow")
                self.e13 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e14 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e15 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e16 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e17 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e18 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e19 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e20 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e21 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e22 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e23 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e24 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e25 = Entry(self.window2, justify="center", font=('Slab Serif', 3))

                self.e1.insert(10, "S.no")
                self.enn2.insert(10, "Name")
                self.enn3.insert(10, "Age")
                self.enn4.insert(10, "Gender")
                self.e5.insert(10, "IdProof")
                self.e6.insert(10, "1")

                self.e11.insert(10, "2")
                self.e16.insert(10, "3")
                self.e21.insert(10, "4")

                self.e1.grid(row=0, column=0)
                self.enn2.grid(row=0, column=1)
                self.enn3.grid(row=0, column=2)
                self.enn4.grid(row=0, column=3)
                self.e5.grid(row=0, column=4)
                self.e6.grid(row=1, column=0)
                self.enn7.grid(row=1, column=1)
                self.enn8.grid(row=1, column=2)
                self.enn9.grid(row=1, column=3)
                self.e10.grid(row=1, column=4)

                self.e11.grid(row=2, column=0)
                self.e12.grid(row=2, column=1)
                self.e13.grid(row=2, column=2)
                self.e14.grid(row=2, column=3)
                self.e15.grid(row=2, column=4)

                self.e16.grid(row=3, column=0)
                self.e17.grid(row=3, column=1)
                self.e18.grid(row=3, column=2)
                self.e19.grid(row=3, column=3)
                self.e20.grid(row=3, column=4)

                self.e21.grid(row=4, column=0)
                self.e22.grid(row=4, column=1)
                self.e23.grid(row=4, column=2)
                self.e24.grid(row=4, column=3)
                self.e25.grid(row=4, column=4)

                def fun(*args):
                    self.enn9.insert(10, self.v2.get())

                def fun1(*args):
                    self.e14.insert(10, self.v3.get())

                def fun2(*args):
                    self.e19.insert(10, self.v4.get())

                def fun3(*args):
                    self.e24.insert(10, self.v5.get())

                def fun4(*args):
                    self.e10.insert(10, self.v6.get())

                def fun5(*args):
                    self.e15.insert(10, self.v7.get())

                def fun6(*args):
                    self.e20.insert(10, self.v8.get())

                def fun7(*args):
                    self.e25.insert(10, self.v9.get())

                self.v2 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v2.set('Select')
                self.v2.trace("w", fun)
                self.popupMenu1 = OptionMenu(self.window2, self.v2, *gender)
                self.popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu1.grid(row=1, column=3)

                self.v3 = StringVar(self.window2)
                gender1 = {'Male', 'Female'}
                self.v3.set('Select')
                self.v3.trace("w", fun1)
                self.popupMenu2 = OptionMenu(self.window2, self.v3, *gender1)
                self.popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu2.grid(row=2, column=3)

                self.v4 = StringVar(self.window2)
                gender2 = {'Male', 'Female'}
                self.v4.set('Select')
                self.v4.trace("w", fun2)
                self.popupMenu3 = OptionMenu(self.window2, self.v4, *gender2)
                self.popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu3.grid(row=3, column=3)

                self.v5 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v5.set('Select')
                self.v5.trace("w", fun3)
                self.popupMenu4 = OptionMenu(self.window2, self.v5, *gender)
                self.popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu4.grid(row=4, column=3)

                self.v6 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v6.set('Select')
                self.v6.trace("w", fun4)
                self.popup = OptionMenu(self.window2, self.v6, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=1, column=4)

                self.v7 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v7.set('Select')
                self.v7.trace("w", fun5)
                self.popup = OptionMenu(self.window2, self.v7, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=2, column=4)

                self.v8 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v8.set('Select')
                self.v8.trace("w", fun6)
                self.popup = OptionMenu(self.window2, self.v8, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=3, column=4)

                self.v9 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v9.set('Select')
                self.v9.trace("w", fun7)
                self.popup = OptionMenu(self.window2, self.v9, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=4, column=4)
        self.b = Button(self.window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=self.Check3)
        self.b.place(x=250, y=155, width=100)

    def Check3(self):
        global count
        count=0
        if len(self.enn7.get()) == 0 or len(self.enn8.get()) == 0 or len(self.enn9.get()) == 0 or len(self.e10.get()) == 0:
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e12.get()) != 0 and (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e17.get()) != 0 and (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif len(self.e22.get()) != 0 and (len(self.e23.get()) == 0 or len(self.e24.get()) == 0 or len(self.e25.get()) == 0):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.e12.get()) != 0 or len(self.e13.get()) != 0 or len(self.e14.get()) != 0 or len(
            self.e15.get()) != 0) and (
            len(self.e22.get()) != 0 or len(self.e23.get()) != 0 or len(self.e24.get()) != 0 or len(
            self.e25.get()) != 0) and (
            len(self.e17.get()) == 0 or (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0)):
            tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif (len(self.enn7.get()) != 0 or len(self.enn8.get()) != 0 or len(self.enn9.get()) != 0 or len(
                self.e10.get()) != 0) and (
                len(self.e17.get()) != 0 or len(self.e18.get()) != 0 or len(self.e19.get()) != 0 or len(
                self.e20.get()) != 0) and (
                len(e12.get()) == 0 or (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0)):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
        elif  self.enn7.get()!="" and self.e12.get()=="" and self.e17.get()=="" and self.e22.get()=="":
            count=1
            self.Show3()
        elif self.e12.get()!="" and self.e17.get()=="":
            count=2
            self.Show3()
        elif self.e17.get()!="" and self.e22.get()=="":
            count=3
            self.Show3()
        elif self.e22.get()!="":
            count=4
            self.Show3()
        else:
            self.Show3()



        def Show3(self):
            global x1
            #self.root.destroy()
            self.window3 = Tk()
            self.window3.title("Ticket")
            screen_width = self.window3.winfo_screenwidth()
            screen_height = self.window3.winfo_screenheight()
            width = 580
            height = 480
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            self.window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.window3.resizable(0, 0)
            self.window3.config(bg='white')

            Label(self.window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
            Label(self.window3, text="Gender", bg='white',font=('Slab Serif', 11)).place(x=320, y=50)
            Label(self.window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
            Label(self.window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
            Label(self.window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
            Label(self.window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
            Label(self.window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
            Label(self.window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
            Label(self.window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
            Label(self.window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

            Label(self.window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

            self.Name = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
            self.Gender = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
            self.DepartureTime = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,height=25)
            self.Age = Label(self.window3, justify="center",bg='white',font=('Slab Serif', 10)).place(x=380, y=90, height=25)
            self.Class = Label(self.window3, justify="center",bg='white',text=self.variable2.get(),font=('Slab Serif', 10)).place(x=380, y=130, height=25)
            self.TrainNumber = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10))
            self.TrainNumber.place(x=170, y=130, height=25)
            self.Source = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
            self.Destination = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,height=25)
            self.Number = Label(self.window3,text=count, justify="center", bg='white',font=('Slab Serif', 9)).place(x=170, y=290, height=25)
            global conn, cursor, x1, x2

            if x1 == 12237:                        
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12237")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))
                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                        (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3, justify="center", text=data[0],bg='white',
                        font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12241:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12241")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=170, height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))


                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                        (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3, justify="center", text=data[0],bg='white',
                        font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12245:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12245")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                    self.Destination = Label(self.window3, text=data[2], justify="center",bg='white',
                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1], justify="center",bg='white',
                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))

                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                        (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3, justify="center", text=data[0],bg='white',
                        font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12249:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12249")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(x=170, y=170,height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1], justify="center",bg='white',
                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3], justify="center",bg='white',
                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))

                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                        (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3, justify="center", text=data[0],bg='white',
                        font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()


            Label(self.window3, text="Have a nice trip!!", bg='white',font=('Slab Serif', 17)).place(x=200, y=340)

            #mainloop()

    #mainloop()

    #self.PassengerDetails()

    def PassengerDetails4(self):
        global x1
        if self.en29.get() == "12238":
            x1 = 12238
        elif self.en29.get() == "12242":
            x1 = 12242
        elif self.en29.get() == "12246":
            x1 = 12246
        else:
            x1=12250

             #def PassengerDetails():
        #self.root.destroy()
        self.window2 = Tk()
        self.window2.title("Passenger Details")
        self.window2.config(bg="green")
        screen_width = self.window2.winfo_screenwidth()
        screen_height = self.window2.winfo_screenheight()
        width = 700
        height = 200
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window2.resizable(0, 0)

        height = 5
        width = 5
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.e1 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn2 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn3 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.enn4 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e5 = Entry(self.window2, justify="center", font=('Slab Serif', 10), bg="orange")
                self.e6 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn7 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn8 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.enn9 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e10 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e11 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e12 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e13 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e14 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e15 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e16 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e17 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e18 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e19 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e20 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e21 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e22 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e23 = Entry(self.window2, justify="center", font=('Slab Serif', 9), bg="yellow")
                self.e24 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e25 = Entry(self.window2, justify="center", font=('Slab Serif', 3))
                self.e1.insert(10, "S.no")
                self.enn2.insert(10, "Name")
                self.enn3.insert(10, "Age")
                self.enn4.insert(10, "Gender")
                self.e5.insert(10, "IdProof")
                self.e6.insert(10, "1")

                self.e11.insert(10, "2")
                self.e16.insert(10, "3")
                self.e21.insert(10, "4")

                self.e1.grid(row=0, column=0)
                self.enn2.grid(row=0, column=1)
                self.enn3.grid(row=0, column=2)
                self.enn4.grid(row=0, column=3)
                self.e5.grid(row=0, column=4)
                self.e6.grid(row=1, column=0)
                self.enn7.grid(row=1, column=1)
                self.enn8.grid(row=1, column=2)
                self.enn9.grid(row=1, column=3)
                self.e10.grid(row=1, column=4)

                self.e11.grid(row=2, column=0)
                self.e12.grid(row=2, column=1)
                self.e13.grid(row=2, column=2)
                self.e14.grid(row=2, column=3)
                self.e15.grid(row=2, column=4)

                self.e16.grid(row=3, column=0)
                self.e17.grid(row=3, column=1)
                self.e18.grid(row=3, column=2)
                self.e19.grid(row=3, column=3)
                self.e20.grid(row=3, column=4)

                self.e21.grid(row=4, column=0)
                self.e22.grid(row=4, column=1)
                self.e23.grid(row=4, column=2)
                self.e24.grid(row=4, column=3)
                self.e25.grid(row=4, column=4)

                def fun(*args):
                    self.enn9.insert(10, self.v2.get())

                def fun1(*args):
                    self.e14.insert(10, self.v3.get())

                def fun2(*args):
                    self.e19.insert(10, self.v4.get())

                def fun3(*args):
                    self.e24.insert(10, self.v5.get())

                def fun4(*args):
                    self.e10.insert(10, self.v6.get())

                def fun5(*args):
                    self.e15.insert(10, self.v7.get())

                def fun6(*args):
                    self.e20.insert(10, self.v8.get())

                def fun7(*args):
                    self.e25.insert(10, self.v9.get())

                self.v2 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v2.set('Select')
                self.v2.trace("w", fun)
                self.popupMenu1 = OptionMenu(self.window2, self.v2, *gender)
                self.popupMenu1.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu1.grid(row=1, column=3)

                self.v3 = StringVar(self.window2)
                gender1 = {'Male', 'Female'}
                self.self.v3.set('Select')
                self.v3.trace("w", fun1)
                self.popupMenu2 = OptionMenu(self.window2, self.v3, *gender1)
                self.popupMenu2.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu2.grid(row=2, column=3)

                self.v4 = StringVar(self.window2)
                gender2 = {'Male', 'Female'}
                self.v4.set('Select')
                self.v4.trace("w", fun2)
                self.popupMenu3 = OptionMenu(self.window2, self.v4, *gender2)
                self.popupMenu3.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu3.grid(row=3, column=3)

                self.v5 = StringVar(self.window2)
                gender = {'Male', 'Female'}
                self.v5.set('Select')
                self.v5.trace("w", fun3)
                self.popupMenu4 = OptionMenu(self.window2, self.v5, *gender)
                self.popupMenu4.config(font=('Slab Serif', 9), bg="purple", fg='white')
                self.popupMenu4.grid(row=4, column=3)

                self.v6 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v6.set('Select')
                self.v6.trace("w", fun4)
                self.popup = OptionMenu(self.window2, self.v6, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=1, column=4)

                self.v7 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v7.set('Select')
                self.v7.trace("w", fun5)
                self.popup = OptionMenu(self.window2, self.v7, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=2, column=4)

                self.v8 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v8.set('Select')
                self.v8.trace("w", fun6)
                self.popup = OptionMenu(self.window2, self.self.v8, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=3, column=4)

                self.v9 = StringVar(self.window2)
                proof = {'Aadhar card', 'Pan card'}
                self.v9.set('Select')
                self.v9.trace("w", fun7)
                self.popup = OptionMenu(self.window2, self.v9, *proof)
                self.popup.config(font=('Slab Serif', 9), bg="light green")
                self.popup.grid(row=4, column=4)
        self.b = Button(self.window2, text='Submit', bg="cyan", font=('Slab Serif', 11), command=self.Check4)
        self.b.place(x=250, y=155, width=100)

        def Check4(self):
            global count
            count=0
            if len(self.enn7.get()) == 0 or len(self.enn8.get()) == 0 or len(self.enn9.get()) == 0 or len(self.e10.get()) == 0:
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif len(self.e12.get()) != 0 and (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif len(self.e17.get()) != 0 and (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif len(self.e22.get()) != 0 and (len(self.e23.get()) == 0 or len(self.e24.get()) == 0 or len(self.e25.get()) == 0):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif (len(self.e12.get()) != 0 or len(self.e13.get()) != 0 or len(self.e14.get()) != 0 or len(
                self.e15.get()) != 0) and (
                len(self.e22.get()) != 0 or len(self.e23.get()) != 0 or len(self.e24.get()) != 0 or len(
                self.e25.get()) != 0) and (
                len(self.e17.get()) == 0 or (len(self.e18.get()) == 0 or len(self.e19.get()) == 0 or len(self.e20.get()) == 0)):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif (len(self.enn7.get()) != 0 or len(self.enn8.get()) != 0 or len(self.enn9.get()) != 0 or len(
                self.e10.get()) != 0) and (
                len(self.e17.get()) != 0 or len(self.e18.get()) != 0 or len(self.e19.get()) != 0 or len(
                self.e20.get()) != 0) and (
                len(self.e12.get()) == 0 or (len(self.e13.get()) == 0 or len(self.e14.get()) == 0 or len(self.e15.get()) == 0)):
                tkinter.messagebox.showinfo('Error', 'enter all required fields')
            elif  self.enn7.get()!="" and self.e12.get()=="" and self.e17.get()=="" and self.e22.get()=="":
                count=1
                self.Show4()
            elif self.e12.get()!="" and self.e17.get()=="":
                count=2
                self.Show4()
            elif self.e17.get()!="" and self.e22.get()=="":
                count=3
                self.Show4()
            elif self.e22.get()!="":
                count=4
                self.Show4()
            else:
                self.Show4()


        def Show4(self):
            global x1
            self.root.destroy()
            self.window3 = Tk()
            self.window3.title("Ticket")
            screen_width = self.window3.winfo_screenwidth()
            screen_height = self.window3.winfo_screenheight()
            width = 580
            height = 480
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            self.window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.window3.resizable(0, 0)

            Label(self.window3, text="Name",bg='white', font=('Slab Serif', 11)).place(x=90, y=50)
            Label(self.window3, text="Gender",bg='white', font=('Slab Serif', 11)).place(x=320, y=50)
            Label(self.window3, text="Departure time",bg='white', font=('Slab Serif', 11)).place(x=60, y=90)
            Label(self.window3, text="Age",bg='white', font=('Slab Serif', 11)).place(x=320, y=90)
            Label(self.window3, text="Class",bg='white', font=('Slab Serif', 11)).place(x=320, y=130)
            Label(self.window3, text="Train no.",bg='white', font=('Slab Serif', 11)).place(x=90, y=130)
            Label(self.window3, text="Train name",bg='white', font=('Slab Serif', 11)).place(x=90, y=170)
            Label(self.window3, text="Source",bg='white', font=('Slab Serif', 11)).place(x=90, y=210)
            Label(self.window3, text="Destination",bg='white', font=('Slab Serif', 11)).place(x=90, y=250)
            Label(self.window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

            Label(self.window3, text="PNR no",bg='white', font=('Slab Serif', 11)).place(x=320, y=170)

            self.Name = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=50, height=25)
            self.Gender = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=50, height=25)
            self.DepartureTime = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=170, y=90,height=25)
            self.Age = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10)).place(x=380, y=90, height=25)
            self.Class = Label(self.window3, justify="center",bg='white',text=variable2.get(), font=('Slab Serif', 10)).place(x=380, y=130, height=25)
            self.TrainNumber = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 10))
            self.TrainNumber.place(x=170, y=130, height=25)

            self.Source = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=170, height=25)
            self.Destination = Label(self.window3, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=250,height=25)
            self.Number = Label(self.window3,text=count, justify="center",bg='white', font=('Slab Serif', 9)).place(x=170, y=290, height=25)
            global conn, cursor, x1, x2

            if x1 == 12238:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12238")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))


                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3,bg='white', justify="center", text=data[0],
                                    font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12242:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12242")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=170, height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))


                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:

                    self.pnr1 = Label(self.window3,bg='white', justify="center", text=data[0],
                                    font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2],bg='white', justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3], bg='white',justify="center", font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12246:
                cursor = conn.cursor()
                TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12246")
                fetch = cursor.fetchall()
                for data in fetch:
                    Source = Label(self.window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(
                        x=170, y=170, height=25)
                    Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))

                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:


                    self.pnr1 = Label(self.window3, justify="center",bg='white', text=data[0],
                                    font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    self.Name = Label(self.window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    self.Age = Label(self.window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    self.Gender = Label(self.window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()
            elif x1 == 12250:
                cursor = conn.cursor()
                self.TrainNumber.config(text=x1)
                cursor.execute("Select * from Rail88 where Trainnumber=12250")
                fetch = cursor.fetchall()
                for data in fetch:
                    self.Source = Label(self.window3, text=data[5], bg='white',justify="center", font=('Slab Serif', 10)).place(x=170, y=170,height=25)
                    self.Destination = Label(self.window3, text=data[2],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=250, height=25)
                    self.TrainName = Label(self.window3, text=data[1],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=210, height=25)
                    self.DepartureTime = Label(self.window3, text=data[3],bg='white', justify="center",
                                        font=('Slab Serif', 10)).place(x=170, y=90, height=25)

                a = 111111
                b = 999999
                pnr = (random.randint(a, b))

                cursor.execute("Insert into Rail999 (pnr,Name,Gender,Age) values (?,?,?,?)",
                                (pnr, str(enn7.get()), int(enn8.get()), str(enn9.get())))

                conn.commit()

                cursor.execute("Select * from Rail999 where pnr=?  ", (pnr,))
                fetch1 = cursor.fetchall()
                for data in fetch1:
                    self.pnr1 = Label(self.window3, justify="center",bg='white', text=data[0],
                                    font=('Slab Serif', 9))
                    self.pnr1.place(x=380, y=170, height=25)
                    self.pnr1.config(text=data[0])
                    Name = Label(self.window3, text=data[1], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=170, y=50, height=25)
                    Age = Label(self.window3, text=data[2], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=90, height=25)
                    Gender = Label(self.window3, text=data[3], justify="center",bg='white', font=('Slab Serif', 9)).place(
                        x=380, y=50, height=25)

                cursor.close()
                conn.close()


            Label(self.window3, text="Have a nice trip!!", bg='white',font=('Slab Serif', 17)).place(x=200, y=340)

            #mainloop()

        
    #mainloop()

    #self.PassengerDetails()

    def Back1(self):
        self.root.destroy()


    #mainloop()


    def Cancellation(self):
        self.root.destroy()
        self.window4 = Tk()
        self.window4.title("Cancel Ticket")

        screen_width = self.window4.winfo_screenwidth()
        screen_height = self.window4.winfo_screenheight()
        width = 410
        height = 400
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.window4.resizable(0, 0)

        self.window4.config(bg='purple')
        self.cancel = Label(self.window4, text="PNR NO", font=('Slab Serif', 15), bg="purple", fg="white").place(x=100, y=150,
                                                                                                       width=90)
        self.e=Entry(self.window4,justify="center", font=('Slab Serif', 15), bg="white")
        self.e.place(x=210, y=150, width=100)
        Button(self.window4, text="Back", font=('Slab Serif', 15), bg="green", fg="white",command=self.Back).place(x=80,y=250, width=120)

        Button(self.window4, text="Delete", font=('Slab Serif', 15), bg="green", fg="white",command=self.Delete).place(x=220, y=250, width=120)

    def Delete1(self):
        self.result = tkinter.messagebox.askquestion('Ask', 'Are you sure you want to delete your booked ticket?',
                                              icon="warning")
        if self.result == 'yes':
            cursor = conn.cursor()
            cursor.execute("Select pnr from Rail999")
            d = cursor.fetchall()

            at=str(d)
            d1=at.replace('(','')
            d2 = d1.replace(')', '')
            d3 = d2.replace(',', '')
            d4=d3.replace('[','')
            d5 = d4.replace(']', '')
            d6=d5.split(' ')
            q=0
            for i in range(1,len(d6)):
                if self.e.get()==d6[i]:
                    x123=self.e.get()
                    q=1
            if q==1:
                cursor.execute("Delete from Rail999 where pnr=?",(x123,))
                tkinter.messagebox.showinfo('Success', 'Ticket Deleted Successfully')
                #self.window4.destroy()
            else:
                tkinter.messagebox.showinfo('Error', 'Ticket Not Found!')

            cursor.close()
            conn.close()


    def Delete(self):
        if (len(self.e.get())==""):
            tkinter.messagebox.showinfo('Error', 'Enter required pnr no.')
        else:
            self.Delete1()

    def Back(self):
        self.root.destroy()


    #mainloop()
    #e1.config(bg="yellow")

    #e1.place(x=210,y=160,height=30,width=100)
    
    

    
if __name__=="__main__":
    main()


