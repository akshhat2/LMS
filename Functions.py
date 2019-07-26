#2) Load Student:
import os,pickle
from Book import*
from Faculty import*
from Student import Student
import datetime
def add_Student():
    temp=int(input("Enter the No. of Students: "))
    l=[]
    for i in range (1,temp+1):
        print(f"\nEnter Details of Student {i}:")
        name=input('Enter Name\t\t: ').upper()
        while True:
            year=int(input("Enter Admission Year\t: "))
            if year<2020 and year>2000:
                break
            else:
                print("Invalid Input")
        print("Branch Code:\n1) Computer Science\t: CS\n2) Mechanical\t\t: ME\n3) Information Tech\t: IT\n4) Electronics\t\t: EC\n5) Electrical\t\t: EX\n6) Pharamacy\t\t: BP")
        branch=input("\nEnter Branch Code\t: ").upper()
        while True:
            adm=input("Enter Admission Number\t: ")
            if len(adm) <4 or len(adm)>4:
                print("Invalid Input(Must be only of 4 Digit)")
            else:
                break
        i_d="0187"+branch+str(year)[2:]+adm
#         Stud_list=load_student()
#         for _ in Stud_lis:
#             if _.i_d ==i_d:
#                 print("Student Already Exists")
#                 return
        l.append(Student(name,year,branch,adm,i_d))
    if os.path.isfile('Student.pkl'): #os.path.exist()
        Stud_list=load_student()
        for _ in Stud_list:
            if _.i_d ==i_d:
                print("Student Already Exists")
                return
        f1=open('Student.pkl','ab')
    else:
        f1=open('Student.pkl','wb')
    for _ in l:
        pickle.dump(_,f1)
    print("*****Data Succesfully Uploaded******")
    f1.close()
def load_student():
    lis=[]
    if os.path.isfile('Student.pkl'):
        with open('Student.pkl','rb') as f:
            while True:
                try:
                    lis.append(pickle.load(f))
                except EOFError:
                    break
    else:
        print("No Student Added")
    return lis
#3) Load Faculty
def load_faculty():
    lis=[]
    if os.path.isfile('Faculty.pkl'):
        with open ('Faculty.pkl','rb') as f:
            while True:
                try:
                    lis.append(pickle.load(f))
                except EOFError:
                    break
    return lis
def load_book():
    lis=[]
    with open ('Book.pkl','rb') as f:
        while True:
            try:
                lis.append(pickle.load(f))
            except EOFError:
                break
    return lis
def dump_Book(lis):
    for i in range (0,len(lis)):
        if i==0:
            with open('Book.pkl','wb') as f:
                pickle.dump(lis[i],f)
        else:
            with open('Book.pkl','ab') as f:
                pickle.dump(lis[i],f)
#4) Dump Student
def dump_Student(lis):
    for i in range (0,len(lis)):
        if i==0:
            with open('Student.pkl','wb') as f:
                pickle.dump(lis[i],f)
        else:
            with open('Student.pkl','ab') as f:
                pickle.dump(lis[i],f)
#         with open('Student.pkl','wb') as f:
#             pickle.dump(lis[0],f)
#         with open ('Student.pkl','ab') as f:
#             pickle.dump(lis[1:],f)
#5) Dump Faculty
def dump_Faculty(lis):
    for i in range (0,len(lis)):
        if i==0:
            with open('Faculty.pkl','wb') as f:
                pickle.dump(lis[i],f)
        else:
            with open('Faculty.pkl','ab') as f:
                pickle.dump(lis[i],f)
#         with open('Faculty.pkl','wb') as f:
#             pickle.dump(lis[0],f)
#         with open ('Faculty.pkl','ab') as f:
#             pickle.dump(lis[1:],f)
#6) Add Book
def add_book():
    temp=int(input("Enter the No. of Books: "))
    l=[]
    for i in range (1,temp+1):
        print(f"\nEnter Details of Book {i}:")
        l.append(Book())
    if os.path.isfile('Book.pkl'): #os.path.exist()
        f1=open('Book.pkl','ab')
    else:
        f1=open('Book.pkl','wb')
    for _ in l:
        pickle.dump(_,f1)
    print("*****Data Succesfully Uploaded******")
    f1.close()
#7) Add Faculty
def add_faculty():
    temp=int(input("Enter the No. of Faculties: "))
    l=[]
    for i in range (1,temp+1):
        print(f"\nEnter Details of Faculty {i}:")
        l.append(Faculty())
    if os.path.isfile('Faculty.pkl'): #os.path.exist()
        f1=open('Faculty.pkl','ab')
    else:
        f1=open('Faculty.pkl','wb')
    for _ in l:
        pickle.dump(_,f1)
    print("*****Data Succesfully Uploaded******")
    f1.close()
#8) Check Student ID
def check_stud_id(i_d,lis):
#     lis=load_student()
    for _ in lis:
#         flag=0
        if temp==_.i_d:
            return True
    return False
#9) Check  Student Limit
def check_stud_limit(temp,lis):
    pass
#10) Check ISBN NO
def check_isbn (isb,lis):
    for _ in lis:
        if _.isbn==isb:
            return True
    return False
#8) Issue Book to Student
def issue_book_stud():
    temp=input("Enter the Student ID: ").upper()
    lis=load_student()
    for i in range (0,len(lis)):
        flag=0
        t=lis[i]
        if temp==t.i_d:
            flag=1
            if len(lis[i].book)>5:
                print("Book Limit Reached")
            else:
                isb=input("Enter the ISBN Number: ")
                isb_list=load_book()
                if (check_isbn(isb,isb_list)):
                    if isb in lis[i].book:
                        print("Book Already Issued")
                        break
                    else:
                        for _ in range(0,len(isb_list)):
                            if (isb_list[_].isbn==isb):
                                if (isb_list[_].copies==0):
                                    print("All Copies Issued")
                                else:
                                    t=datetime.date.today()
                                    lis[i].book[isb]=t
                                    print(f"Book with {isb} ISBN Succesfully Issued to Student {lis[i].i_d}")
                                    isb_list[_].copies-=1
                                    dump_Book(isb_list)
                                    break
                        dump_Student(lis)
                        break
                else:
                    print(f"Book with {isb} ISBN Not Present")
    if flag==0:
        print("Student Not Found")
#     return False
#     if(!check_stud_id(temp,lis)):
#         print("Student Not Found")
#         return
#     if len(book)>5:
#         print("Book Limit Reached")
#         return
#12) Issue Book to Faculty
def issue_book_faculty():
    temp=input("Enter the Faculty ID: ").upper()
    lis=load_faculty()
    flag=0
    for i in range (0,len(lis)):
        if temp==lis[i].id:
            flag=1
            isb=input("Enter the ISBN Number: ")
            isb_list=load_book()
            if (check_isbn(isb,isb_list)):
                for _ in range(0,len(isb_list)):
                    if (isb_list[_].isbn==isb):
                        copy=int(input("Enter the No. of Copies: "))
                        if (isb_list[_].copies<copy):
                            print(f"{isb_list[_].copies} Copies Available")
                            break
                        else:
                            lis[i].book[isb]=copy
                            isb_list[_].copies-=copy
                            print(f"{copy} Copies of Book with {isb} ISBN Succesfully Issued to Faculty {lis[i].id}")
                            dump_Book(isb_list)
                            break
                dump_Faculty(lis)
                break
            else:
                print(f"Book with {isb} ISBN Not Present")
    if flag==0:
        print("Faculty Not Found")
### Caluculate Fine
def calc_fine(obj,isb):
    d2=datetime.date.today()
    d1=obj.book[isb]
    days=(d2-d1).days
    if (days>20):
        days-=20
        return days*2
    return 0
#13) Return Book (Student)
def return_stud():
    temp=input("Enter the Student ID: ").upper()
    lis=load_student()
    flag=0
    for i in range (0,len(lis)):
        if temp==lis[i].i_d:
            flag=1
            isb=input("Enter the ISBN: ")
            if isb in lis[i].book:
                fine=calc_fine(lis[i],isb)
                if (fine!=0):
                    print(f"Student with ID {lis[i].i_d} have been Charged by Rs. {fine}")
                try:
                    del lis[i].book[isb]
                except KeyError:
                    pass
#                 lis[i].book.pop('isb')
                dump_Student(lis)
                print("************Book Returned*************")
                book_list=load_book()
                for _ in range(0,len(book_list)):
                    if book_list[_].isbn==isb:
                        book_list[_].copies+=1
                        break
                dump_Book(book_list)
                break
            else:
                print(f"Book with {isb} ISBN Not Issued to thi Student with ID {lis[i].i_d}")
                break
    if flag==0:
        print(f"Student with ID {temp} Not Present")
### Caluclate Fine for Faculty
#$$##
# def calc_fine_faculty(obj,isb):
#     d2=datetime.date.today()
#     d1=obj.book[isb]
#     days=(d2-d1).days
#     if (days>45):
#         days-=45
#         return days*2
#     return 0
#14) Return Book by Faculty
def return_faculty():
    temp=input("Enter the Faculty ID: ").upper()
    lis=load_faculty()
    flag=0
    for i in range (0,len(lis)):
        if temp==lis[i].id:
            flag=1
            isb=input("Enter the ISBN: ")
            if isb in lis[i].book:
                copy=lis[i].book[isb]
                no=int(input("Enter the No. of Copies to Return"))
                if (no==copy):
                    print("***********Book Successfully Reuturned***************")
                    try:
                        del lis[i].book[isb]
                    except KeyError:
                        pass
#                 lis[i].book.pop('isb',None)
                else:
                    lis[i].book[isb]-=no
                    print(f"{no} Copies with {isb} ISBN Successfully Returned, {copy-no} Copies Left with Faculty Id: {lis[i].id}")
                dump_Faculty(lis)
                book_list=load_book()
                for _ in range(0,len(book_list)):
                    if book_list[_].isbn==isb:
                        book_list[_].copies+=copy
                        break
                dump_Book(book_list)
                break
            else:
                print(f"Book with {isb} ISBN Not Issued to this Faculty with ID {lis[i].id}")
                break
    if flag==0:
        print(f"Faculty with ID {temp} Not Present")
#15) Search Book
def search_book(mode,data):
    book_list=load_book()
    flag=0
    if mode==1:
        for _ in book_list:
            if _.isbn==data:
                flag=1
                print(_)
                break
    elif mode==2:
        for _ in book_list:
            if _.author==data:
                flag=1
                print(_)
    else:
        for _ in book_list:
            if _.title==data:
                flag=1
                print(_)
    if flag==0:
        print("*****Book Not Found*******")
#16) Print Student Records
def record_stud(mode,data=None):
    stud_list=load_student()
    if mode==1:
        i=1
        for _ in stud_list:
            print(f"Details of Student {i}: ")
            print(_)
            print("Book Issued with Date of Issuing")
            print(_.book)
            i+=1
    else:
        flag=0
        for _ in stud_list:
            if _.i_d==data:
                flag=1
                print(_)
                print("Book Issued with Date of Issuing")
                print(_.book)
                return True
                break
        if flag==0:
            print(f"Student with Id {data} does not Exist")
#17) Print Faculty Records
def record_faculty(mode,data=None):
    faculty_list=load_faculty()
    if mode==1:
        i=1
        for _ in faculty_list:
            print(f"Details of Faculty {i}: ")
            print(_)
            print("Book Issued with No. of Copies")
            print(_.book)
            i+=1
    else:
        flag=0
        for _ in faculty_list:
            if _.id==data:
                flag=1
                print(_)
                print("Book Issued with No. of Copies")
                print(_.book)
                return True
                break
        if flag==0:
            print(f"Faculty with Id {data} does not Exist")
            return False
def record_book():
    book_list=load_book()
    i=1
    for _ in book_list:
        print(f"Details of Book {i}: ")
        i+=1
        print(_)