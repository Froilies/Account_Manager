import base64
import os
from cryptography.fernet import Fernet

def Prog_pass():
    key = input("What is the Program key")
    return key

#First, Create your own private key using this function and store securely
"""def create_key():
    key = Fernet.generate_key()
    with open("secure.key", 'wb') as key_file:
        key_file.write(key)"""


def view():
    print("The existing accounts in the program are as follows:\n")
    with open("accounts.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            website, username, pwd = data.split("  ||  ")
            print(f"Website: {website}, Username: {username}, Password: {pwd}")


def delete():
    site_delete = input("What website would you like to delete: ")
    i=0
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
    with open("accounts.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            website, username, pwd = data.split("  ||  ")
            while i <= len(line):
                if website == site_delete:
                    del lines[i]
                    break
                else:
                    i += int(1)
                    break
    with open("accounts.txt", "w") as file:
        for line in lines:
            file.write(f"{line}")
        print("Account sucessfully deleted!")
        return




def add():
    website = input("What website is the account connected to: ")
    username = input("Account log in: ")
    pwd = input("Account password: ")

    with open("accounts.txt", "a+") as file:
        file.writelines(website + "  ||  "+ username + "  ||  "+ pwd + "\n")
    print("Account succesfully Added!")




def main():
    print("Account accessed! What would you like to do")

    while True:
        selection = input("Pick a selection: Add: Add an account \n"
                          "View: View existing accounts, \n"
                          "Delete: Delete an existing account or \n"
                          "Quit: Exit the Program\n").lower()

        if selection == "quit" or selection == "q":
            print("This program will now close")
            break
        if selection == "add" :
            add()
        elif selection == "view" :
            view()
        elif selection == "delete" :
            delete()
        else:
            print("invalid selection")
            continue


if Prog_pass() == "gypG3JOXyKKrSi3EJ2_gNYoAVqo2FT5P7rF1M3_3d-M=":
    main()
else:
    print("Wrong key")