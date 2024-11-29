
class employee:
    #construtor
    def __init__(self,name):
        self.name=name

    #destructor
    def __del__(self):
        print(" destructor called. object deleted ")

emp1=employee("zoha")
print(emp1.name, " is passionate about coding")
del emp1

