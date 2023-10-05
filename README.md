# Barbar-Sleeping-Problem
A barbershop consists of a waiting room with n chairs, and a barber room containing the barber chair. If there
are no customers to be served, the barber goes to sleep. If a customer enters the barbershop and all chairs are
occupied, then the customer leaves the shop. If the barber is busy, but chairs are available, then the customer sits
in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate
the barber and the customers.

Overview
This Python program simulates a simplified barber shop system where customers arrive for haircuts, and a barber provides haircuts to customers. The program uses multi-threading to model the interactions between customers and the barber.

Features
Customers arrive at the barber shop and request haircuts.
The barber serves customers with different hair types (short, medium, long) and estimates the time required for each haircut.
Customers wait in a waiting room with a limited number of chairs.
The program tracks the number of haircuts given, tips received by the barber, and the shop's daily profit.
The barber can take short naps when there are no customers in the waiting room.
Usage
Run the program by executing main.py i.e Khadija_CS-19075.py file .

Enter the number of chairs in the waiting room when prompted. This determines how many customers can wait at once.

Enter the number of customers you want to simulate.

The program will simulate the barber shop operations, including customers arriving, getting haircuts, and the barber taking breaks.
