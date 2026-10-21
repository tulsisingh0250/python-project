import random
import string
password=input("enter a password:")
if len(password)<8:
    print ("add aleast 8 character")
if not  any(ch.isupper() for ch in password):
    print("add aleast one uppercase")
if not any(ch.islower() for ch in password):
    print("add aleast one lowercase")
if not any(ch.isdigit() for ch in password):
    print("add aleast one digit")
special ="@#$&"
if not any(ch in special for ch in password):
    print("add aleast one special")
if (len(password)>=8 and
   any(ch.isupper() for ch in password)and
   any(ch.islower() for ch in password)and
   any(ch.isdigit() for ch in password)and
   any(ch in special for ch in password)):
    print("strong password")
else:
    strong_password= (
    random.choice ( string.ascii_uppercase)+
    random.choice(string.ascii_lowercase)+
    random.choice(string.digits )+
    random.choice(special)+
    ''.join(random.choices(string.ascii_letters + string.digits + special, k=4))
    )
    print("suggested strong password:",strong_password)

