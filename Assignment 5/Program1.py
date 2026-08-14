##1 Prompt user to enter userid and password. Give 3 chances if wrong, then terminate.

userid = "Radha_Krishn"
password = "Radhe-Radhe"
attempts = 0
while (attempts < 3):
    id = input("Enter the userid: ")
    password = input("Enter the password: ")
    if (id == userid) and (password == password):
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect credentials. Attempts left:",(3 - attempts))
else:
    print("Too many failed attempts. Program terminated.")

