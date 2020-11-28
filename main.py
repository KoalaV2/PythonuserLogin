#!/usr/bin/env python3

import bcrypt
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
def writepasswd():
    c.execute('''CREATE TABLE IF NOT EXISTS users (username,password)''')
    username = input("What is your username? \n :") 
    passwd = input("What is your password? \n :").encode("utf-8")
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    c.execute("INSERT INTO users VALUES (?,?);",(username,hashed))
    conn.commit()
    conn.close()
    return passwd,hashed
def checkpasswd():
#    cursor= c.execute("SELECT username,password FROM users")
    # for row in cursor:
        # print("USERNAME = ", row[0])
        # print("HASHEDPASSWD = ", row[1]) 
# #    if bcrypt.checkpw(passwd,hashed):
# #        print("It matches!")
    conn.close()
def deleteuser():
    cursor= c.execute("SELECT username,password FROM users")
    for row in cursor:
        print("\n USERNAME = ", row[0])
    user = input("\n What user do you want to delete? \n : ")
    c.execute("DELETE from users where username =" + f'"{user}"' + ";")
    conn.commit()
def main():
    choice = input("signup, delete or login? \n :")
    if choice == "signup":
        writepasswd()
    elif choice == "login":
        checkpasswd()
    elif choice == "delete":
        deleteuser()
    else:
        print("Something went wrong")
if __name__ == "__main__":
    main()
