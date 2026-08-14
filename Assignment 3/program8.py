
correct_userid = "Radha_Krishn"
correct_password = "Radhe-Radhe"
 
userid = input("Enter userid: ")
password = input("Enter password: ")
 
if (userid == correct_userid )and (password == correct_password):
    captcha = 876543
    print(f"Captcha code: {captcha}")
    entered_captcha = int(input("Enter the captcha shown above: "))
    if (entered_captcha == captcha):
        print("Success! Captcha Verified.")
    else:
        print("Failed! Captcha does not match.")
else:
    print("Invalid Userid or Password")
 