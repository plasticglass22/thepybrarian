import sys
import re
import numpy

## Menu Object
class Menu:
    def __init__(self, name, choices):
        self.name = name
        self.choices = choices

    ## This method will be used to make a choice and move to the next menu.
    def __call__(self, num):
        print(num)

## Menu Instances
mainMenu = Menu("Main Menu", 
                ["Topics", "List All Books", "FAQ", 
                 "Additions and Removals", "About the Project"])

topicsMenu = Menu("Topics", ["ABC", "DEF", "GHI", "JKL"])

## Book Object

def show_menu(m):
    # print("list menu options here")
    print(m.name + ": ")
    for i in range(0, len(m.choices)):
        print(str(i+1) + ". " + m.choices[i])

def main():
    print("Welcome to Pybrarian, a Python3 implementation of Librarian.")
    print("Search, catalogue, and access your PDFs and eBooks from the command line.")
    print("")
    print("")
    show_menu(mainMenu)
    print("")

    ## ISSUE 1-1 ##
    print("Please select an option by typing the number of your choice: ")
    m = input(">> ")

    ## ISSUE 1-2 ##
    if (int(m) < 1) or (int(m) > len(mainMenu.choices)):
        print("Invalid input. Please try again: ")
        show_menu(mainMenu)

    ## ISSUE 1-3 ##
    if int(m) == 1:
        show_menu(topicsMenu)
        print("")
        print("Select a topic: ")
        topic = input(">> ")

if __name__ == '__main__':
    main()