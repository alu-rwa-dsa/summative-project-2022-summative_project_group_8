
import mysql.connector

class View:
    def king_faisal(self):
        # connect to the database
        global conn, mycursor, a
        conn = mysql.connector.connect(host='localhost',
                                       database='registerdb',
                                       user='root',
                                       password=''
                                       )
        mycursor = conn.cursor()


        # VIEWING STARTS
        print("--Appointment details for King-Faisal Hospital")
        pas = input("Enter your password that you signed up with")

        print("Below are your appointment details")
        try:
            # fetch the password from the table in the database
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
        except:
            print("An exception occurred, your password was not found")
            return

        mycursor.close()
        conn.close()
#-----------------------------------------------------------------------------------------------------------------

    def chuk_hospital(self):
        global conn, mycursor, a
        conn = mysql.connector.connect(host='localhost',
                                       database='registerdb',
                                       user='root',
                                       password=''
                                       )
        mycursor = conn.cursor()

        # VIEWING STARTS
        print("--Appointment details for Chuk Hospital")
        pas = input("Enter your password that you signed up with")

        print("Below are your appointment details")

        try:

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
        except:
            print("An exception occurred, your password was not found")
            return

        mycursor.close()
        conn.close()
#---------------------------------------------------------------------------------------------------------------
    def Polyfam_clinic(self):
        global conn, mycursor, a
        conn = mysql.connector.connect(host='localhost',
                                       database='registerdb',
                                       user='root',
                                       password=''
                                       )
        mycursor = conn.cursor()

        # VIEWING STARTS
        print("--Appointment details for Polyfarm Clinic")
        pas = input("Enter your password that you signed up with")
        print("Below are your appointment details")

        try:
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
        except:
            print("An exception occurred, your password was not found")
            return

        mycursor.close()
        conn.close()

# v= View()
# v.king_faisal()