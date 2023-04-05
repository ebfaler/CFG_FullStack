'''TASK 3 Efuah Faler Homework 4'''

# Simple Shop Program
# Using exception handling code blocks such as try/ except / else / finally, write a program that simulates a customer in a shop
# (NB: the more code blocks the better, but try to use at least two key words e.g. try/except, raise)


# Tasks:
# Create a dictionary with a minimum of 3 items and prices
# One of the items needs to cost more than £100
# Customer’s available money is £100
# Welcome the customer and display the items and their prices, along with an option to “exit”
# Accept the option as an input, an invalid input should raise a ValueError
# If the customer can afford it, print out a message saying “Here’s your {item}!”
# The user should be then greeted out of the shop, and the program terminated.
# If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
# The purchase should be tried a maximum of 3 items, if it fails a custom error should be raised and the customer will exit the shop.

shop_items = {
    "top": 150,
    "scarf": 99,
    "bag": 1020
}


# CUSTOM ERROR
class BalanceError(Exception):
    "Raised when the user has been asked 3 times but can't afford the purchase"
    pass


# INPUT FUNCTIONS
def get_input(text):
    return input(text)


def get_more_money(text):
    return int(input(text))


# FUNCTION TO GET ITEM PRICE (and checkout)
def item_price():
    balance = int(100)
    attempts = 0

    item_name = get_input("What item would you like to buy? ").lower()
    price = (shop_items[item_name])
    print('OK. The ' + item_name + " costs " + str(price))

    if balance >= price:
        print('Here is your ' + item_name + '. Goodbye and have a nice day!')
        return price

    else:
        while attempts <= 3:
            print("Sorry, but you can't afford that currently. Your balance is " + str(balance))
            try:
                more_money = get_more_money('How much money can you add to your balance? ')
                new_balance = balance + more_money
                balance = new_balance
                print("Ok, I've added " + str(more_money) + ". Your updated balance is " + str(balance))
            except ValueError:  # added this to only accept valid input
                print("Sorry, that's not a valid amount. Please try again")
            attempts += 1
            if balance >= price:
                print('Here is your ' + item_name + '. Have a nice day!')
                return price
            if attempts == 3:
                raise BalanceError
            else:
                continue


# MAIN SHOP FUNCTION
def luxury_shop():
    print('Hello and welcome to Luxury Shop, We stock the following items: ')
    for key, value in shop_items.items():
        print(key, ':', value)

    exit = get_input("It's expensive here. Type y to stay, or n to exit ").lower()

    if exit == 'n':
        print("Goodbye!")
        return
    elif exit == 'y':
        print("Ok, I'm happy that you're staying!")

        try:
            item_price()
        except KeyError:
            print("Sorry, we don't have that item in stock")

        except BalanceError:
            print('Sorry there is a problem with your balance. Please kindly leave the shop.')

        finally:
            print("Goodbye!")
    else:
        raise ValueError('The format needs to be n for no, or y for yes')


# Uncomment below to run the function (I commented it out while running tests)
# luxury_shop()
