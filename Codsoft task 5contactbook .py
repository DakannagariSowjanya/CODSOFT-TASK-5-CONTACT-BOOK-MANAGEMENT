contacts = []
def add_contact():
    print("----ADD CONTACT---")
    name = input("Enter name:")
    phone= input("Enter phone number:")
    email = input("Enter email adress:")
    address = input("Enter adress:")
    contact ={
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
        }
    global contacts
    contacts = contacts+[contact]
    print("Contact Added Succesfully!")
def view_contact():
    print("----CONTACT LIST---")
    if len(contacts) == 0:
       print("NO CONTACT FOUND..")
    else:
        i =1
        for contact in contacts:
            print(f"contact {i}:")
            print(f"Name :{contact['name']}")
            print(f"Phone :{contact['phone']}")
            print(f"Email{contact['email']}")
            print(f"Address{contact['address']}")
            i+=1
        
def search_contact():
    print("---SEARCH CONTACT---")
    search_name = input("Enter the contact name to be searched : ").lower()
    found = False
    for contact in contacts:
        if search_name in contact["name"].lower():
            print("CONTACT FOUND")
            print(f"Name :{contact['name']}")
            print(f"Phone :{contact['phone']}")
            print(f"Email{contact['email']}")
            print(f"Adress{contact['address']}")
            found = True
            break
        if not found:
            print("NO CONTACT FOUND..")
def update_contact():
    print("---UPDATE CONTACT----")
    name = input("Enter the name of contact to update:").lower()
    for contact in contacts:
        if contact["name"].lower()== name:
            contact["phone"]= input("enter new phone number : ")
            contact["email"]= input("enter new email adress: ")
            contact["adress"]= input("enter new adress : ")
            print("CONTACT UPDATED SUCCESSFULLY!")
            return
    print("NO CONTACT FOUND")
def delete_contact():
    print("DELETE CONTACT")
    name = input("Enter contact to be deleted:").lower()
    for contact in contacts:
        if contact["name"].lower()== name:
           contacts.remove(contact)
           print("contact deleted ")
           return
    print("NO CONTACT FOUND..")
def main():
    while True:
        print("1.Add Contact")
        print("2.View Contact")
        print("3.Search Contact")
        print("4.Update contact")
        print("5.Delete Contact")
        print("6.exit")
        choice = input("choose an option:")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("good bye!....")
            break
        else:
            print("Invalid choice.please Enter a valid number from 1 to 6")
def contact():
    main()

contact()
    
    
        
            











            











            











            









