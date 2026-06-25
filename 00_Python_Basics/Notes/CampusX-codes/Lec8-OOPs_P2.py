    # A user can create a 2D coordinates - x-axis and y-axis
    # 2d coordinate point - (x,y)
    # origin point - (0,0)
    # A user can check if the point lies on a given line - ax+by+c or not
    # calculate distance btwn 2 points
    # calculate distance btwn a point and a line
class Coordinate :
    def __init__(self,x,y):
        self.x_coord = x
        self.y_coord = y

    def __str__(self):
        return f'({self.x_coord},{self.y_coord})'

    def dist_2pts(self,other):
        dist = ((self.x_coord - other.x_coord)**2 + (self.y_coord - other.y_coord)**2)**0.5
        return dist
    
    def dist_origin(self):
        origin = Coordinate(0,0)
        return self.dist_2pts(origin)
    
    def pt_on_line(self,line):
        if line.A*self.x_coord + line.B*self.y_coord + line.C == 0:
            return True
        else :
            return False
    

class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return f'{self.A}x + {self.B}y + {self.C} = 0'
    
    def pt_on_line(line,point):
        if line.A*point.x_coord + line.B*point.y_coord + line.C == 0:
            return True
        else:
            return False
    
    def dist_line_pt(line,point):
        if line.pt_on_line(point):
            dist = 0
        else :
            dist = abs(line.A*point.x_coord + line.B*point.y_coord + line.C)/(line.A**2 + line.B**2)**0.5
        return dist
    

# p1 = Coordinate(1,10)
# l1 = Line(1,1,-2)

# print(p1)
# print(l1)

# print(l1.dist_line_pt(p1))


class Person:
    def __init__(self,name,country) :
        self.name = name
        self.country = country
    
    def greet(self):
        if self.country == 'india':
            print('Namaste,',self.name)
        else:
            print('Hello,',self.name)

P1 = Person('prasham','india')
# P1.greet()
# print(P1.name)

# P1.gender = 'male'
# print(P1.gender)
# P2 = Person('prasham2','pakistan')
# print(P2.gender)
def main1():
    p1 = Person('Prasham','USA')
    p2 = p1 

    def obj(person):
        person.name = 'Jp'
        print(id(person))
        return person

    p3 = obj(p2)

    print(id(p1))
    print(id(p2))
    print(id(p3))

    print(p1.name)
    print(p2.name)
    print(p3.name)
# All have the same ids and changes are reflected in all of them,
# since all are referring to the same object 

# main1()

# ENCAPSULATION

class Atm:
    # __init__(self) -> special function called -> 
    # Constructor -> it executes by default whenever 
    # an object is created

    __counter = 1 # static variable

    def __init__(self): # self parameter replaced by the object created 
         # initially when obj is created , it will have 
         # following data with default values - 
        # print(id(self))
        self.pin = ''
        self.__balance = 0
        # self.menu() 
        # whenever an object is created , 
        # the menu function will be called as it is called 
        # from within the constructor
        self.cid = Atm.__counter
        Atm.__counter += 1
    
    # this is a utility function
    @staticmethod
    def get_counter():
        return Atm.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        self.__balance = new_value


    def menu(self):
        menu = input('''
Hi how can I help you ?
1. Press 1 to set Pin
2. Press 2 to change Pin
3. Press 3 to check Balance
4. Press 4 to withdraw money
5. Press 5 to exit
        ''')
        if menu == '1':
            #create pin
            self.create_pin()
        elif menu == '2':
            #change pin
            self.change_pin()
        elif menu == '3':
            # check balance
            self.check_balance()
        elif menu == '4':
            #withdraw
            self.withdraw()
        else:
            #exit
            print("Thank you")
            exit()

    def create_pin(self):
        set_pin = input("Enter your pin: ")
        self.pin = set_pin

        bal = int(input("Enter your balance: "))
        self.__balance = bal

        print("Pin Created Successfully")
        # self.menu()
    
    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin :
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin Changed Successfully")
            self.menu()
        else :
            print("Wrong Pin")
            # self.menu()

    def check_balance(self):
        pin = input("Enter your pin: ")
        if pin == self.pin :
            print("Current Balance :",self.__balance)
        else:
            print('Wrong Pin')
        # self.menu()
    
    def withdraw(self):
        pin = input("Enter your pin: ")
        if pin == self.pin :
            print("Current Balance :",self.__balance)
            amount = int(input("Enter Amount you want to withdraw: "))
            if amount <= self.__balance :
                self.__balance -= amount
                print("Withdraw Successfull. Current Balance:",self.__balance)
            else:
                print("Not Enough Balance")
        else:
            print('Wrong Pin')
        # self.menu()


# obj = Atm()
# obj.create_pin()
# obj._Atm__balance = 'hehehe'

# obj.withdraw()


# p1 = Person('Prasham','IN')
# p2 = Person('PJ','PK')

# L = {p1,p2}

# for i in L:
#     print(i.name,i.country)

c1 = Atm()
print(c1.cid)
c2 = Atm()
print(c2.cid)
c3 = Atm()
print(c3.cid)

# print(Atm.counter)
Atm.counter = 'some value'
c4 = Atm()
c4.cid = Atm.counter 
print(c4.cid)
