class libraRY:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.bookdict={}

    def display(self):
        print("we have following books")
        for books in self.booklist:
            print(books)

    def lendbook(self,user,book):
        if book not in self.bookdict:
         self.bookdict.update({book:user})
         print("you can take the book")
        else:
          print("this is already lended to ",self.bookdict[book])
    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added")
        
    def returnbook(self,book):
        self.bookdict.pop(book)
