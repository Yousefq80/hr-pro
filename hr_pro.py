


class Employee:
    
    def __init__(self, name, age, sal, doj):
        self.name = name
        self.age = age
        self.sal=sal
        self.doj=doj

    def anualsal(self):
        return self.sal*12
    
    def showemp(self):
        print(f"name:,{self.name}/age:,{self.age}/:salary:,{self.sal}/working year:,{self.doj}")
    def addemp(self):
        self.name=(input("Enter emp name:\t"))
        self.age = int(input("Enter age:\t"))
        self.sal = input("Enter salary:\t")
        self.doj = input("Enter working years:\t")
     
    def __str__(self):
        return f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}"
    
    
    
   #Employee class here

class Manager(Employee):
    def __init__(self, name, age, sal, doj):
        super().__init__(name, age, sal, doj)
        
        
    #Manager class here
    def getbonus(self):
        return self.sal * (20/100)
    def showmang(self):
        print(f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}bonus:,{self.getbonus}")
    def addmng(self):
       self.name=(input("Enter emp name:\t"))
       self.age =int(input("Enter age:\t"))
       self.sal = input("Enter salary:\t")
       self.doj = input("Enter working years:\t") 
    def __str__(self):
       return f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}bonus:,{self.getbonus}"
    def menu(self):
        print("Welcome to Employee Management Record")
        print("Press ")
        print("1 to show all emp list")
        print("2 to show  manager")
        print("3 to add emp")
        print("4 to add manager")
        print("5 to Exit")
        ch = int(input("Enter your Choice "))
        if ch == 1:
         self.showemp()
        elif ch == 2:
         self.showmang()
        elif ch == 3:
         self.addemp()
        elif ch == 4:
         self.addmng()
        elif ch == 5:
         exit(0)
        else:
          print("Invalid Choice")   
def main():

 emp1=Employee("yousef",37,2000,17)
 emp2=Employee("naif",20,1000,12)
 ma=Manager("Rashed",50,4000,25)
 ma.menu()

#  emp1.addemp()
#  emp2.addemp()
#  ma.addmng()
 
     
     
     
if __name__ == '__main__':
	main()
