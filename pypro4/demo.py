#Implementing password hashing in Python using Bcrypt 
import bcrypt#The import that would be used for the hashing. 

password = b"thisismypassword" #Initial Password that is going to be used as a reference.
hashed_password=bcrypt.hashpw(password,bcrypt.gensalt())#The password is now hashed using the bycrypt.hashpw(). That function only accepts bytes, so the original password needed to be converted into bytes. 
#The gensalt() function adds 'salt' to the hashed password. 'Salt' is used as a means of prevention to prevent the chance of a person guessing the hash and reverse-engineering the passwords stored in a database. 
 

print(hashed_password)

entered_Password = input("Enter password to login: ")#New password that is going to be compared with the original. 
entered_Password = bytes(entered_Password, encoding='utf-8')#Conversion into bytes. 


if bcrypt.checkpw(entered_Password,hashed_password):#This is a function that checks the passsword input and then compares it to the hashed output
    print("Login successful")
else:
    print("Invalid password")
