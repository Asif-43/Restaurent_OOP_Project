from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant

def main():
    #add pizza
    pizza_1 = Pizza('chicken Pizza', 600, 'Large', ['chicken', 'Mushroom', 'Onion', 'Cheese'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Vegetable Pizza', 400, 'Large', ['Vegetables', 'Onion', 'Mushroom', 'Cheese'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Mixed Pizza', 700, 'Large', ['chicken', 'Vegetables', 'Onion', 'Mushroom', 'Cheese'])
    menu.add_menu_item('pizza', pizza_3)

    #add burger
    burger_1 = Burger('Naga Burger', 350, 'chicken', ['bread', 'chilli'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Mixed Burger', 550, 'chicken', ['bread', 'chilli', 'Vegetables'])
    menu.add_menu_item('burger', burger_2)

    #add drinks
    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha', 150, False)
    menu.add_menu_item('drinks', coffee)

    #show Menu
    menu.show_menu()
    
    
    Chilis = Restaurant
    

#call main function
if __name__ == '__main__':
    main()
    



