class Book:
    def __init__(self):
        self.title=input("Enter Title\t\t: ").upper()
        self.isbn =input("Enter ISBN NO\t\t: ")
        self.author=input("Enter Author Name\t: ").upper()
        self.copies=int(input("Enter No of Copies\t: "))
        print("\n*****************Data Uploaded Successfully********************\n")
    def __str__(self):
        return (f"\n******Book Details*******\nTile\t\t: {self.title}\nISBN\t\t: {self.isbn}\nAuthor\t\t: {self.author}\nCopies\t\t: {self.copies}\n")
     