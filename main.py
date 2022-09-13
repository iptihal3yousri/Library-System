# borrow book   --->   1
# return book   --->   2
# search book   --->   3
# add book      --->   4
# remove book   --->   5
# display books --->   6

# ---------- library class ----------
class library:

    def __init__(self, list_title, list_author, list_number_of_copies_borrowed, list_number_of_copies_available, list_of_total_copies):
        self.list_title = list_title
        self.list_author = list_author
        self.list_number_of_copies_borrowed = list_number_of_copies_borrowed
        self.list_number_of_copies_available = list_number_of_copies_available
        self.list_of_total_copies = list_of_total_copies
        self.check = False
        self.ind = -1

    def borrow_book(self, book):
        self.search_book(book)
        if self.ind == -1:
            print(f"The {book} book is not in our library.")
        else:
            if self.list_number_of_copies_borrowed[self.ind] == self.list_of_total_copies[self.ind]:
                print(f"All copies of {book} book are already borrowed.")
            else:
                self.list_number_of_copies_borrowed[self.ind] += 1
                self.list_number_of_copies_available[self.ind] -= 1
                print(
                    f"now you borrowed the the {book} copy number : {self.list_number_of_copies_borrowed[self.ind]}")
        print("\n" + "-" * 50 + "\n")
        self.check = False
        self.ind = -1

    def return_book(self, book):
        self.search_book(book)
        if self.ind == -1:
            print(f"The {book} book is not in our library, you may borrow this book from another library.")
        else:
            if self.list_number_of_copies_borrowed[self.ind] == 0:
                print(f"The {book} book is not borrowed from our library, you may borrow this book from another library.")
            else:
                self.list_number_of_copies_borrowed[self.ind] -= 1
                self.list_number_of_copies_available[self.ind] += 1
                print(f"the {book} book is returned successfully.")
        print("\n" + "-" * 50 + "\n")
        self.check = False
        self.ind = -1


    def search_book(self, book_name):
        for i, book in enumerate(self.list_title):
            if book == book_name:
                self.check = True
                self.ind = i
                break

    def search_book_1(self, book):
        self.search_book(book)
        if self.check == True:
            print("the book founded, and here is the book information.")
            print(f"""the book name : {self.list_title[self.ind]}
the book author : {self.list_author[self.ind]}
number of copies borrowed : {self.list_number_of_copies_borrowed[self.ind]}
number of copies available : {self.list_number_of_copies_available[self.ind]}
number of total copies : {self.list_of_total_copies[self.ind]}""")
        else:
            print(f"the {book} book is not in our library.")
        print("\n" + "-" * 50 + "\n")
        self.check = False
        self.ind = -1

    def remove_book(self, book):
        self.search_book(book)
        if self.ind == -1:
            print(f"The {book} book is not in our library.")
        else:
            print(f"the {book} book is deleted successfully.")
            self.list_title.pop(self.ind)
            self.list_author.pop(self.ind)
            self.list_number_of_copies_borrowed.pop(self.ind)
            self.list_number_of_copies_available.pop(self.ind)
            self.list_of_total_copies.pop(self.ind)
        print("\n" + "-" * 50 + "\n")
        self.check = False
        self.ind = -1




# ---------- some functions ----------
def add_book(list_title, list_author, list_num_borrowed, list_num_available, list_num_total):
    num = int(input("Enter How Many Books You Want To Add : "))
    for i in range(0, num):
        title = input("Enter The Book Title : ")
        author = input("Enter The Book Author : ")
        num_borrowed_copies = int(input("Enter The Number of borrowed Copies : "))
        num_available_copies = int(input("Enter The Number of available Copies : "))
        print("\n" + "-" * 50 + "\n")
        list_title.append(title)
        list_author.append(author)
        list_num_borrowed.append(num_borrowed_copies)
        list_num_available.append(num_available_copies)
        list_num_total.append((num_borrowed_copies + num_available_copies))
    print("books are added successfully.")
    print("if you want to display the books enter '1' otherwise enter '0'.")
    n = int(input("enter your choice : "))
    if(n == 1):
        display(list_title, list_author, list_num_borrowed, list_num_available, list_num_total)

def display(list_title, list_author, list_num_borrowed, list_num_available, list_num_total):
    for i in range(0, len(list_title)):
       print(f"book number {i+1} name : {list_title[i]},    author : {list_author[i]},    number of copies borrowed : {list_num_borrowed[i]},    number of copies available : {list_num_available[i]},    number of total copies : {list_num_total[i]}.")
    print("\n" + "-" * 50 + "\n")




# ---------- Main ----------
l_title = ["python", "java", "c++", "robotics", "php"]
l_author = ["iptihal", "osama", "nadin", "mariam", "marwa"]
l_num_borrowed = [0, 2, 5, 9, 4]
l_num_available = [3, 3, 1, 0, 2]
l_num_total = [3, 5, 6, 9, 6]
obj = library(l_title, l_author, l_num_borrowed, l_num_available, l_num_total)
b = True
while b:
    print("---Main List---\n1- Borrow Book.\n2- Return Book.\n3- Search Book.\n4- Add Book.\n5- Remove Book.\n6- Display Books")
    a = int(input("Enter your choice : "))
    if a == 1:
        requested_book = input("enter the book name you want to borrow : ")
        obj.borrow_book(requested_book)
    elif a == 2:
        requested_book = input("enter the book name you want to return : ")
        obj.return_book(requested_book)
    elif a == 3:
        requested_book = input("enter the book name you want to search for : ")
        obj.search_book_1(requested_book)
    elif a == 4:
        add_book(l_title, l_author, l_num_borrowed, l_num_available, l_num_total)
    elif a == 5:
        requested_book = input("enter the book name you want to remove : ")
        obj.remove_book(requested_book)
    elif a == 6:
        display(l_title, l_author, l_num_borrowed, l_num_available, l_num_total)
    else:
        print("Not a valid input!")
    q = input("if you want to make another operation enter 'yes' otherwise enter 'no' : ")
    if q.lower() == 'yes':
        b = True
    else:
        b = False    
