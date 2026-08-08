# Library Management System

lib_dict = {
    "python": 20,
    "sql": 2,
    "pandas": 5, 
    }

class lms:
    # lib_dict = {
    # "python": 20,
    # "sql": 2,
    # "pandas": 5, 
    # }

    def __init__(self, lib_stock, name, mobile, email, stud_id, books_record = {} ):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.stud_id = stud_id 
        self.lib_stock = lib_stock
        self.books_record = books_record

    
    def issue_book(self, book_name):
        if book_name in self.lib_stock and self.lib_stock[book_name] > 0:
            self.lib_stock[book_name] -= 1
            self.books_record["issued"] = [(book_name, self.issue_count)]
            return f"Book issued: {book_name}"
        
        elif book_name == 0:
            return f"Book Stock Empty, Try issuing later: {book_name}"
        
        else:
            return f"{book_name} unavailable"
        
    def book_return(self, book_name):
        if book_name in self.lib_stock:
            self.lib_stock[book_name] += 1
            self.books_record["returned"] = [book_name]
            return f"{book_name} Book returned Successfully"
        else:
            return f"{book_name} Book doesn't belong to this library"
        
    def list_books(self):
        return self.lib_stock
    
    def my_details(self):
        return {
            "Student_name ": self.name,
            "Mobile ": self.mobile,
            "Email ": self.email,
            "ID": self.stud_id,
            "Books_recored": self.books_record
        }



nandu = lms(lib_dict, "Nandu", 8873948653, "myemail@mail.com", 1222)
print(nandu.my_details())
books_available = nandu.list_books()
print(books_available)
print(nandu.issue_book("pandas"))
print(nandu.issue_book("pandas"))
print(nandu.issue_book("pandas"))
print(nandu.issue_book("pandas"))
print(nandu.issue_book("pandas"))
print(nandu.issue_book("python"))
print(nandu.issue_book("pandas"))
print(nandu.issue_book("python"))
print(nandu.book_return("pandas"))
print(nandu.list_books())

print(nandu.my_details())
