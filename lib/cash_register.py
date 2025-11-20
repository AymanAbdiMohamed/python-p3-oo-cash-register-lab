#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount      # discount percentage
        self.items = []               # list of item names
        self.last_transaction = 0     # track last transaction amount

    def add_item(self, name, price, quantity=1):
        """Add items to the register and track last transaction."""
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(name)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """Apply discount to the total and print success message."""
        if self.discount:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction
        self.last_transaction = 0
