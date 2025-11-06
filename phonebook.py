import sys

def intial_phonebook():
    rows, cols = int(input("Please enter intial number of contacts: ")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name: ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exising due to blank field...")

            if j == 1:
                temp.append(str(input("Enter number: ")))

            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter catagory(Family/Friends/Work/Others): ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
    print("1. Add a new contact")
    print("2. Remove an exising contact")
    print("3. Delete all contacts")
    print("4. Search for all contacts")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = (int(input(" Please enter a choice: ")))
    return choice

def contact_add(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
                dip.append(str(input("Enter name: ")))

        if i == 1:
                dip.append(str(input("Enter number: ")))

        if i == 2:
                dip.append(str(input("Enter e-mail address: ")))

        if i == 3:
                dip.append(str(input("Enter date of birth(dd/mm/yy): ")))

        if i == 3:
                dip.append(str(input("Enter catagory(Family/Friends/Work/Others): ")))

    pb.append(dip)
    return pb

def remove_exising(pb):
    query = (int(input("Please enter the name of the contact you wish to remove: ")))
    temp = 0
    for i in range(len(pb[0])):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            return pb
    if temp == 0:
        print("Sorry you have entered an invalid query. Please recheck and try again.")
        return pb
