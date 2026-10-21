import base64
File="vault.txt"
def encode_data(data):
    return base64.b64encode(data.encode()).decode()
def decode_data(data):
    return base64.b64decode(data.encode()).decode()
def password_strength(password):
    if len(password)<6:
        return "weak"
    elif len(password)<10:
        return "medium"
    else:
        return"strong"
def add_credentials():
    website=input("enter website:")
    username=input("ener username:")
    password=input("enter password:")
    strength=password_strength(password)
    data=website + "|" + username + "|" + password
    encoded = encode_data(data)
    with open(File,"a")as file:
        file.write(encoded + "/n")
    print("credentials saved")
    print("password strength:",strength)
def view_credentials():
    try:
        with open(File,"r")as file:
            lines=file.readlines()
        if not lines:
          print("No credentials found")
          return
        for line in lines:
          data = decode_data(line.strip())
          website, username, password= data.split("|")
          print("/n Website:", website)
          print(" username:", username)
          print("password:","*" * len(password))
    except FileNotFoundError:
        print("No credentials found")
def update_password():
    website=input("enter your website:")
    new_password=input("enter your new password: ")
    try:
        with open(File,"r")as file:
            lines=file.readlines()
            found=False
        with open(File,"w")as file:
            for line in lines:
                data= decode_data(line.strip())
                old_website, username, password =data.split("|")
                if old_website==website:
                    data= website +"|"+ username +"|"+ new_password
                    found = True
                    
                file.write(encode_data(data)+"/n")
        if found:
            print("password update successfully")
        else :
            print("website not found")
    except FileNotFoundError:
        print("No credentials found")
while True:
    print("OFFICIAL CREDENTIALS MANAGER")
    print("1. Add a credentials")
    print("2. view a credentials")
    print("3. update the credentials")
    print("4. Exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_credentials()
    elif choice=="2":
        view_credentials()
    elif choice=="3":
        update_password()
    elif choice=="4":
        print("thank you!!")
        break
    else:
        print("invalid choice")

        
