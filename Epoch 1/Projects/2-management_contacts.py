#----------------------------------------------------------
#           MANAGEMENT CONTACT
# ---------------------------------------------------------

contacts = {}   # Empty Dict --> Name & Phone Number

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    if name in contacts:
        print("This Contact was Invaild!")
    else:
        contacts[name] = phone
        print(f"'{name}' Added. ")

def show_all():
    if not contacts:
        print("The notebook is empty")
        return
    print("\n--- CONTACT LIST ---")
    for i, (name, phone) in enumerate(contacts.items(), 1):
        print(f"{i}. {name}: {phone}")
    print(f"Total Count: {len(contacts)}")

def search():
    name = input("Name for: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(" Not Founded.")

def delete():
    name = input("  Name for delete: ").strip()
    if contacts.pop(name, None):
        print(f"'{name}'  Deleted.")
    else:
        print("Not Found. ")

while True:
    print("\n1. Add  2. Show  3. Search  4. Remove  5. Exit")
    choice = input("Choice: ")
    if   choice == "1": add_contact()
    elif choice == "2": show_all()
    elif choice == "3": search()
    elif choice == "4": delete()
    elif choice == "5": break
    else: print("Invalid option")