from tkinter import *
from PIL import ImageTk, Image
import traintestdummy
import bustestdummy
import carfinal
import main
import os

class Main:
        def __init__(self, root):
            self.root = root
            pad = 3
            self.root.title("TRAVEL BOOKING MANAGEMENT SYSTEM")
            self.root.geometry(
                "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

            # create mainframe to add message
            top = Frame(self.root)
            top.pack(side="top")
                     
            self.img = ImageTk.PhotoImage(Image.open("Travel.png"))
            label=Label(self.root, image=self.img)
            label.place(x=0, y=20)
            
            # create frame to add buttons
            bottom = Frame(self.root)
            bottom.pack(side="top")

            # display message
            self.label = Label(top, font=('arial', 50, 'bold'), text="WELCOME", fg="blue", anchor="center")
            self.label.grid(row=0, column=3)

            # create check in button
            self.train_button = Button(bottom, text="TRAIN", font=('', 20), bg="pink", fg="black", relief=RAISED, height=2,
                                      width=20,anchor="center", command=traintestdummy.main)
            self.train_button.grid(row=0, column=2, padx=10, pady=10)
                                      
            # create check out button
            
            # create show list button
            self.car_button = Button(bottom, text="CAR", font=('', 20), bg="pink", relief=RAISED,
                                       height=2,
                                       width=20, fg="black", anchor="center", command=carfinal.main)
                                       # call main function from carfinal.py file
            self.car_button.grid(row=1, column=2, padx=10, pady=10)

            # create get information of all the guest
            self.bus_button = Button(bottom, text="BUS", font=('', 20), bg="pink",
                                      relief=RAISED, height=2, width=20, fg="black", anchor="center",command=bustestdummy.main)
            # call customer_info_ui function from customer_info.py file
            self.bus_button.grid(row=2, column=2, padx=10, pady=10)

            self.hotel_button = Button(bottom, text="HOTEL", font=('', 20), bg="pink",
                                      relief=RAISED, height=2, width=20, fg="black", anchor="center", command=main.home_ui)
                                      
            # call customer_info_ui function from customer_info.py file
            self.hotel_button.grid(row=3, column=2, padx=10, pady=10)



            # button to exit the program
            self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="pink", relief=RIDGE, height=2, width=20,
                                  fg="black", anchor="center", command=self.root.destroy)
            self.exit_button.grid(row=4, column=2, padx=10, pady=10)
        

def home_ui():
    root = Tk()
    application = Main(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
'''ws = Tk()
ws.title('TRAVEL MANAGEMENT SYSTEM')
ws.configure(bg='sky blue')
# Open the Image File
img = ImageTk.PhotoImage(Image.open("Travel.png"))
# Create a Canvas
canvas = Canvas(ws, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(20, 20, image=img, anchor='nw')
img = PhotoImage(file='Travel.png')
#Label(ws,image=img).pack()
btn=Button(ws, text="TRAIN", bg='black', fg='white',command=tf.train)
btn.place(x=300, y=500)
btn1=Button(ws, text="FLIGHT", bg='black', fg='white')
btn1.place(x=400, y=500)
btn2=Button(ws, text="BUS", bg='black', fg='white')
btn2.place(x=500, y=500)
btn3=Button(ws, text="CAR", bg='black', fg='white')
btn3.place(x=600, y=500)
btn4=Button(ws, text="HOTEL", bg='black', fg='white')
btn4.place(x=700, y=500)
ws.geometry("1000x700+30+50")
ws.title('TRAVEL MANAGEMENT SYSTEM')
ws.mainloop()'''
