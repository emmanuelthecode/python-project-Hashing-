#This is a tkinter program that produces a Graphical User Interface using the inbuilt Tkinter interface in python.

import bcrypt#The import that would be used for the hashing. 
from tkinter import *

def validate_password():#This method validates the password through the use of hashing. It compares the new one to the old one.
    hashed_version = bytes(entry_1.get(), encoding='utf-8')
    hashed = bcrypt.hashpw(hashed_version,bcrypt.gensalt())#The password is now hashed using the bycrypt.hashpw(). That function only accepts bytes, so the original password needed to be converted into bytes. 
#The gensalt() function adds 'salt' to the hashed password. 'Salt' is used as a means of prevention to prevent the chance of a person guessing the hash and reverse-engineering the passwords stored in a database. 
 

    second_hashed = bytes(entry_2.get(), encoding='utf-8')
    if(bcrypt.checkpw(second_hashed, hashed)):#This is a function that checks the passsword input and then compares it to the hashed output
        print("The passwords are the same.")
    else:
        print("The passwords are different.")
    




root = Tk()

label_1 = Label(root, text="Type your password")
entry_1 = Entry(root)
label_2 = Label(root, text = "Re-enter your password")
entry_2 = Entry(root)
button_1 = Button(root, text="Confirm", command=validate_password)

label_1.grid(row=0, column=0)
entry_1.grid(row = 0, column=1)
label_2.grid(row=1, column=0)
entry_2.grid(row=1, column=1)
button_1.grid(row =2, column=1)
root.mainloop()