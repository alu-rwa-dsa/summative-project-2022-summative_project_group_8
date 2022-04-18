from Slot import s
from Linked import LinkedList
from PStack import p
import Slot
import PStack
import mysql.connector


conn = mysql.connector.connect(host='localhost',
                               database='registerdb',
                               user='root',
                               password=''
                               )
mycursor = conn.cursor()


class Deleting:
    def king_faisal(self):

        list = LinkedList()

        mycursor.execute("SELECT userid FROM user")
        myresult = mycursor.fetchall()

        for i in myresult:
            for j in i:
                list.insert(j)


        print("TO DELETE YOUR APPOINTMENT ENTER YOUR ID:")

        id = int(input("Enter your id: "))
        if id in i:
            list.deleteKey(id)
            # list.display()

            mycursor.execute("DELETE FROM user WHERE userid = '%s';" % id)
            conn.commit()
            print("YOUR APPOINTMENT HAS BEEN DELETED")
            if p.isEmpty():
                print(" ")
            else:
                a = p.items[0]
                p.items.pop(0)
                s.push(a)

        else:
            print("INCORRECT ID.")

    def chuk_hospital(self):
        list = LinkedList()

        mycursor.execute("SELECT userid FROM user2")
        myresult = mycursor.fetchall()

        for i in myresult:
            for j in i:
                list.insert(j)

        print("TO DELETE YOUR APPOINTMENT ENTER YOUR ID:")
        id = int(input("Enter your id: "))
        if id in i:
            list.deleteKey(id)
            # list.display()

            mycursor.execute("DELETE FROM user2 WHERE userid = '%s';" % id)
            conn.commit()
            print("YOUR APPOINTMENT HAS BEEN DELETED")
            if p.isEmpty():
                print(" ")
            else:
                a = p.items[0]
                p.items.pop(0)
                s.push(a)

        else:
            print("INCORRECT ID.")

    def Polyfam_clinic(self):
        list = LinkedList()

        mycursor.execute("SELECT userid FROM user3")
        myresult = mycursor.fetchall()

        for i in myresult:
            for j in i:
                list.insert(j)

        print("TO DELETE YOUR APPOINTMENT ENTER YOUR ID:")
        id = int(input("Enter your id: "))
        if id in i:
            list.deleteKey(id)
            # list.display()

            mycursor.execute("DELETE FROM user3 WHERE userid = '%s';" % id)
            conn.commit()
            print("YOUR APPOINTMENT HAS BEEN DELETED")
            if p.isEmpty():
                print(" ")
            else:
                a = p.items[0]
                p.items.pop(0)
                s.push(a)

        else:
            print("INCORRECT ID.")

