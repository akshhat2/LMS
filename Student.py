# Stud_List =[]
class Student:
    def __init__(self,name,year,branch,adm,i_d):
#         self.name=input('Enter Name\t\t: ').upper()
#         while True:
#             self.year=int(input("Enter Admission Year\t: "))
#             if self.year<2020 and self.year>2000:
#                 break
#             else:
#                 print("Invalid Input")
#         print("Branch Code:\n1) Computer Science\t: CS\n2) Mechanical\t\t: ME\n3) Information Tech\t: IT\n4) Electronics\t\t: EC\n5) Electrical\t\t: EX\n6) Pharamacy\t\t: BP")
#         self.branch=input("\nEnter Branch Code\t: ")
#         while True:
#             self.adm=input("Enter Admission Number\t: ")
#             if len(self.adm) <4 or len(self.adm)>4:
#                 print("Invalid Input(Must be only of 4 Digit")
#             else:
#                 break
#         self.id="0187"+self.branch+str(self.year)[2:]+self.adm
        self.name=name
        self.year=year
        self.branch=branch
        self.adm=adm
        self.i_d=i_d
        self.book={}
#         Stud_List.append(self.i_d)
        print("Student Id : ",self.i_d)
#obj=Student()
    def __str__(self):
        return(f"Name\t\t: {self.name}\nID\t\t: {self.i_d}\nYear\t\t: {self.year}\nBranch\t\t: {self.branch}")