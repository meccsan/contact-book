import json
import os

FILE_NAME = "contact-data.json"

# make sure data properly loads
def load_contacts():

    if not os.path.exists(FILE_NAME):
        return []
    
    # open el data
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f: # push out data to json file
        json.dump(contacts, f, indent=4) # save with pretty formatting

def create_contact():
    name = input("Please insert contact name: ")
    phone_number = input("Please insert contact phone number: ")
    email = input("Please insert contact email: ")
    other = input("Please insert other forms of contact: ")
    notes = input("Please insert notes about contact: ")

    # this the shit that gets saved
    contact = {
        "contact_name": name,
        "contact_phone_number": phone_number,
        "contact_email": email,
        "contact_other": other,
        "contact_notes": notes
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)

    print("Contact saved.")

def display_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.") # where da fuk yo contact at?
        return

    for contact in contacts:
        print("══════════════")
        print("Name:", contact["contact_name"])
        print("Phone:", contact["contact_phone_number"])
        print("Email:", contact["contact_email"])

def main():
    while True:
        usr_decision = input(
            "What would you like to do (h for help): "
        )

        if usr_decision == "h":
            print("Commands:")
            print("h = help")
            print("c = create contact")
            print("a = display contacts")
            print("q = quit")

        elif usr_decision == "c":
            create_contact()

        elif usr_decision == "a":
            display_contacts()

        elif usr_decision == "q":
            break

        else:
            print("Illegal command.")

if __name__ == "__main__":
    main()