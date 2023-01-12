class library:
    def __init__(self, list, name):
        self.bookslist = list
        self.libraryname = name
        self.lenddict = {}

    def displaybook(self):
        print(f"We have following books in our library: {self.libraryname}")
        for book in self.bookslist:
            print(book)

    def lendbook(self,user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Library Lender database has been updated, You can take your book now.")
        else:
            print(f"The book is already used by {self.lenddict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)

if __name__ == '__main__':
    lib = library(["Python", "Machine Learning", "Big Data", "C++", "Artifical Inteligience", " "], "Vachanalay")

    while(True):
        print(f"Welcome to the {lib.libraryname} Library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option from number 1,2,3,4 ")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            lib.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to Lend:\n")
            user = input("Enter your name:\n")
            lib.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add:\n")
            lib.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return:\n")
            lib.returnbook(book)
            print(f"Thank You for returning {book} Book")

        else:
            print("Not a valid option kindly choose number from 1,2,3,4.")

        print("--------------------------")
        print("Press Q to Quit or C to Continue")
        user_choice2 = " "
        while(user_choice2!="C" and user_choice2!="Q" ):
            user_choice2 = input().capitalize()
            if user_choice2 == "Q":
                exit()
            elif user_choice2 == "C":
                continue






