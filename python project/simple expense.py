import csv
File="expenses.csv"
def load_expense():
    expenses=[]
    try:
        with open(File,"r")as file:
          reader=csv.reader(file)
          for row in reader:
           expenses.append({
               "Name": row[0],
               "Amount":int(row[1]),
               "category":row[2]
         })
           return expenses
    except FileNotFoundError:
        return[]
def save_expense(expenses):
    with open(File,"w")as file:
        writer=csv.writer(file)
        for expense in expenses:
            writer.writerow([
                expense["Name"],
                expense["Amount"],
                expense["category"]
            ])
expenses=load_expense()
while True:
    print("simple expense")
    print("1. Add a expense")
    print("2. view a expense")
    print("3. Total expense")
    print("4. Reduce expense")
    print("5. exit")
    choice=input("enter your choice (1/2/3/4/5):")
    if choice=="1":
        name=input("enter your expenses name:")
        amount=int(input("enter your amount:"))
        category=input("enter your category:")
        expense={
            "Name":name,
            "Amount":amount,
            "category":category
        }
        expenses.append(expense)
        save_expense(expenses)
        print("expense added successfully")
    elif choice=="2":
        if len(expenses)==0:
            print("No expenese")
        else:
            print("Name\tAmount\tcategory")
            for expense in expenses:
                print(expense["Name"],"\t",
                      expense["Amount"],"\t",
                      expense["category"])
    elif choice=="3":
        total=0
        for expense in expenses:
            total=total+expense["Amount"]
        print("Total expense:",total)
    elif choice=="4":
        name = input("Enter expense name to remove: ")

        for expense in expenses:
             if expense["Name"]==name:
                 expenses.remove(expense)
                 save_expense(expenses)
                 print("Expense removed successfully!")
                 break  
    elif choice=="5":
        print("thank you!!!")
    else:
        print("invalid choice")




