'''
When a library class with no_of_books and books as two instances variables. Write a program to create a library from the library class
and show how you can print all books, add a book and get the number of books using different methods. Show that your program does not
persist the books after the program is stopped.

library -> class
    var books -> list
    var no_of_books -> integer

    method to check -> no_of_books == len_of_books


'''

class library:
    def __init__(self):
        self.books = [] # <- NULLA list
        self.no_of_books = 0
        self.lengthOfBooks = None
        self.flag = 0


    def addingBook(self):
        while True:
            self.selection = input("Do you Want to Add Some Book to this library for yes type `YES` for no type `NO` : ")
            if (self.selection == "YES"):
                self.bookName = input("Enter the Name of Book : ")
                self.books.append(self.bookName)
                self.no_of_books = self.no_of_books + 1
            if(self.selection == "NO"):
                print("Thank you for Adding Books in this Library")
                break
            # else:
            #     print("You Didn't Entered the Correct Option use `YES` for yes and `NO` for no.")
            #     quit()
        self.lengthOfBooks = len(self.books)


    def check(self, val):  # for me, not for public use
        self.no_of_books = self.no_of_books - val
        if(self.no_of_books == self.lengthOfBooks):
            print("Everthing is Fine in the library.")
            print("Counter's Count : ",self.no_of_books)
            print("List's Count : ",self.lengthOfBooks)
        else:
            print("Number of Books is not Equal to Legnth of Books")

    def remBooks(self):
        while True:
            selection = input("Do You Want to Remove Some Books {Answer in YES or NO Only}: ")
            if selection == "YES":
                bookSelection = input("Enter the Name of Book You Want to Remove : ")
                self.books.remove(bookSelection)
                self.lengthOfBooks = len(self.books)
                self.flag += 1
            else:
                print("SURE !")
                break
    
    def listingBooks(self):
        for i in range(self.lengthOfBooks):
            print(self.books[i])


phy_lib = library()
Flag = 0

phy_lib.addingBook()
phy_lib.listingBooks()
phy_lib.remBooks()
# while True:
#     sel1 = input("Do you want to remove some Books {Answer in YES or NO}: ")
#     if(sel1 == "YES"):
#         phy_lib.remBooks()
#         Flag = Flag + 1
#     else:
#         print("SURE !")
#         break
phy_lib.listingBooks()
# phy_lib.check(phy_lib.flag)



# lib = []
# data = []
# counter = 0
# while True:
#     storeData = input("Do you want to Create a library if yes type `YES` if no type `NO` :  ")
#     if(storeData == "YES"):
#         lib.append(library())
#         lib[counter].
#         counter = counter + 1
#     if (storeData == "NO"):
#         quit()


# MORE WORKING ON THIS PROJECT...