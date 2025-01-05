from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("What is the master password? ")
key= load_key()+ master_pwd.encode()
fer=Fernet(key)


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def view():
    with open("Passwords.txt", 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
            user,passw = data.split("|")
            print(f"User: {user}, Password: {str(fer.decrypt(passw.encode()).decode())}")

def add():
    name= input("Account Name:")
    pwd= input("Password: ")

    with open("Passwords.txt", 'a') as f:
        f.write(name+ "|" +  + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones(view,add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("Invalid mode. ")
        continue