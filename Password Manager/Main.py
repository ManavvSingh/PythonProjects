from cryptography.fernet import Fernet
# Module to encrypt text

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

#  # write_key()

def load_key():
    file = open("key.key","rb") #rb -> read byte
    key = file.read()
    file.close()
    return key

# Mpwd = input("Please enter the master password: ")
key = load_key() # + Mpwd.encode()
fer = Fernet(key)

# def view():
#     with open('pwd.txt', 'r') as f:
#         for lines in f.readlines():
#             data = lines.rstrip()
#             user,passw = data.split("|")
#             print("User: ",user,"| Password: ",(fer.decrypt(passw.encode())).decode())

def view():
    with open('pwd.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

def add():
    name = input("Enter account name: ")
    pwd = input("Enter password: ")

    with open('pwd.txt', 'a') as f:
        # a - open for writing, appending to the end of the file if it exists
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        # f.write("Account name: " + name + " || " + "Password: " + (fer.encrypt(pwd.encode())).decode() + "\n")

while True:
    func = input("Would you like to view your existing passwords or add a new password or Quit? (view or add or quit) ").lower()
    if func == "quit":
        break

    if func == "view":
        view()
    elif func == "add":
        add()
    else:
        print("Invalid input. Please enter view or add")
        continue
