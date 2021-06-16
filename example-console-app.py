from domain.iota_easy_wallet import create_account, restore_account, login, AccountInterface
import getpass

def cui_login() -> None:
    username = input("username: ")
    manage_wallet(login(username, getpass.getpass("password: ")))

def cui_create_account() -> None:
    username = input("username: ")
    manage_wallet(create_account(username, getpass.getpass("password: ")))

def cui_restore_account() -> None:
    file_name = input("file name: ")
    username = input("username: ")
    manage_wallet(restore_account(file_name, username, getpass.getpass("password: ")))

def manage_wallet(interface: AccountInterface) -> None:
    secondary_options = [
        { "description": "balance", "handler": interface.balance},
    ]
    quit_index = len(secondary_options)+1
    while True:
        print("What do you want to do? (type number)")
        for index, elem in enumerate(secondary_options):
            print("{}) {}".format(index+1, elem["description"]))
        print("{}) {}".format(quit_index, "quit")) 
        should_quit = handle_choice(input(), secondary_options, quit_index)
        if should_quit:
            print("going back to primary options...\n")
            break

def handle_choice(choice: str, options, quit_index: int) -> bool:
    if not choice.isnumeric():
        print("please enter a valid option:")
    else:
        numbered_choice = int(choice)
        if numbered_choice == 0 or numbered_choice > quit_index:
            print("please enter a valid option:")
        elif numbered_choice == quit_index:
            return True
        else:
            handle_choice_by_valid_number(numbered_choice, options)
    return False

def handle_choice_by_valid_number(choice: int, options) -> None:
    options[choice-1]["handler"]()
    
primary_options = [
    { "description": "login", "handler": cui_login},
    { "description": "create new wallet", "handler": cui_create_account},
    { "description": "restore wallet from stronghold", "handler": cui_restore_account},
]

quit_index = len(primary_options)+1
while True:
    print("What do you want to do? (type number)")
    for index, elem in enumerate(primary_options):
        print("{}) {}".format(index+1, elem["description"]))
    print("{}) {}".format(quit_index, "quit")) 
    should_quit = handle_choice(input(), primary_options, quit_index)
    if should_quit:
        print("stopping app...\n")
        break
    