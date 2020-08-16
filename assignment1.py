"""
Replace the contents of this module docstring with your own details
Name: NGUYEN THANH HAI
Date started: 30/7/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-travel-tracker-thanhhai93/blob/master/assignment1.py
"""

''''Here are the global lists which will be used in the function, also the command to open the songs.csv file. I 
import csv library just in case i have to use some of its function to interact with the csv file. one important list 
to notice is the FILE_LIST in which will store all valuable data from main_menu(), list_function, add_function() and 
learnt_function() '''


remainder = [1]
total_place = [0]
place= open('place.csv', "r")
FILE = place.readline()


def main():
    print("Travel Tracker 1.0 - by <NGUYEN THANH HAI>")
    main_menu()



def main_menu() :
    print("Menu: ")
    count_need = 0
    for lines in file:
        count_load +=1
    print(cout_load, "places loaded")

    print("L - List places ")
    print("A - Add new place ")
    print("M - Mark a place as visited ")
    print("Q - Quit ")
    menu = input(">>>").upper()
    while menu not in ["L", "A", "M", "Q"]:
        menu = input ("Invalid menu choice ").upper()
    if menu == "L":
        list_function()
    if menu == "A":
        add_function()
    if menu == "M":
        learnt_function()
    else:
        confirm = input("Are you sure you want to quit? -(Y)es, (N)o ").upper()
        while confirm not in ["Y", "N"]:
            confirm = input("Invalid, please re-enter your option: (Y)es or (N)o").upper()
        if confirm == "Y":
            with open("place.csv", "w") as place:
                for item in FILE:
                    place.write("{}".format(item))
                print("4 places saved to places.csv")
                print("Have a nice day :) ")
                quit()
        else:
            main_menu()

    def list_function():
        count = 0
        count_learnt = 0

        list = []
        for lines in FILE:
            count += 1
            new_lines = lines.split(',')
            input_place = new_lines[0]
            input_country = new_lines[1]
            input_priority = new_lines[2]
            learn = new_lines[3].replace("l", "*").replace("u", "").replace("\n", "")
            list.append(count)
            places_display = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, learn, input_place, input_capital, input_priority))
            print(places_display)

            if "*" in learn:
                count_learnt += 1
        print("-" * 3)
        print("Total places loaded: ", max(list))
        count_need = (max(list) - count_learnt)
        REMAINDER.append(count_need)
        print(max(list) - count_learnt, "places still to learn")
        print(count_learnt, "places learned")
        TOTAL_PLACE.append(max(list))
        print("-" * 3)
        main_menu()

def add_function():
    learn_status = "u\n"
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country == "":
        print("Input can not be blank")
        country = input("Country: ")
    test = True
    while test == True:
        try:
            priority = int(input("Priority: "))
            test = False
        except ValueError:
            print("Invalid input; enter a valid number")
    while priority < 0:
        print("Number must be > 0")
        test = True
        while test == True:
            try:
                priority = int(input("Priority: "))
                test = False
            except ValueError:
                print("Invalid input; enter a valid number")

    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    final_result = ("{},{},{},{}".format(name, country, priority, learn_status))
    FILE_LIST.append(final_result)
    print("{} by {} from ({}) added to place list".format(name, country, priority))
    print('-' * 3)
    main_menu()

def learnt_function():
    learn_status = "l\n"
    if min(REMAINDER) == 0:
        print('-' * 3)
        print("No more places to learn!")
        print('-' * 3)
        main_menu()

    test = True
    while test == True:
        try:
            number = int(input("Enter the number of a place to mark as visited: "))
            test = False
        except ValueError:
            print("Invalid input, please enter a number")
    if max(TOTAL_PLACES) == 0:
        print("-" * 3)
        print("4 places. You still want to visit 3 places.")
        print("-" * 3)
        main_menu()

    while number > max(TOTAL_PLACE) or number <= 0:
        print("No unvisited places")
        number = int(input("Enter the number of a place to mark as visited: "))

    rows = FILE[number - 1]
    new_list_rows = rows.split(",")
    place_name = new_list_rows[0]
    country_name = new_list_rows[1]
    priority = new_list_rows[2]
    result = ("{},{},{},{}".format(place_name, country_name, priority, learn_status))

    FILE.append(result)
    FILE.remove(FILE[number - 1])

    print("4 places. No places left to visit. Why not add a new place? ")
    print('-' * 3)
    main_menu()



if __name__ =='__main__':
    main()










