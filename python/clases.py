#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clases.py
#  
#  Copyright 2022 epigm <epigm@SEXMACHINE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
class Item:
	pay_rate = 0.8 #The pay rate after 20% discoount
	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		assert price >= 0, f"Price {price} is not greater than or equal to zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
		
		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):
		return f"The total price of {self.name} is {self.price * self.quantity}"
		
	def apply_discount(self):
		self.price = self.price * self.pay_rate


def main(args):
	item1 = Item("Phone", 100, 1)
	item2 = Item("Laptop", 1000, 3)
	item3 = Item("Cable", 10, 5)
	item4 = Item("Mouse", 50, 5)
	item5 = Item("Keyboard", 75, 5)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


