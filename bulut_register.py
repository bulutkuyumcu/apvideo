# Name: Bulut Kuyumcu
# Student No: 304
# Subject: Register Form

# Register Start
print("-_-_-_-_-REGISTER PAGE-_-_-_-_-")
input("press 'enter' for continue...")

# Get User Information

# Name
name = input("Enter your name: ")
# Surname
surname = input("Enter your surname: ")
#Age
age = int(input("Enter your age: "))
# Weight ( we get this info with kg.g for become float.)
weight = float(input("Enter your weight: "))
# Height ( we get this info with meter for become float.)
height = float(input("Enter your height [with meter]: "))
# Nickname ( We are gonna use this info while we are signing in)
nickname = input("Enter your nickname: ")
# Password ( We are gonna use this info while we are signing in)
password = input("Please select a password:")
# Confirmation text.
print("Your password has been selected successfully!")

print("-_-_-_-_-REGISTRATION COMPLETED-_-_-_-_-")
# Register End

# Print User Information Start
print("Here is your profile information...")

print("Name: {} Surname: {} Age: {} Weight: {} Height: {}".format(name,surname,age,weight,height))
print("Nickname: {}".format(nickname))
# Print User Information End

# Another Confirmation
input("press 'enter' for confirm and go to the sign in page")

# Sign In Start
print("-_-_-_-_-SIGN IN PAGE -_-_-_-_-")
input("press 'enter' for continue...")

#Veri tabanı
dbNickname = nickname
dbPassword = password

inputNickname = input("Please Enter your Nickname: ")
if dbNickname == inputNickname:
    inputPassword = input("Please Enter your Password: ")
    if dbPassword == inputPassword:
        print("You have signed in successfully!")
    else:
        print("Your password is wrong.")
else:
    print("Account not found")
# Sign In End

""" The codes that we use in 49 to 57 is be usefull for the conditions that we are gonne use while we are
signing in  """