# Pretify console output by highlighting using bold fond
BOLD_FONT = "\033[1m"
REGULAR_FONT = "\033[0m"


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"Please type: {BOLD_FONT}{func.__name__.rstrip('_contact')} username phone{REGULAR_FONT}."
        except IndexError:
            return f"User name missing, type: {BOLD_FONT}phone username{REGULAR_FONT}."
        except KeyError:
            return "Contact not found. Please add contact first."

    return wrapper


def parser_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Empty command."

    return wrapper


@parser_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        res = "Contact changed."
    else:
        res = "Contact not found. Please add contact first."
    return res


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    res = str()
    for k, v in contacts.items():
        res = res + f"{k}: {v},\n"
    res = res.rstrip(",\n")
    return res


def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Use: hello, add, change, phone, all or exit.")


if __name__ == "__main__":
    main()
