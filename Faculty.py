class Faculty:
    def __init__(self):
        self.name=input("Enter Name\t\t: ").upper()
        self.id  =input("Enter ID\t\t: ").upper()
        self.book={}
    def __str__(self):
        return (f"Name\t\t: {self.name}\nID\t\t: {self.id}")