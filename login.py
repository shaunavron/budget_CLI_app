import hashlib

USERS = "users.txt"
    
def read_users():
    """Reads user data from users.txt"""
    try:
        with open(USERS, 'r') as file:
            lines = file.readlines()
            user_dict = {}
            for line in lines:
                username, password = line.strip().split(":")
                user_dict[username] = password
            return user_dict
    except FileNotFoundError:
        return {}

def write_users(user_dict):
    """Writes user data to users.txt. Passwords are hashed before stored"""
    with open(USERS, 'w') as file:
        for username, password in user_dict.items():
            file.write(f"{username}:{password}\n")

def register():
    print("Welcome! Please create your account below!")
    users = read_users()
    username = input("Username: ")
    while True:
        if username in users:
            print("Username taken, please try a different username.")
        else:
            break
    password = input("Password: ")
    # Password Hashing
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_pass
    write_users(users)
    print("You're registered!")

def login():
    print("Please enter your login details below: ")
    username = input("Username: ")
    password = input("Password: ")
    users = read_users()
    # Password Hashing
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed_pass:
        print("Login Successful!")
        return username
    else:
        # Implement username doesn't exist thing
        print("Invalid username or password")
        return None

def logout():
    print("Logout Successful")
    return None
