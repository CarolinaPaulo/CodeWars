# -*- coding: utf-8 -*-
"""(8 kyu) Transportation on vacation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CnCpPvV65emnHsHwN_mN-0dZWQi7W3w9

After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.


Every day you rent the car costs \$ 40.   If  you rent the car for 7 or more days, you get \$50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.


Write a code that gives out the total amount for different days(d)
"""

def rental_car_cost(d):
    # your code
    a = d
    if a >= 7:
        car_cost = a * 40 - 50.0
        return car_cost
    if a >= 3 and a < 7:
        car_cost = a * 40 - 20.0
        return car_cost
    else:
        car_cost = a * 40
    
        return car_cost