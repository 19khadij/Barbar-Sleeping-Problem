import time
import random
#import Queue
try:
   import queue
except ImportError:
   import Queue as queue
from threading import Thread

NAMES=["Al", "Alex", "Anthony", "Bill", "Bob", "Brad", "Cam", "Cal",
         "Chris", "Charlie", "Dave", "Dan", "Derek", "Devin", "Eric",
         "Elijah", "Frank", "Fred", "Gary", "George", "Hal", "Harry",
         "Isaac", "Ishmael", "Jared", "Jake", "Jeremy", "Kevin", "Kris",
         "Larry", "Louie", "Mark", "Mort", "Nathan", "Norb", "Oscar",
         "Orville", "Peter", "Paul", "Quinn", "Rob", "Rick", "Steve",
         "Tim", "Trevor", "Ulysses", "Victor", "Walter", "Xavier",
         "Yadier", "Zack"]

class Barber(Thread):

    def __init__(self, waiting_customers):
        super(Barber, self).__init__()
        self.waiting_customers = waiting_customers # the Queue passed in
        self.number_haircuts = 0
        self.tips = 0 
        self.days_profit = 0 
        self.shop_open = True # Flag to end the main thread
        self.sleeping = True # Flag to have the barber start at sleep until a customer arrives

    def run(self):
        while self.shop_open or not self.waiting_customers.empty(): # continue until Queue is empty or shop is closed 
            if not self.waiting_customers.empty(): 
                self.sleeping = False # if customers awake 
                customer = self.waiting_customers.get()
                if customer.hair_type == 'short':
                    customer.in_barber_chair = True
                    print("The barber is cutting %s's hair." % customer.name)
                    print("%s has %s hair, this should take 20 minutes." % (customer.name, customer.hair_type))
                    time.sleep(2)
                elif customer.hair_type == 'medium':
                    customer.in_barber_chair = True
                    print("The barber is cutting %s's hair." % customer.name)
                    print("%s has %s hair, this should take 40 minutes." % (customer.name, customer.hair_type))
                    time.sleep(4)
                else:
                    customer.in_barber_chair = True
                    print("The barber is cutting %s's hair." % customer.name)
                    print("%s has %s hair, this should take 60 minutes." % (customer.name , customer.hair_type))
                    time.sleep(6)
                print("Done cutting %s's hair" % customer.name)
                self.number_haircuts += 1
                self.tips += random.choice(range(6))
                self.days_profit += 15
            elif not self.sleeping: # elif no customers in line and not already sleeping go to sleep
                self.sleeping = True 
                print("No one in the waiting room, the barber is going to nap in his chair")
                print("The barber gave %d haircuts and made $%d." % (self.number_haircuts, sum([self.tips, self.days_profit]))) 


class Customer(Thread):

    def __init__(self, name, hair_type):
        super(Customer, self).__init__()
        self.name = name
        self.hair_type = hair_type
        self.in_barber_chair = False

    def run(self):
        while not self.in_barber_chair:
            pass
        if customer.hair_type == 'short':
            customer.in_barber_chair = True
            print("The barber is cutting %s's hair." % customer.name)
            print("%s has %s hair, this should take 20 minutes." % (customer.name, customer.hair_type))
            time.sleep(2)
        elif customer.hair_type == 'medium':
            customer.in_barber_chair = True
            print("The barber is cutting %s's hair." % customer.name)
            print("%s has %s hair, this should take 40 minutes." % (customer.name, customer.hair_type))
            time.sleep(4)
        else:
            customer.in_barber_chair = True
            print("%s has %s hair, this should take 60 minutes." % (customer.name , customer.hair_type))
            time.sleep(6)

if __name__ == '__main__':
    hair_types = ['short', 'medium', 'long'] # additional variable for a haircut length to simulate time
    chair=int(input("Enter no of chairs:"))
    waiting_room = queue.Queue(chair) # a queue for a waiting room with max input chairs
    barber = Barber(waiting_room)        
    barber.start()
    cust=int(input("Enter no of cust:"))
    close_time = 48 # end thread after 48 seconds
    shop_open = time.time()
    current_time = shop_open
    while (current_time - shop_open) < close_time: # check if barber thread has been running longer than open time
        i_need_a_haircut = random.choice(NAMES) # pick a random name
        if cust<=chair:
           if not waiting_room.full(): # if the Queue isn't full grab a seat
            length = random.choice(hair_types)
            customer = Customer(i_need_a_haircut, length)
            waiting_room.put(customer)
            print("%s sat down in the waiting room" % i_need_a_haircut)
            customer.start()
            chair=chair-1
         
        elif chair!=0:
           if not waiting_room.full(): # if the Queue isn't full grab a seat
            length = random.choice(hair_types)
            customer = Customer(i_need_a_haircut, length)
            waiting_room.put(customer)
            print("%s sat down in the waiting room" % i_need_a_haircut)
            customer.start()
            chair=chair-1
        else:
           print("Sorry, %s too full, try coming back when its not so busy" % i_need_a_haircut)
        stagger = random.choice([1, 5, 10, 20]) # stagger time each customer thread is created
        time.sleep(stagger)
        current_time = time.time()
    barber.shop_open = False # close shop/barber will finish off remaining threads in queue.
