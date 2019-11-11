# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Josh Embury, 11/10/19, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
print("Loading existing To Do List...")
File = open(objFile, "a")
File = open(objFile, "r")
if not File.read():
    print("Current To Do List empty.")
else:
    File = open(objFile, "r")
    for row in File:
        strData = row.split(",")
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    print("Load successful.")
File.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable:
            print("To Do List is Empty! Please enter tasks and priorities!")
        else:
            for row in lstTable:
                print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        lstRow = ["", ""]
        lstRow[0] = input("Enter new task: ")
        lstRow[1] = input("Enter priority: ")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        currentLen = len(lstTable)
        removal = input("Which task would you like to remove? : ")
        for row in lstTable:
            if row["Task"] == removal:
                lstTable.remove(row)
        newLen = len(lstTable)
        if newLen == currentLen:
            print(removal + " does not exist in To Do List")
        else:
            print("Task removed!")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        File = open(objFile, "w")
        for row in lstTable:
            File.write(row["Task"] + ", " + row["Priority"] + "\n")
        File.close()
        print("Tasks written to file!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program!")
        break  # and Exit the program