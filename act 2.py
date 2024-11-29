class libraRY:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.bookdict={}

    def display(self):
        print("we have following books")
        for books in self.booklist:
            print(books)