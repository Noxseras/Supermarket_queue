class Supermarket:
    def __init__(self):
        # Create two empty lists for the first and second cashier, in order to add the customer
        self.cashier1 = []
        self.cashier2 = []
        self.total_customers = ()
        self.customer = []  # assign each customer with the number of it's line
        self.wait_list = []  # if the lines are full, the customer will be add in this list
        self.shopping = []  # a list for the customers that go to shop again
        self.leaving = []  # a list for every customer that leaves, then remove them

    # Ask the user to give the total number of how customers.
    def customers_range(self):
        while True:  # create a loop to ensure that the users will enter only integers not letters nor float
            try:
                self.total_customers = int(input('How many customers are in total?: '))  # Range of customers
                if 0 < self.total_customers <= 20:  # Customers must be at least one and less than 20
                    print('{} customer(s) so far'.format(self.total_customers))
                    break
                # In case there are not any customers, exit the program
                elif self.total_customers == 0:
                    print('No customers! Ending the program')
                    exit()
                # in case the users enters 0 or a negative number
                elif self.total_customers < 0:
                    print('{} is not valid!Please enter at least 1 customer!'.format(self.total_customers))
                    continue
                else:
                    print('Please enter a total of customers below 20!')
                    continue
            except ValueError:  # if the users enters anything rather than int, prints a message and returns to the loop
                print('Please enter only numbers, not letters!')

    # Function to add all the customers in a list
    def register_customers(self):
        for i in range(self.total_customers):
            # Insert() instead of append()
            # because we want the first customer to exit the loop first (FIFO)
            self.customer.insert(0, i)

    # Function to add the customer to a cashier
    def add_to_line(self):
        for self.customer in range(self.total_customers):  # range for each customer
            print('You can always leave without shopping; if you would like so, just write "leave"')
            print('If you would like to go shopping again, you can simply type "shop" ')
            ask = str(input('Hello customer {}, which line you want?(choose 1 or 2): '.format(self.customer)))
            ask = ask.lower()
            # Add the customer to the cashier depending on where the customer wants.
            if ask == '1':
                # set a range to 5 for each cashier
                if len(self.cashier1) < 5:
                    self.cashier1.insert(0, self.customer)
                    print('Customer {} is now in cashier 1!'.format(self.customer))
                elif len(self.cashier1):
                    # set a big range, in order if the user insert anything incorrect, it makes a loop
                    for i in range(100000000):
                        checking = str(input('Cashier 1 is full! Would you like to wait or check for second cashier?'
                                             '(Please enter "check" or "wait"): '))
                        checking = checking.lower()  # Lower all the letters of what the user enters
                        # if wants to check for the other cashier and it is free, add the customer, else add to
                        # wait_list
                        if checking == 'check':
                            if len(self.cashier2) < 5:
                                self.cashier2.insert(0, self.customer)
                                print('Customer {} is waiting in line for the second cashier!'.format(self.customer))
                                break
                            else:
                                print('Cashier 2 is also full, you need to wait!')
                                self.wait_list.insert(0, self.customer)
                                break
                        elif checking == 'wait':
                            print('Customer {} is now waiting!'.format(self.customer))
                            self.wait_list.insert(0, self.customer)
                            break
                        else:
                            print('{} is not valid, please try again!'.format(checking))
                            continue
            elif ask == '2':
                # set a range to 5 for each cashier
                if len(self.cashier2) < 5:
                    self.cashier2.insert(0, self.customer)
                    print('Customer {} is now in cashier 2!'.format(self.customer))
                elif len(self.cashier2):
                    # set a big range, in order if the user insert anything incorrect, it makes a loop
                    for i in range(100000000):
                        checking = str(input('Cashier 2 is full! Would you like to wait or check for second cashier?'
                                             '(Please enter "check" or "wait"): '))
                        checking = checking.lower()  # Lower all the letters of what the user enters
                        # if wants to check for the other cashier and it is free, add the customer, else add to
                        # wait_list
                        if checking == 'check':
                            if len(self.cashier1) < 5:
                                self.cashier1.insert(0, self.customer)
                                print('Customer {} is waiting in line for the first cashier!'.format(self.customer))
                                break
                            else:
                                print('Cashier 1 is also full, you need to wait!')
                                self.wait_list.insert(0, self.customer)
                                break
                        elif checking == 'wait':  # If user enters "wait" insert the customer to wait list
                            print('Customer {} is now waiting!'.format(self.customer))
                            self.wait_list.insert(0, self.customer)
                            break
                        else:
                            print('{} is not valid, please try again!'.format(checking))
                            continue
            elif ask == 'shop':  # For the customers that want to shop again
                self.shopping.insert(0, self.customer)  # insert them to the shopping list
                print('Customer {} went shopping again!'.format(self.customer))

            elif ask == 'leave':  # for the customers that want to leave
                self.leaving.append(self.customer)  # Append to a list then remove them
                print('Have a nice one!')
            else:  # a loop to ensure that the user enters 1 or 2, if not repeat until the right input is inserted
                while not ask == '1' or not ask == '2' or not ask == 'shop' or not ask == 'leave':
                    print('If you would like to go shopping again, you can simply type "shop" ')
                    ask = str(input('What you entered is not correct! Enter number 1 for cashier 1 and 2 for cashier '
                                    '2: '))
                    ask = ask.lower()
                    # If the user's input is correct, insert them to a cashier
                    if ask == '1':  # If the user enters 1, break and go to the next customer
                        self.cashier1.insert(0, self.customer)
                        print('Customer {} is now in cashier 1!'.format(self.customer))
                        break
                    elif ask == '2':  # if the user enters 2, break and go to the next customer
                        self.cashier2.insert(0, self.customer)
                        print('Customer {} is now in cashier 2!'.format(self.customer))
                        break
                    elif ask == 'shop':
                        self.shopping.insert(0, self.customer)
                        print('Customer {} went shopping again!'.format(self.customer))
                        break
                    elif ask == 'leave':
                        self.leaving.append(self.customer)
                        print('Have a nice one!')
                    else:
                        continue

    def shoppers(self):  # A function for the customers that went to shop again
        if not self.shopping == []:
            for self.customer in range(len(self.shopping)):
                print('Customer {}, which line would you like to enter ?'.format(self.customer))
                asking = int(input('Enter here (1 or 2): '))
                if asking == 1:
                    self.cashier1.insert(0, self.customer)
                    self.shopping.pop()
                    break
                elif asking == 2:
                    self.cashier2.insert(0, self.customer)
                    self.shopping.pop()
                    break
                else:  # a loop to ensure that the user enters 1 or 2, if not repeat until the right input is inserted
                    while not asking == 1 or not asks == 2:
                        asking = int(
                            input('What you entered is not correct! Enter 1 for cashier 1 and 2 for cashier 2: '))
                        # If the user's input is correct, insert them to a cashier
                        if asking == '1':  # If the user enters 1, break and go to the next customer
                            self.cashier1.insert(0, self.customer)
                            print('Customer {} is now in cashier 1!'.format(self.customer))
                            break
                        elif asking == '2':  # if the user enters 2, break and go to the next customer
                            self.cashier2.insert(0, self.customer)
                            print('Customer {} is now in cashier 2!'.format(self.customer))
                            break
                        else:
                            return
        elif not self.shopping:  # if the list is empty, continue
            return
        else:
            return

    def remove_customer(self):  # Function for every customer that wants to leave without shopping
        self.leaving.clear()  # Delete every customer from the list

    def pop_customers(self):
        for i in range(len(self.cashier1)):
            self.cashier1.pop(-1)
        for i in range(len(self.cashier2)):
            self.cashier2.pop(-1)

    def add_again(self):  # function to add back to the line the customers who were waiting
        global asks  # make asks global for the while not below
        if not self.wait_list == []:  # check if there are customers waiting, if True, call add_to_line function
            for self.customer in range(len(self.wait_list)):
                print('Customer {}, which line would you like to enter ?'.format(self.customer))
                asks = int(input('Enter here (1 or 2): '))
                if asks == 1:
                    self.cashier1.insert(0, self.customer)
                    self.wait_list.pop()
                    break
                elif asks == 2:
                    self.cashier2.insert(0, self.customer)
                    self.wait_list.pop()
                    break
                else:  # a loop to ensure that the user enters 1 or 2, if not repeat until the right input is inserted
                    while not asks == 1 or not asks == 2:
                        asks = int(
                            input('What you entered is not correct! Enter 1 for cashier 1 and 2 for cashier 2: '))
                        # If the user's input is correct, insert them to a cashier
                        if asks == '1':  # If the user enters 1, break and go to the next customer
                            self.cashier1.insert(0, self.customer)
                            print('Customer {} is now in cashier 1!'.format(self.customer))
                            break
                        elif asks == '2':  # if the user enters 2, break and go to the next customer
                            self.cashier2.insert(0, self.customer)
                            print('Customer {} is now in cashier 2!'.format(self.customer))
                            break
                        else:
                            return
        elif not self.wait_list:
            return
        else:
            return


start = Supermarket()
start.customers_range()  # add the range of the customers function
start.register_customers()  # assign each customer with the number of the entrance
start.add_to_line()  # add each customer to a cashier
start.remove_customer()  # remove the customers that leave without shopping function
start.pop_customers()  # function to remove customers from both cashiers desk
start.add_again()   # for the customers that are waiting
start.shoppers()  # function for the customers who go for shopping again
