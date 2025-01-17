from abc import ABC, abstractclassmethod
class User(ABC):
    def __init__(self, name, phone, email, address)-> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name,phone, email, address, money)->None:
        self.wallet = money
        self.__order = None
        super().__init__(name, phone, email, address)
        
    @property()
    def order(self):
        return self.__order

    @order.setter
    def order(self,order):
        self.__order = order
        
    def place_order(self,order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')

    def eat_food(self, order):
        print(f'{self.name} item food {order.items}')
        
    def pay_for_order(self, amount):
        # TODO: submit the money to manager
        pass
        
    def give_tips(self, tips_amount):
        pass


    def write_review(self, stars):
        pass 
   


class Employee(User):
    def __init__(self, name,phone, email, address, salary, staring_date, department)->None:
        super().__init__(name)
        self.salary = salary
        self.due = salary
        self.staring_date = staring_date
        self.department = department
        
    def receieve_salary(self):
        self.due = 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, staring_date, department, cooking_item)-> None:
        super().__init__(name, phone, email, address, salary, staring_date, department)
        self.cooking_item = cooking_item
        
        
class Server(Employee):
    def __init__(self, name, phone, email, address, salary, staring_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, staring_date, department)
        
        
    def take_order(self, order):
        pass
    
    def transfer_order(self, order):
        pass
    
    def serve_food(self, order):
        pass
    
    def receieve_tips(self, amount):
        self.tips_earning += amount
        

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, staring_date, department) ->None:
        super().__init__(name, phone, email, address, salary, staring_date, department)
        