#Password manager

import random
import hashlib

print("Welcome to passwords manager\n")
print("Please type your login and password")

login = input("Login: ")
passwd = input("Password: ")
access_log = "admin"
access_passwd = "admin"


while login != access_log or passwd != access_passwd:
    print("-"*10)
    login = input("Login: ")
    passwd = input("Password: ")

def manager():
    while True:
        print("\n","-"*15)
        print(" Select action \n ep - encrypt password \n gp - generate random password \n get - get password \n q - quit")
        print("","-"*15)
        choice = str(input("What do you want to do?: "))
        if choice == "ep":
            choice = str(input("choose xor/caesar/md5: ")).lower()
            sentence = input("Please type your password: ")
            if choice == "xor":
                keey = int(input("Please type your key to hash and unhash, save it to further decode: "))
                idk = _xor(sentence, keey)  
                save_to_file("passwords", idk, 0) #0 to flaga do zapisywania zahashowanych haseł (xor)
                print("Done! Your password is now in password file!")
            elif choice == "caesar":
                keey = int(input("Please type your key to hash and unhash, save it to further decode: "))
                idk = caesar(sentence, keey)  
                save_to_file("passwords", idk, 1) #1 to flaga do zapisywania zahashowanych haseł (cezar)
                print("Done! Your password is now in password file!")
            elif choice == "md5":
                idk = encrypt_md5(sentence)  
                save_to_file("passwords", idk, 2) #2 to flaga do zapisywania zahashowanych haseł (md5)
                print("Done! Your password is now in password file!")
            else:
                raise ValueError

        elif choice == "gp":
            number_of_char = int(input("How long do you want your password to be? "))
            idk = generate_pass(number_of_char)
            print(f"Your random password is: {idk}")
            ans = str(input("Do you want to save it to the file? Y/N: ")).lower()
            if ans == "y":
                save_to_file("passwords", idk, 3)  #3 to flaga do zapisywaniem wygenerowanych haseł
            elif ans == "n":
                print("You chose to not save password.")
            else:
                raise ValueError

        elif choice == "get":
            break
        elif choice == "q":
            break

    

def save_to_file(file_, idk, flag):
    with open(file_ + ".txt", mode="a", encoding="utf-8") as f:
        if flag == 0:
            f.write(" URL, xor password : " + str(idk) + "\n")
        elif flag == 1:
             f.write(" URL, caesar password: " + str(idk) + "\n")
        elif flag == 2:
             f.write(" URL, md5 password: " + str(idk) + "\n")
        elif flag == 3:
             f.write(" Generated password is: " + str(idk) + "\n")
        else:
            print("błąd")
        f.close()


# XOR
# ------------------------------------------------------    
def _xor(sentence, keey):
    cipher = ""
    for i in sentence:
        cipher += chr(ord(i)^keey)  #each char sets by key value
    return cipher
# -------------------------------------------------------


# CAESAR
# -------------------------------------------------------
def caesar(txt, key=4):
    cipher = ""
    for char in txt:
        if not char.isalpha():
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97)
    return cipher
    # print(cipher)
# ---------------------------------------------------------------


# MD5
# ----------------------------------------------------------------
def encrypt_md5(txt):
    cipher = hashlib.md5(str(txt).encode()).hexdigest()
    return cipher
    # print(cipher)
# ---------------------------------------------------------------


# generate password
# ----------------------------------------------------------------
def generate_pass(number_of_char):
    lottery = "".join([random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for char in range(number_of_char)])
    return lottery
# ----------------------------------------------------------------


if __name__ == "__main__":
    manager()    












