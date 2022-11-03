# İngilizce bir şekilde bir kayıt formu hazırla formatla bilgileri ver tasarım yap if-elif-else kullan.

# tasarım olacak


# REGISTER START

print("-_-_-_-_-REGISTER PAGE-_-_-_-_-")
input("press 'enter' for continue...")

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
height = float(input("Enter your height [with meter]: "))
nickname = input("Enter your nickname: ")

password = input("Please select a password:")
print("Your password has been selected successfully!")

print("-_-_-_-_-REGISTRATION COMPLETED-_-_-_-_-")
# REGSTER END

# PROFILE INFO
print("Here is your profile information...")

print("Name: {} Surname: {} Age: {} Weight: {} Height: {}".format(name,surname,age,weight,height))
print(f"Nickname: {nickname}")

input("press 'enter' for confirm and go to the sign in page")

# SIGN IN START
print("-_-_-_-_-SIGN IN PAGE -_-_-_-_-")
input("press 'enter' for continue...")

#Veri tabanı
dbUsername = nickname
dbPassword = password

username = input("Please Enter your Nickname: ")

if dbUsername == username:
    passcode = input("Please Enter your Password: ")
    if dbPassword == passcode:
        print("You have signed in successfully!")
    else:
        print("Your password is wrong.")
else:
    print("Account not found")

# SIGN IN END

# CODES ALL COMPLETED