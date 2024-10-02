#!/bin/bash

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance, defaulting to zero."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from the account balance if sufficient funds are available.
        Returns True if successful, otherwise False.
        """
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

