import csv

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
        
    def storedDataPermanently(self):
        with open("storedData.csv", 'a', newline='') as csv_writer:
            writer = csv.writer(csv_writer)
            writer.writerow(self.books)
            print("Data Stored SuccessFully !!")
    
    def displayPermanentlyStoredData(self):
        with open("storedData.csv", 'r') as csv_reader:
            self.readData = csv.reader(csv_reader)
            for self.rows in self.readData:
                print(self.rows)


phy_lib = library()

phy_lib.addingBook()
phy_lib.storedDataPermanently()
# phy_lib.listingBooks()
phy_lib.displayPermanentlyStoredData()
phy_lib.remBooks()
phy_lib.storedDataPermanently()
look = input("Do You Want to Look at the Current Stored Data {Answer in YES or NO only} : ")
if look == "YES":
    phy_lib.displayPermanentlyStoredData()
else:
    print("Thank you for using Our Program !!")
    quit()


#Below Codes are just Test Codes !!

# while True:
#     sel1 = input("Do you want to remove some Books {Answer in YES or NO}: ")
#     if(sel1 == "YES"):
#         phy_lib.remBooks()
#         Flag = Flag + 1
#     else:
#         print("SURE !")
#         break
# phy_lib.listingBooks()
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