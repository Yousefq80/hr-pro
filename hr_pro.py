from sys import builtin_module_names
from unicodedata import name


class Employee:
    
    def __init__(self, name, age, sal, doj):
        self.name = name
        self.age = age
        self.sal=sal
        self.doj=doj

    def anualsal(self):
        return self.sal*12
    
    def showemp(self):
        print(f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}")
    def addemp(self):
        self.name=(input("Enter emp name:\t"))
        self.age = int(input("Enter age:\t"))
        self.sal = input("Enter salary:\t")
        self.jod = input("Enter working years:\t")
     
    def __str__(self):
        return f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}"
    
    
    ch = int(input("Enter your Choice "))  
   #Employee class here

class Manager(Employee):
    def __init__(self, name, age, sal, doj,bonus_per):
        super().__init__(name, age, sal, doj)
        self.bonus_per=bonus_per
        total=self.sal*(self.bonus_per/100)
    #Manager class here
    def getbonus(self):
        return self.sal * self.bonus
    def showmang(self):
        print(f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}bonus:,{self.getbonus}")
    def addmng(self):
       self.name=(input("Enter emp name:\t"))
       self.age =int(input("Enter age:\t"))
       self.sal = input("Enter salary:\t")
       self.jod = input("Enter working years:\t") 
    def __str__(self):
       return f"name:,{self.name}age:,{self.age}salary:,{self.sal}working year:,{self.doj}bonus:,{self.getbonus}"
    def menu(self):
        print("Welcome to Employee Management Record")
        print("Press ")
        print("1 to show all emp list")
        print("2 to show  manager")
        print("3 to Promote add emp")
        print("4 to add manager")
        print("5 to Exit")
        ch = int(input("Enter your Choice "))
        if ch == 1:
         self.showemp
        elif ch == 2:
         self.showmang
        elif ch == 3:
         self.addemp
        elif ch == 4:
         self.addmng
        elif ch == 5:
         exit(0)
        else:
          print("Invalid Choice")   
def main():

    # print("Welcome to Employee Management Record")
    # print("Press ")
    # print("1 to show all emp list")
    # print("2 to show  manager")
    # print("3 to Promote add emp")
    # print("4 to add manager")
    # print("5 to Exit")
    # if ch == 1:
    #     showemp()
    # elif ch == 2:
    #     Remove_Employ()
    # elif ch == 3:
    #     Promote_Employee()
    # elif ch == 4:
    #     Display_Employees()
    # elif ch == 5:
    #     exit(0)
    # else:
    #     print("Invalid Choice")
    
    # ch = int(input("Enter your Choice "))

	# main code here
 
if __name__ == '__main__':
	main()
