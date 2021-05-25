class OrderHelper:

    def __init__(self):
        self.order_active = True
        self.order_contents = []


    def show_menu(self):
        #print out the available items
        for item in menu.values():
            print(item)

    def add_item(self):
        #add an item to the order, after showing the menu
        print("Here's what's on the menu")

        show_menu()





    def take_order(self):
        #this function will add or remove items to an order until the customer states they are happy with their order, or abort the order process
        while self.order_active:
            if self.order_contents == False:
                print("You are currently ordering nothing. Type 'add' to add items, or 'exit' to exit: ")
            else:
                print("Here is your current order:")
                for item in order:
                    print(item)
                next_step = input("Type 'add' to add an item, or 'remove' to remove an item. To place your order, type 'done', or 'exit' to quit the order process: ")

                #Have now taken input. Next is to take appropriate action with list.
                #if done, set order_active to False and print out order.
                #if add, run add_item
                #if remove, run remove_item
                #if exit, empty list and quit order process



#Set up a menu for usage
menu = {
    1 : "Burger",
    2 : "Milkshake",
    3 : "Fries",
    4 : "Sweet Potato Fries",
    5 : "Beer",
}

my_order = OrderHelper()
my_order.show_menu()