# Project Overview:
# Create a simple phone book manager where users can add, view, update, and delete contacts
# in a file named `phone_book.py`.

# Requirements:
# 1. Data Storage: Use a list of dictionaries to store contact information. Each contact should have the following attributes:
# Name (string)
# Phone Number (string)
# Favorite (boolean)
# 2. Functions/Actions:
# add_contact(): Add a new contact to the phone book.
# view_contacts(): Display all the contacts in the phone book.
# update_contact(phone_number): Update the information of a contact given their phone number.
# delete_contact(phone_number): Remove a contact from the phone book using their phone
# number.
# search_contact(name): Search for a contact by their exact name.
# mark_favorite(phone_number): Mark a contact as a favorite.
# unmark_favorite(phone_number): Unmark a contact as a favorite.
#3.User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.
def phonebook():

    data_storage = [
      {"name": "Kariola Johnson", "phone": "08034917916", "favorite": True},
      {"name": "Bola Ahmed Tinubu", "phone": "09034987126", "favorite": False},
      {"name": "Kariola John", "phone": "08084931407", "favorite": True}
    ]
    
    def print_menu():
      print("\nPhone Book Manager")
      print("1. Add Contact")
      print("2. View Contacts")
      print("3. Update Contact")
      print("4. Delete Contact")
      print("5. Search Contact (by exact name)")
      print("6. Mark Favorite")
      print("7. Unmark Favorite")
      print("8. Exit")   
      
    def add_contact():
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        contact = {"name": name, "phone": phone, "favorite": False}
        data_storage.append(contact)
        print(f"✅ {name} added successfully!")

    def view_contacts():
        if not data_storage:
            print("No contacts found.")
        else:
            for i, contact in enumerate(data_storage, start=1):
                fav = "⭐" if contact["favorite"] else ""
                print(f"{i}. {contact['name']} - {contact['phone']} {fav}")    
    def update_contact():
        if  data_storage:
          phone = input("Enter the phone number of the contact to update: ").strip()
          for contact in data_storage:
              if contact["phone"] == phone:
                  print(f"found: {contact['name']} - {contact['phone']} ")
                  new_name = input("Enter new name (leave blank to keep current): ").strip()
                  new_phone = input("Enter new phone (leave blank to keep current): ").strip()

                  if new_name:
                      contact["name"] = new_name
                  if new_phone:
                      contact["phone"] = new_phone
                      print(" Contact updated successfully!")
                      return   

          else:
             print("Contact not found in the phonebook")      



    def delete_contact():
        name = input("Enter the name to delete: ").strip()
        matches = [char for char in data_storage if char["name"].lower() == name.lower()]

        if not matches:
            print("❌ Contact not found")
        elif len(matches) == 1:
            data_storage.remove(matches[0])
            print(f" {matches[0]['name']} deleted successfully!")
        else:
            print("Multiple matches found:")
            for i, char in enumerate(matches, start=1):
                print(f"{i}. {char['name']} - {char['phone']}")
            choice = int(input("Enter the number to delete: "))
            data_storage.remove(matches[choice - 1])
            print("✅ Deleted successfully!")

    def search_contact():
          name = input("Enter the name to search: ").strip().lower()
          found = False

          for contact in data_storage:
              if contact["name"].lower() == name:
                  fav = "⭐" if contact["favorite"] else ""
                  print(f"✅ Found: {contact['name']} - {contact['phone']} {fav}")
                  found = True

          if not found:
              print(" Contact not found")

    def mark_favorite():
          phone = input("Enter the phone number to mark as favorite: ").strip()
          for contact in data_storage:
              if contact["phone"] == phone:
                  contact["favorite"] = True
                  print(f"⭐ {contact['name']} marked as favorite!")
                  return
          print("❌ Contact not found")


    def unmark_favorite():
          phone = input("Enter the phone number to mark as favorite: ").strip()
          for contact in data_storage:
              if contact["phone"] == phone:
                  contact["favorite"] = False
                  print(f"⭐ {contact['name']} removed as favorite!")
                  return
          print("❌ Contact not found")


  
    def main():
      while True:
          print_menu()  
          choice = input("Choose an option (1-8): ").strip()

          if choice == "1":
              add_contact()
          elif choice == "2":
              view_contacts()
          elif choice == "3":
              update_contact()
          elif choice == "4":
              delete_contact()
          elif choice == "5":
              search_contact()
          elif choice == "6":
              mark_favorite()
          elif choice == "7":
              unmark_favorite()
          elif choice == "8":
              print("Exiting Phone Book Manager. Goodbye!")
              break
          else:
              print("Invalid choice. Please try again.")        



    main()
phonebook()

              
                 

        