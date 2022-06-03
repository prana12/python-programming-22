password1 = input("Password: ")
while True:
    password2 = input("Repeat Password: ")
    if(password1 == password2):
        print("User account created!")
        break
    print("They do not match!")