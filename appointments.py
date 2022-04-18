import tkinter.messagebox as tkMessageBox
from tkinter import *
import mysql.connector
from mysql.connector import Error

root = Tk()
root.title("Appointment Registration Form")

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# =======================================VARIABLES=====================================
password = StringVar()
first_name = StringVar()
last_name = StringVar()
age = StringVar()


# =======================================METHODS=======================================
def Database():
    global conn, mycursor
    conn = mysql.connector.connect(host='localhost',
                                   database='registerdb',
                                   user='root',
                                   password=''
                                   )
    mycursor = conn.cursor()

    # if conn.is_connected():
    #     print("connected")
    # else:
    #     print("Error")
    # conn.close()


# Database()


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Register():
    Database()
    # if password.get == "" or first_name.get() == "" or last_name.get() == "" or age.get == "":
    #     lbl_result.config(text="Please complete the required field!", fg="orange")
    # else:
    #     # mycursor.execute("SELECT * FROM `user` WHERE `user` = %s")
    #     mycursor.execute("SELECT * FROM user WHERE first_name = 'Maxine' AND last_name = 'Bnei'")
    #
    #     # 91;USER.get()])
    # if mycursor.fetchone() is not None:
    #     lbl_result.config(text="Username is already taken", fg="red")
    #
    # else:
    mycursor.execute("INSERT INTO `user` (password, first_name, last_name, age) VALUES(%s, %s, %s, %s)",
                     (str(password.get()), str(first_name.get()), str(last_name.get()), str(age.get())))
    conn.commit()
    # password.set("")
    # first_name.set("")
    # last_name.set("")
    # age.set("")
    lbl_result.config(text="Successfully Created!", fg="green")
    mycursor.close()
    conn.close()


# =====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)

# =====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="D.Y.M.K-Hospital Management System - Booking Form", font=('arial', 18), bd=1,
                  width=640)
lbl_title.pack()
lbl_password = Label(RegisterFrame, text="password:", font=('arial', 18), bd=18)
lbl_password.grid(row=1)
lbl_first_name = Label(RegisterFrame, text="first_name:", font=('arial', 18), bd=18)
lbl_first_name.grid(row=2)
lbl_last_name = Label(RegisterFrame, text="last_name:", font=('arial', 18), bd=18)
lbl_last_name.grid(row=3)
lbl_age = Label(RegisterFrame, text="age:", font=('arial', 18), bd=18)
lbl_age.grid(row=4)
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)

# =======================================ENTRY WIDGETS===========================
password = Entry(RegisterFrame, font=('arial', 20), textvariable=password, width=15, show="*")
password.grid(row=1, column=1)
first_name = Entry(RegisterFrame, font=('arial', 20), textvariable=first_name, width=15)
first_name.grid(row=2, column=1)
last_name = Entry(RegisterFrame, font=('arial', 20), textvariable=last_name, width=15)
last_name.grid(row=3, column=1)
age = Entry(RegisterFrame, font=('arial', 20), textvariable=age, width=15)
age.grid(row=4, column=1)
# ========================================BUTTON WIDGETS=========================
btn_register = Button(RegisterFrame, font=('arial', 20), text="Book", command=Register)
btn_register.grid(row=6, columnspan=2)
# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================INITIALIZATION===================================


if __name__ == '__main__':
    root.mainloop()
