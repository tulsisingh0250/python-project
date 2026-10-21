import json
from cryptography.fernet import Fernet
VAULT_FILE="vault.json"
KEY_FILE="secret.key"
def load_key():
    try:
        with open(KEY_FILE,"rb")as file:
            return file.read()
    except FileNotFoundError:
        key=Fernet.generate_key()
        with open(KEY_FILE,"wb")as file:
            file.write(key)
            return key
key=load_key()
fernet=Fernet(key)
def load_notes():
    try:
        with open(VAULT_FILE,"r")as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def saves_notes(notes):
        with open(VAULT_FILE,"w")as file:
            json.dump(notes,file,indent=4)
def add_note():
    title=input("Enter note title:")
    content=input("Enter note content:")
    encrypted_content=fernet.encrypt(content.encode()).decode()
    notes=load_notes()
    notes.append({
        "title":title,
        "content":encrypted_content
    })
    saves_notes(notes)
    print("Note saved successfully!")
def list_notes():
    notes=load_notes()
    if not notes:
        print("No notes found")
        for i,note in enumerate(notes,start=1):
            print(i,"-",note["title"])
def view_notes():
    notes=load_notes()
    if not notes:
        print("No notes found")
        return
    list_notes()
    try:
        choice=int(input("Enter note number:"))
        if choice<1 or choice>len(notes):
            print("Invalid note number.")
            return
        note=notes[choice-1]
        decrypted_content=fernet.decrypt(note["content"].encode()).decode()
        print("/n Title:",note["title"])
        print("content:",decrypted_content)
    except ValueError:
        print("please enter a number.")
def search_notes():
    keyword=input("Enter keyword to search:").lower()
    notes=load_notes()
    found =False
    for note in notes:
        content=fernet.decrypt(note["content"].encode()).decode()
        if keyword in note["title"].lower() or keyword in content.lower():
            print("/n Title:",note["title"])
            print("Content:",content)
            found=True
            if not found:
                print("No matching notes found")
while True:
    print("/n---- OFFLINE NOTES LOCKER----")
    print("1. Add Note")
    print("2. List Notes")
    print("3. View Note")
    print("4. Search Notes")
    print("5. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_note()
    elif choice=="2":
        list_notes()
    elif choice=="3":
        view_notes()
    elif choice=="4":
        search_notes()
    elif choice=="5":
        print("Thank you!!")
    else:
        print("Invalid choice")

