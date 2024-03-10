from src.classes.record import Record
from src.classes.addressBook import AddressBook
from src.tools.handlers import add_birthday, add_contact, birthdays, change_contact, parse_input, phone, print_contacts, show_birthday


def bot():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
            print("How can I help you?")
        elif command == "change":
            print(change_contact(args, book))
            print("How can I help you?")
        elif command == "phone":
            print(phone(args, book))
            print("How can I help you?")
        elif command == "all":
            print_contacts(book)
            print("How can I help you?")
        elif command == "add-birthday":
            print(add_birthday(args, book))
            print("How can I help you?")
        elif command == "show-birthday":
            print(show_birthday(args, book))
            print("How can I help you?")
        elif command == "birthdays":
            birthdays(book)
            print("How can I help you?")
        else:
            print("Invalid command.")