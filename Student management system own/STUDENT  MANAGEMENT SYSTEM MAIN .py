
# STUDENT MANAGEMENT SYSTEM
# MADE BY HARSHIT PRASAD 
# PYTHON AND CSV USED

import csv
import os

# FUNCTION FOR ADDING STUDENTS

def add_stu():
    st=input("Enter number of students to add: ")
    print("")
    with open ("student.csv","w",newline="") as f:
        writer=csv.writer(f)
        lf=["ID" , "NAME" , "FATHER'S NAME" , "MOTHER'S NAME" , "CLASS" , "STREAM"]
        writer.writerow(lf)
        for i in range(int(st)):
                name=input("Enter student's name: ")
                fname=input("Enter student's father's name: ")
                mname=input("Enter student's mother's name: ")
                id=input("Enter the Id number of student: ")
                cl=(input("Enter the class of the student :"))
                stream =input("Enter stream of student(if no stream enter NONE): ")
                l=[id , name , fname , mname , cl , stream]
                writer.writerow(l)
                print("")
                print("Student has been added succesfully")
                print("")

# FUNCTION FOR VIEWING ALL THE STUDENTS

def view_stu():
    with open ("student.csv","r",newline="") as f:
        rd=csv.reader(f)
        print("\nVIEWING ALL STUDENTS\n")
        for i in rd:  
            print(i)

# FUNCTION FOR APPENDING STUDENTS

def app_stu():
    st=input("Enter number of students to append: ")
    print("")
    with open ("student.csv","a",newline="") as f:
        writer=csv.writer(f)
        for i in range(int(st)):
                name=input("Enter student's name: ")
                fname=input("Enter student's father's name: ")
                mname=input("Enter student's mother's name: ")
                id=input("Enter the Id number of student: ")
                cl=(input("Enter the class of the student :"))
                stream =input("Enter stream of student(if no stream enter NONE): ")
                l=[id , name , fname , mname , cl , stream]
                writer.writerow(l)
                print("")
                print("Student has been added succesfully")
                print("")

# FUNCTION FOR SEARCHING STUDENT

def search_stu():
    print("")
    sid = input("Enter Student ID to search: ")

    with open("student.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        flag=0
        for i in reader:
            if i["ID"]==sid:
                print("\n STUDENT FOUND\n")
                print("ID NUMBER:",i["ID"])
                print("NAME: ",i["NAME"])
                print("FATHER'S NAME: ",i["FATHER'S NAME"])
                print("MOTHER'S NAME: ",i["MOTHER'S NAME"])
                print("CLASS: ",i["CLASS"])
                print("STREAM: ",i["STREAM"])
                flag=1
        if flag==0:
            print("Student not found!")

# FUNCTION FOR UPDATING STUDENT DATA            

def update_stu():
    update=input("Enter the ID of the student for which you want to update data: ")
    up2=input("Enter what to update(name/class/stream): ")
    if up2.lower()=="name":
        with open ("student.csv","r") as f:
            rd=list(csv.reader(f))
            name=input("Enter new name: ")
            for i in rd:
                if i[0]==update:
                    i[1]=name
        with open ("student.csv","w",newline="") as n:
            w=csv.writer(n)
            w.writerows(rd)
            print("\nData Updated successfully\n")
    elif up2.lower()=="class":
        with open("student.csv","r") as f:
            r=list(csv.reader(f))
            cl=input("Enter new class: ")
            for i in r:
                if i[0]==update:
                    i[4]=cl
        with open("student.csv","w",newline="") as g:
            wr=csv.writer(g)
            wr.writerows(r)
            print("\nData Updated Successfully\n")
    elif up2.lower()=="stream":
        with open("student.csv","r") as k:
            rs=list(csv.reader(k))
            st=input("Enter new stream(if no stream type NONE): ")
            for i in rs:
                if i[0]==update:
                    i[5]=st
        with open("student.csv","w",newline="") as k:
            wr=csv.writer(k)
            wr.writerows(rs)
            print("\nData Updated Successfully\n")
    else:
        print("Data not updated")
        print("\n Either you have entered wrong category or the selected category is not available for updation\n")

# FUNCTION FOR DELETING STUDENT

def delete_stu():
    idin=input("Enter the id of the student you want to delete: ")
    found=False
    f=open("student.csv","r")
    rd=csv.reader(f)
    fn=open("new_student.csv","w",newline="")
    w=csv.writer(fn)
    for i in rd:
        if i[0]==idin:
            found=True
        else:
            w.writerow(i)
    f.close()
    fn.close()
    if found:
        os.remove("student.csv")
        os.rename("new_student.csv","student.csv")
        print("\nDATA DELETED SUCCESSFULLY\n")
    else:
        os.remove("new_student.csv")
        print("\nDATA NOT FOUND\n")

# MAIN PROGRAM WHERE ALL FUNCTIONS ARE THERE

while True:
    print("_______________________________________________________")
    print("_______________________________________________________")
    print("")
    print(" ******* STUDENT     MANAGEMENT     SYSTEM   ********* ")
    print("_______________________________________________________")
    print("_______________________________________________________")
    try:
        ask=int(input("ENTER SECURITY PIN: ")) 
        if ask==2008:
            print("ADMINISTRATION REQUEST GRANTED !!")
            print("")
            print("press:-")
            print("")
            print("1 for Adding students (NOTE:- This will delete all the previous records and will store from the stratch)")
            print("2 for Viewing all students")
            print("3 for Searching a student")
            print("4 for Updating data of the students")
            print("5 for Deleting a student")
            print("6 for exiting the system")
            print("7 for appending students")
            print("")
            ch=int(input("Enter your choice: "))
            if ch==1:
                add_stu()
            elif ch==2:
                view_stu()
            elif ch==3:
                search_stu()
            elif ch==4:
                update_stu()
            elif ch==5:
                delete_stu()
            elif ch==6:
                print("Exiting the system")
                break
            elif ch==7:
                app_stu()

            else:
                print("\nWrong Input Try Again !!\n")
                print("-----------------------------")
        else:
            print("\nWrong pin, Administration request denied!!\n")
            print("-----------------------------------------------")
    except ValueError:
        print("\nPLEASE USE NUMBERS !!\n")
