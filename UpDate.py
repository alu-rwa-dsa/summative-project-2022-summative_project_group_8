import mysql.connector
import Slot
import PStack
from Linked import LinkedList

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="registerdb"
)
mycursor = db.cursor()


class Update:
    def __int__(self):
        pass

    def king_faisal(self):

        userInputId = input("Please enter your password ")
        try:
            # mycursor.execute("select * from user where password = '%s';" % userInputId)
            userDetails = "select * from user where password = '%s';" % userInputId
            if userDetails == " ":
                print("Invalid password")
                return
            else:
                mycursor.execute(userDetails)
                myresult = mycursor.fetchall()

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")
        except:
            print("An exception occurred, your id was not found")
            return

        confirm = input("Do you still want to edit your appointment time?(y/n) ").lower()
        if confirm == "y":
            # Print available slots at King Faisal Hospital
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
                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()
                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * user where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at King-Faisal Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("Password:", row[1])
                    print("Firstname: ", row[2])
                    print("Lastname: ", row[3])
                    print("Time: ", row[4])
                    print("\n")

            elif slot == "2":

                a = Slot.s.items[1]
                # Popping the selected time slot from the stack
                Slot.s.items.pop(1)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()
                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at King-Faisal Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("Password:", row[1])
                    print("Firstname: ", row[2])
                    print("Lastname: ", row[3])
                    print("Time: ", row[4])
                    print("\n")

            elif slot == "3":
                a = Slot.s.items[2]
                Slot.s.items.pop(2)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at King-Faisal Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("Password:", row[1])
                    print("Firstname: ", row[2])
                    print("Lastname: ", row[3])
                    print("Time: ", row[4])
                    print("\n")

    def chuk_hospital(self):

        userInputId = input("Please enter your password ")
        try:
            mycursor.execute("select * from user2 where password = '%s';" % userInputId)
            myresult = mycursor.fetchall()
            # prints out the users details
            for row in myresult:
                print("userid: ", row[0])
                print("password:", row[1])
                print("first_name: ", row[2])
                print("last_name: ", row[3])
                print("time: ", row[4])
                print("\n")
        except:
            print("An exception occurred, your id was not found")
            return


        confirm = input("Do you still want to edit your appointment time?(y/n) ").lower()
        if confirm == "y":

            # Print available slots at King Faisal Hospital

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

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user2 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user2 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at Chuk Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")

            elif slot == "2":

                a = Slot.s.items[1]
                # Popping the selected time slot from the stack
                Slot.s.items.pop(1)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user2 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user2 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at Chuk Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")

            elif slot == "3":
                a = Slot.s.items[2]
                Slot.s.items.pop(2)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user2 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user2 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at Chuk Hospital")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")

    def Polyfam_clinic(self):

        userInputId = input("Please enter your password ")
        try:
            mycursor.execute("select * from user3 where password = '%s';" % userInputId)
            myresult = mycursor.fetchall()

            for row in myresult:
                print("userid: ", row[0])
                print("password:", row[1])
                print("first_name: ", row[2])
                print("last_name: ", row[3])
                print("time: ", row[4])
                print("\n")
        except:
            print("An exception occurred, your id was not found")
            return

        confirm = input("Do you still want to edit your appointment time?(y/n) ").lower()
        if confirm == "y":

            # Print available slots at King Faisal Hospital

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

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user3 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user3 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at Polyfarm")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")

            elif slot == "2":

                a = Slot.s.items[1]
                # Popping the selected time slot from the stack
                Slot.s.items.pop(1)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user3 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user3 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()
                print("Below is your updated appointment at Polyfarm Clinic")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")

            elif slot == "3":
                a = Slot.s.items[2]
                Slot.s.items.pop(2)
                # push the removed timeslot to another stack in a file named three. The file can be renamed.
                PStack.p.push(a)

                mycursor.execute("set @item:='%s'" % a)
                mycursor.execute("UPDATE user3 SET time = @item WHERE password = '%s' " % userInputId)
                db.commit()

                list = LinkedList()
                for i in mycursor:
                    list.insert(i)
                # UPDATING ENDS HERE

                # VIEWING STARTS

                mycursor.execute("select * from user3 where password = '%s';" % userInputId)
                myresult = mycursor.fetchall()

                print("Below is your updated appointment at Polyfarm Clinic")

                for row in myresult:
                    print("userid: ", row[0])
                    print("password:", row[1])
                    print("first_name: ", row[2])
                    print("last_name: ", row[3])
                    print("time: ", row[4])
                    print("\n")
