import getpass
import sys
from Functions import*
print("**********************************************Welcome to Library Management System*********************************************")
print("*"*127)
def show():
    print("*"*63)
    print("1)  Add Student\n2)  Add Book\n3)  Add Faculty\n4)  Issue Book to Student\n5)  Issue Book to Faculty\n6)  Return Book from Student")
    print("7)  Return Book from Faculty\n8)  Search Book\n9)  Records of Student\n10) Records of Faculty\n11) Records of Book\n12) LogOut\n13) Exit")
    print("*"*63)
def search():
    print("Select the Search Option: ")
    print("-"*37)
    print("1. Search by ISBN\n2. Search by Author\n3. Search by Title")
    print("-"*37)
    se=int(input("Select the search Operation from 1 to 3:  "))
    if se==1:
        isb=input("Enter ISBN No:  ")
        search_book(1,isb)
    elif se==2:
        auth=input("Enter Author Name:  ").upper()
        search_book(2,auth)
    elif se==3:
        title=input("Enter Title of the Book:  ").upper()
        search_book(3,title)
    else:
        print("__________Invalid Input__________")

while True:
    print("Login: ")
    print("Admin Login   : Enter 1")
    print("Student Login : Enter 2")
    print("Faculty Login : Enter 3")
    print("Exit          : Enter 0")
    ch=int(input("Choose the Mode of Login: "))
    if ch==1:
        user_id=input("Enter Id: ")
        passw=getpass.getpass("Enter Password: ")
        if user_id=="admin" and passw=="admin":
            print("___________________Login Successful____________________")
            while True:
                show()
                opt=int(input("Enter the Choice from 1 to 13 to Perform :  "))
                if opt==1:
                    add_Student()
                elif opt==2:
                    add_book()
                elif opt==3:
                    add_faculty()
                elif opt==4:
                    issue_book_stud()
                elif opt==5:
                    issue_book_faculty()
                elif opt==6:
                    return_stud()
                elif opt==7:
                    return_faculty()
                elif opt==8:
                    search()
                elif opt==9:
                    print("1. Display Record of All Student")
                    print("2. Display Record of a Particular Student")
                    dis=int(input("Enter 1 or 2 to Display the Record Accordingly"))
                    if dis==1:
                        record_stud(1)
                    elif dis==2:
                        i_d=input("Enter Student ID:  ").upper()
                        record_stud(2,i_d)
                    else:
                        print("__________Invalid Input__________")
                elif opt==10:
                    print("1. Display Record of All Faculty")
                    print("2. Display Record of a Particular Faculty")
                    dis=int(input("Enter 1 or 2 to Display the Record Accordingly"))
                    if dis==1:
                        record_faculty(1)
                    elif dis==2:
                        i_d=input("Enter Faculty ID:  ").upper()
                        record_faculty(2,i_d)
                    else:
                        print("__________Invalid Input__________")
                elif opt==11:
                    record_book()
                elif opt==12:
                    print("Successfully Logged Out......")
                    print("*"*63)
                    break
                elif opt==13:
                    sys.exit("Exiting.........Please Wait....>>")
        else:
            print("-------------------Invalid Username or Password---------------")
    elif ch==2:
        i_d=input("Enter your Id : ").upper()
        t=record_stud(2,i_d)
        if t==True:
            temp=input("Do you want to see the available Books in Library(y/n): ")
            if temp=='y' or temp=="Y":
                print("1) Display all Books\n2) Search Book")
                get=int(input(" Press 1 or 2 Accordingly:  "))
                if (get==1):
                    record_book()
                elif get==2:
                    search()
                else:
                    print("__________Invalid Input___________")
    elif ch==3:
        i_d=(input("Enter your Id : ").upper())
        t=record_faculty(2,i_d)
        if t==True:
            temp=input("Do you want to see the available Books in Library(y/n): ")
            if temp=='y' or temp=="Y":
                print("1) Display all Books\n2) Search Book")
                get=int(input(" Press 1 or 2 Accordingly:  "))
                if (get==1):
                    record_book()
                elif get==2:
                    search()
                else:
                    print("__________Invalid Input___________")
    elif ch==0:
        print("Exiting...........Please Wait.....>>>")
        break
    else:
        print("__________Invalid Input__________")
        
    
    
    