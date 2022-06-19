
### Assignment_Warehouse_APP.py
# MIT License
# 
# Copyright (c) 2022 Matteo Giardini
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Class - Create 1 base class for generic stock
class AppleStock:
    #total_stock = 0 # Class attributed, not depending on instance

    def __init__(self, amount = int):
        ''' Initialization function for AppleStock class'''
        self.amount = amount

    def add_stock(self, x = int):
        ''' Function that adds x amount of stock '''
        self.amount += x

    def remove_stock(self, y = int):
        ''' Function that removes y amount of stock, 
        if y is greater than the stock available, all stock is removed'''
        if y > self.amount:
            self.amount = 0
            return "You cannot remove so much stock, only {} products have been removed.".format(y)
        else:
            self.amount -= y

    def remove_all_stock(self):
        ''' Function that removes all stock for a given product'''
        self.amount = 0

    def get_stock(self):
        ''' Function that returns stock amount for a given product'''
        return self.amount



# Inheritance - Define 3 other types of stock through the AppleStock class
class Airpods(AppleStock):
    def __init__(self, amount = int, color = str):
        ''' Initialization function of Airpods class, inheriting amount from AppleStock class'''
        super().__init__(amount) # references to the super class AppleStock
        self.color = color

class iPhone(AppleStock):
    def __init__(self, amount = int, color = str):
        ''' Initialization function of iPhone class, inheriting amount from AppleStock class'''
        super().__init__(amount) # references to the super class AppleStock
        self.color = color

class iPad(AppleStock):
    def __init__(self, amount = int, color = str):
        ''' Initialization function of iPad class, inheriting amount from AppleStock class'''
        super().__init__(amount) # references to the super class AppleStock
        self.color = color



class Warehouse:
    def __init__(self, airpods, iphones, ipads):
        ''' Initialization function for Warehouse Class which is used to provide report of items in stock
        It takes as input the amount of stock for each product.'''
        self.airpods = airpods
        self.iphones = iphones
        self.ipads = ipads
        self.tot_stock = self.airpods + self.iphones + self.ipads

    def get_stock_breakdown(self):
        ''' Function that returns tuple with total stock and stock for each type of item availble'''
        return self.tot_stock, self.airpods, self.iphones, self.ipads

    def report_total_stock(self):
        ''' Function that returns a string indicating the total stock of Apple devices in the warehouse'''
        self.report_tot = "The total amount of Apple devices in stock is: {}".format(self.tot_stock)
        return self.report_tot

    def report_airpods_stock(self):
        ''' Function that returns a string indicating the total stock of Airpods in the warehouse'''
        self.report_airpods = "The total amount of Airpods in stock is: {}".format(self.airpods)
        return self.report_airpods

    def report_iphones_stock(self):
        ''' Function that returns a string indicating the total stock of iPhoes in the warehouse'''
        self.report_iphones = "The total amount of iPhones in stock is: {}".format(self.iphones)
        return self.report_iphones

    def report_ipads_stock(self):
        ''' Function that returns a string indicating the total stock of iPads in the warehouse'''
        self.report_ipads = "The total amount of iPads in stock is: {}".format(self.ipads)
        return self.report_ipads

    def final_report(self): 
        ''' Comprehensive function that puts together all functions above and returns the Inventory Report
        in form of string. '''

        ## Initial idea was to create and return a pandas df with the inventory but had issues
        ## installing pandas on Visual Studio Code, currently solving the problem        
        
        print('________________ Inventory Report _______________')
        print(self.report_airpods_stock())
        print(self.report_iphones_stock())
        print(self.report_ipads_stock())
        print()
        print(self.report_total_stock())
        print('_________________________________________________')
        return ''



### Main Warehouse Class that provides the functionalities
### It needs to create the objects for the different types of stock
### Adding or removing things from the warehouse has to be done in the main

if __name__ == "__main__":
    ''' In the main, all functionalities are displayed, it is divided into 6 sections:
    1. Stock of the different items and colors is initialized
    2. Stock of the different items and colors is removed
    3. Stock of the different items is retrieved
    4. A warehouse is created and the stock previously initialized is added to the warehouse 
    5. A Stock Report is displayed in the terminal to give a summary of the stock available
    6. User is asked whether more items should be added or not '''

    ### 1. Add Stock
    # Add Airpords
    airpods_white = Airpods(2, 'White')
    airpods_black = Airpods(4, 'Black')
    airpods_white.add_stock(5)

    # Add iPhones
    iphone_black = iPhone(2, 'Black')
    iphone_black.add_stock(6)

    # Add iPads
    ipad_red = iPad(2, 'Red')
    ipad_red.add_stock(7)


    ### 2. Remove Stock
    # Remove Airpods
    airpods_white.remove_stock(3)
    
    # Remove iPhones
    iphone_black.remove_stock(3)

    # Remove iPads
    ipad_red.remove_stock(3)


    ### 3. Get Stock
    # Get Airpods stock
    airpods_stock = airpods_white.get_stock() + airpods_black.get_stock()

    # Get iPhone stock
    iphones_stock = iphone_black.get_stock() # + iphone_red.get_stock()

    # Get iPad stock
    ipads_stock = ipad_red.get_stock() # other colors


    ### 4. Create a warehouse with the stock added above
    tot_stock = airpods_stock + iphones_stock + ipads_stock
    warehouse = Warehouse(airpods_stock, iphones_stock, ipads_stock)
    
    ### 5. Create a Stock Report
    stock = warehouse.final_report()
    print(stock)


    ### 6. Ask user if more stock needs to be added [Extra functionality]
    add_items = 'Y'
    while add_items == 'Y':
        add_items = str(input('Would you like to add more items? Y/N  '))
        if add_items == 'Y':
            print('Which item would you like to add?  ')
            device_type = str(input('Please type one of these three: Airpods, iPhone, iPad - '))

            if device_type == 'Airpods':
                device_amount = int(input('How many Airpods would you like to add?  ')) 
                device_color = str(input('Which color would you like your Airpods to be:  '))

                airpods_add = Airpods(device_amount, device_color)
                airpods_stock += device_amount

            elif device_type == 'iPhone':
                device_amount = int(input('How many iPhone would you like to add?  ')) 
                device_color = str(input('Which color would you like your iPhone to be:  '))

                iphone_add = iPhone(device_amount, device_color)
                iphones_stock += device_amount

            elif device_type == 'iPad':
                device_amount = int(input('How many iPad would you like to add?  ')) 
                device_color = str(input('Which color would you like your iPad to be:  '))

                ipad_add = iPad(device_amount, device_color)
                ipads_stock += device_amount


        tot_stock = airpods_stock + iphones_stock + ipads_stock
        warehouse = Warehouse(airpods_stock, iphones_stock, ipads_stock)
        print(warehouse.final_report())

