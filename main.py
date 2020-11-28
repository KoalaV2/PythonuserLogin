#!/usr/bin/env python3

import bcrypt
import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()
def writepasswd():
    c.execute('''CREATE TABLE IF NOT EXISTS users (username,password)''')
    username = input("What is your username? \n :").encode("utf-8")
    passwd = input("What is your password? \n :").encode("utf-8")
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    c.execute("INSERT INTO users VALUES (?,?);",(username,hashed))
    conn.commit()
    conn.close()
    return passwd,hashed
def main():
    passwd, hashed = writepasswd()
    if bcrypt.checkpw(passwd, hashed):
        print("It matches!")

    else:
        print("Password does not match")
if __name__ == "__main__":
    main()
