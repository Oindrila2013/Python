import sys

def intial_slambook():
    rows, cols = int(input("Please enter intial number of contacts: ")), 5

    slam_book = []
    print(slam_book)
    for i in range(rows):
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter your name: ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exising due to blank field...")

            if j == 1:
                temp.append(str(input("Enter friend's name: ")))

            if j == 2:
                temp.append(str(input("Enter home address: ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter catagory(Myself/Friends/School/Others): ")))
                if temp[j] == ' ' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)
    print(slam_book)
    return slam_book