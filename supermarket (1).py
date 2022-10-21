import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from customer import Customer
import random

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.opening_time = datetime.strptime("07:00:00","%H:%M:%S")
        self.closing_time = datetime.strptime("22:00:00","%H:%M:%S")

    def __repr__(self):
        print ('Welcome to MARTkov')

    def get_time(self):
        """current time in HH:MM format,
        """
        hour = 7 + self.minutes // 60
        minute = self.minutes % 60
        return f'{hour:02}:{minute:02}:00'

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        from customer import Customer
        for customer in self.customers:
            time = self.get_time()
            print(f"{time}, Customer {customer.identifier}, {customer.location}")

    def next_minute(self):
        """propagates all customers to the next state.
        """
        from customer import Customer
        self.minutes = self.minutes =+ 1
        for customer in self.customers: 
            customer.move_location()
        #return cust.location, self.minutes
    
    def add_new_customers(self):
        """randomly creates new customers.
        """
        from customer import Customer
        for i in range(1,3):
            customer = Customer()
            self.customers.append(customer)
        return self.customers

    def remove_finished_customers(self):
        """removes every customer that is not active any more.
        """
        from customer import Customer
        for customer in self.customers:
            if customer.location == 'checkout':
                customer.status = 'churned'
                self.customers.remove(customer)    
        return self.customers


martkov = Supermarket()
martkov.get_time()
martkov.print_customers()
martkov.add_new_customers()
martkov.next_minute()
martkov.remove_finished_customers()
martkov.get_time()
martkov.print_customers()
martkov.add_new_customers()
martkov.next_minute()
martkov.remove_finished_customers()
martkov.get_time()
martkov.print_customers()
martkov.add_new_customers()
martkov.next_minute()
martkov.remove_finished_customers()