new_file = open('New_file1.txt', 'x')
new_file.close()

import os
print("Checking if my file exists or not...")
if os.path.exists("codingal.txt"):
    os.remove("codingal.txt")
else:
    print("The file doesn't exists")

codingal_update = open('codingal_update.txt', 'w')
codingal_update.write("Hi! I am Penguin and I am 1 year old")
codingal_update.close

os.rmdir("Codingal")