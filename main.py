from mysql.connector import cursor
from Views import View
from UpDate import Update
from delete import Deleting
import Slot
from Linked import Node
from Linked import LinkedList
import PStack
import mysql.connector
import tkinter.messagebox as tkMessageBox
from tkinter import *



class Booking:
    def king_faisal(self):
        print(".....King-Faisal hospital")

        print("Choose from the available slots:")
        for i in Slot.s.items:
            print(Slot.s.items.index(i) + 1, ")", i)
        slot = input()
        if slot == "1":
            a = Slot.s.items[0]
            # Popping the selected time slot from the stack
            Slot.s.items.pop(0)
            # push the removed timeslot to another stack in a file named three. The file can be renamed.
            PStack.p.push(a)
        elif slot == "2":
            a = Slot.s.items[1]
            # Popping the selected time slot from the stack
            PStack.p.push(a)
            Slot.s.items.pop(1)
        elif slot == "3":
            a = Slot.s.items[2]
            Slot.s.items.pop(2)
            PStack.p.push(a)

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

        # =======================================METHODS=======================================
        def Database():
            global conn, mycursor, a
            conn = mysql.connector.connect(host='localhost',
                                           database='registerdb',
                                           user='root',
                                           password=''
                                           )
            mycursor = conn.cursor()

        def Exit():
            result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
            if result == 'yes':
                root.destroy()
                exit()

        def Register():
            Database()
            mycursor.execute("INSERT INTO `user` (password, first_name, last_name, time) VALUES(%s, %s, %s, %s)",
                             (str(password.get()), str(first_name.get()), str(last_name.get()), a))
            conn.commit()
            lbl_result.config(text="Successfully Created!", fg="green")

            # VIEWING STARTS
            pas = input("Enter your password")
            print("Below are your appointment details at King-Faisal")

            mycursor.execute("select * from user where password = '%s';" % pas)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("---------------------")
                print("userid: ", row[0])
                print("password: ", row[1])
                print("first_name: ", row[2])
                print("last_name: ", row[3])
                print("time:", row[4])
                print("\n")

            mycursor.close()
            conn.close()

        # =====================================FRAMES====================================
        TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
        TitleFrame.pack(side=TOP)
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=20)

        # =====================================LABEL WIDGETS=============================
        lbl_title = Label(TitleFrame, text="D.Y.M.K-Hospital Management System - Booking Form", font=('arial', 18),
                          bd=1,
                          width=640)
        lbl_title.pack()
        lbl_password = Label(RegisterFrame, text="password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=1)
        lbl_first_name = Label(RegisterFrame, text="first_name:", font=('arial', 18), bd=18)
        lbl_first_name.grid(row=2)
        lbl_last_name = Label(RegisterFrame, text="last_name:", font=('arial', 18), bd=18)
        lbl_last_name.grid(row=3)
        # lbl_time = Label(RegisterFrame, text="time:", font=('arial', 18), bd=18)
        # lbl_time.grid(row=4)
        lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result.grid(row=5, columnspan=2)

        # =======================================ENTRY WIDGETS===========================
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=password, width=15, show="*")
        password.grid(row=1, column=1)
        first_name = Entry(RegisterFrame, font=('arial', 20), textvariable=first_name, width=15)
        first_name.grid(row=2, column=1)
        last_name = Entry(RegisterFrame, font=('arial', 20), textvariable=last_name, width=15)
        last_name.grid(row=3, column=1)
        # time = Entry(RegisterFrame, font=('arial', 20), textvariable=time, width=15)
        # time.grid(row=4, column=1)
        # # ========================================BUTTON WIDGETS=========================
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

    # ------------------------------------------------------------------------------------------------------------
    def chuk_hospital(self):
        print("....Chuk Hospital")
        print("Choose from the available slots:")
        for i in Slot.s.items:
            print(Slot.s.items.index(i) + 1, ")", i)
        slot = input()
        if slot == "1":
            a = Slot.s.items[0]
            # Popping the selected time slot from the stack
            Slot.s.items.pop(0)
            # push the removed timeslot to another stack in a file named three. The file can be renamed.
            PStack.p.push(a)
        elif slot == "2":
            a = Slot.s.items[1]
            # Popping the selected time slot from the stack
            PStack.p.push(a)
            Slot.s.items.pop(1)
        elif slot == "3":
            a = Slot.s.items[2]
            Slot.s.items.pop(2)
            PStack.p.push(a)

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

        # =======================================METHODS=======================================
        def Database():
            global conn, mycursor, a
            conn = mysql.connector.connect(host='localhost',
                                           database='registerdb',
                                           user='root',
                                           password=''
                                           )
            mycursor = conn.cursor()

        def Exit():
            result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
            if result == 'yes':
                root.destroy()
                exit()

        def Register():
            Database()
            mycursor.execute("INSERT INTO `user2` (password, first_name, last_name, time) VALUES(%s, %s, %s, %s)",
                             (str(password.get()), str(first_name.get()), str(last_name.get()), a))
            conn.commit()
            lbl_result.config(text="Successfully Created!", fg="green")

            # VIEWING STARTS
            pas = input("Enter your password")
            print("Below are your appointment details at Chuk Hospital")

            mycursor.execute("select * from user2 where password = '%s';" % pas)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("---------------------")
                print("userid: ", row[0])
                print("password: ", row[1])
                print("first_name: ", row[2])
                print("last_name: ", row[3])
                print("time:", row[4])
                print("\n")

            mycursor.close()
            conn.close()

        # =====================================FRAMES====================================
        TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
        TitleFrame.pack(side=TOP)
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=20)

        # =====================================LABEL WIDGETS=============================
        lbl_title = Label(TitleFrame, text="D.Y.M.K-Hospital Management System - Booking Form", font=('arial', 18),
                          bd=1,
                          width=640)
        lbl_title.pack()
        lbl_password = Label(RegisterFrame, text="password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=1)
        lbl_first_name = Label(RegisterFrame, text="first_name:", font=('arial', 18), bd=18)
        lbl_first_name.grid(row=2)
        lbl_last_name = Label(RegisterFrame, text="last_name:", font=('arial', 18), bd=18)
        lbl_last_name.grid(row=3)
        # lbl_time = Label(RegisterFrame, text="time:", font=('arial', 18), bd=18)
        # lbl_time.grid(row=4)
        lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result.grid(row=5, columnspan=2)

        # =======================================ENTRY WIDGETS===========================
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=password, width=15, show="*")
        password.grid(row=1, column=1)
        first_name = Entry(RegisterFrame, font=('arial', 20), textvariable=first_name, width=15)
        first_name.grid(row=2, column=1)
        last_name = Entry(RegisterFrame, font=('arial', 20), textvariable=last_name, width=15)
        last_name.grid(row=3, column=1)
        # time = Entry(RegisterFrame, font=('arial', 20), textvariable=time, width=15)
        # time.grid(row=4, column=1)
        # # ========================================BUTTON WIDGETS=========================
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
#---------------------------------------------------------------------------------------------------------------

    def Polyfam_clinic(self):
        print("...Polyfarm Clinic")
        print("Choose from the available slots:")
        for i in Slot.s.items:
            print(Slot.s.items.index(i) + 1, ")", i)
        slot = input()
        if slot == "1":
            a = Slot.s.items[0]
            # Popping the selected time slot from the stack
            Slot.s.items.pop(0)
            # push the removed timeslot to another stack in a file named three. The file can be renamed.
            PStack.p.push(a)
        elif slot == "2":
            a = Slot.s.items[1]
            # Popping the selected time slot from the stack
            PStack.p.push(a)
            Slot.s.items.pop(1)
        elif slot == "3":
            a = Slot.s.items[2]
            Slot.s.items.pop(2)
            PStack.p.push(a)

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

        # =======================================METHODS=======================================
        def Database():
            global conn, mycursor, a
            conn = mysql.connector.connect(host='localhost',
                                           database='registerdb',
                                           user='root',
                                           password=''
                                           )
            mycursor = conn.cursor()

        def Exit():
            result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
            if result == 'yes':
                root.destroy()
                exit()

        def Register():
            Database()
            mycursor.execute("INSERT INTO `user3` (password, first_name, last_name, time) VALUES(%s, %s, %s, %s)",
                             (str(password.get()), str(first_name.get()), str(last_name.get()), a))
            conn.commit()
            lbl_result.config(text="Successfully Created!", fg="green")

            # VIEWING STARTS
            pas = input("Enter your password")
            print("Below are your appointment details at Polyfam Clinic")

            mycursor.execute("select * from user3 where password = '%s';" % pas)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("---------------------")
                print("userid: ", row[0])
                print("password: ", row[1])
                print("first_name: ", row[2])
                print("last_name: ", row[3])
                print("time:", row[4])
                print("\n")

            mycursor.close()
            conn.close()

        # =====================================FRAMES====================================
        TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
        TitleFrame.pack(side=TOP)
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=20)

        # =====================================LABEL WIDGETS=============================
        lbl_title = Label(TitleFrame, text="D.Y.M.K-Hospital Management System - Booking Form", font=('arial', 18),
                          bd=1,
                          width=640)
        lbl_title.pack()
        lbl_password = Label(RegisterFrame, text="password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=1)
        lbl_first_name = Label(RegisterFrame, text="first_name:", font=('arial', 18), bd=18)
        lbl_first_name.grid(row=2)
        lbl_last_name = Label(RegisterFrame, text="last_name:", font=('arial', 18), bd=18)
        lbl_last_name.grid(row=3)
        # lbl_time = Label(RegisterFrame, text="time:", font=('arial', 18), bd=18)
        # lbl_time.grid(row=4)
        lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result.grid(row=5, columnspan=2)

        # =======================================ENTRY WIDGETS===========================
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=password, width=15, show="*")
        password.grid(row=1, column=1)
        first_name = Entry(RegisterFrame, font=('arial', 20), textvariable=first_name, width=15)
        first_name.grid(row=2, column=1)
        last_name = Entry(RegisterFrame, font=('arial', 20), textvariable=last_name, width=15)
        last_name.grid(row=3, column=1)
        # time = Entry(RegisterFrame, font=('arial', 20), textvariable=time, width=15)
        # time.grid(row=4, column=1)
        # # ========================================BUTTON WIDGETS=========================
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


def redo():
    choose = input("\nWould you like to redo the program? (yes/no)\n")
    if choose == "yes":
        return display()
    else:
        exit()


def display():
    print("-----WELCOME TO D.Y.M.K Hospital Booking Services")
    Choice = input("""Available service: 
                    1) Booking 
                    2) Update an appointment
                    3) Delete an appointment 
                    4) View appointments 
                    """)

    Hospitals = ['King-Faisal Hospital', 'CHUK Hospital', 'Polyfam Clinic']

    book = Booking()
    v= View()
    u = Update()
    d = Deleting()
    if Choice == "1":
        print("Available hospitals: ")
        a = 1
        for i in Hospitals:
            print(Hospitals.index(i) + 1, ")", i)
        hos = input()
        if hos == "1":
            book.king_faisal()
            redo()
        elif hos == "2":
            book.chuk_hospital()
            redo()
        elif hos == "3":
            book.Polyfam_clinic()
            redo()
        else:
            print("Invalid choice. Try again")
            redo()
    elif Choice == "2":
        print("These are the available hospitals:")
        a = 1
        for i in Hospitals:
            print(Hospitals.index(i) + 1, ")", i)
        hos = input()
        if hos == "1":
            u.king_faisal()
            redo()
        elif hos == "2":
            u.chuk_hospital()
            redo()
        elif hos == "3":
            u.Polyfam_clinic()
            redo()
        else:
            print("Invalid choice. Try again")
            redo()
    elif Choice == "3":
        print("These are the available hospitals:")
        a = 1
        for i in Hospitals:
            print(Hospitals.index(i) + 1, ")", i)
        hos = input()
        if hos == "1":
            d.king_faisal()
            redo()
        elif hos == "2":
            d.chuk_hospital()
            redo()
        elif hos == "3":
            d.Polyfam_clinic()
            redo()
        else:
            print("Invalid Choice. Try again")
            redo()
    elif Choice == "4":
        print("These are the available hospitals:")
        a = 1
        for i in Hospitals:
            print(Hospitals.index(i) + 1, ")", i)
        hos = input()
        if hos == "1":
            v.king_faisal()
            redo()
        elif hos == "2":
            v.chuk_hospital()
            redo()
        elif hos == "3":
            v.Polyfam_clinic()
            redo()
        else:
            print("Invalid choice.try again")
            redo()
    else:
        print("Invalid choice try again")
        redo()

display()
