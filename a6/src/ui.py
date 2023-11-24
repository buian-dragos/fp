#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import functions as fc

def start_program():
    apartments = fc.create_apartments()
    undo_list = []
    while True:
        user_input = input(">")
        command_list = []
        command_list = user_input.split(" ")
        if command_list[0] == "exit":
            exit()
        elif command_list[0] == "add":
            if len(command_list)==4:
                try:
                    apartments, undo_list = fc.add_transaction(apartments,undo_list,command_list[1],command_list[2],command_list[3])
                except ValueError as error:
                    print(str(error))
            else:
                print("Invalid parameters for command 'add'")
        elif command_list[0]=="remove":
            if len(command_list)==4:
                try:
                    apartments, undo_list = fc.remove_apartment(apartments,undo_list,command_list[1],command_list[3])
                except ValueError as error:
                    print(str(error))
            elif len(command_list)==2:
                if command_list[1].isdigit():
                    try:
                        apartments, undo_list = fc.remove_apartment(apartments,undo_list,command_list[1],0)
                    except ValueError as error:
                        print(str(error))
                else:
                    try:
                        apartments, undo_list = fc.remove_type(apartments,undo_list,command_list[1])
                    except ValueError as error:
                        print(str(error))
            else:
                print("Invalid parameters for command 'remove'")
        elif command_list[0] == "replace":
            if len(command_list)==5:
                try:
                    apartments, undo_list = fc.replace(apartments,undo_list,command_list[1],command_list[2],command_list[4])
                except ValueError as error:
                    print(str(error))
            else:
                print("Invalid parameters for command 'replace'")
        elif command_list[0]=="list":
            if len(command_list)==1:
                print(fc.list(apartments))
            elif len(command_list)==2:
                try:
                    print(fc.list_apartment(apartments,command_list[1]))
                except ValueError as error:
                    print(str(error))
            elif len(command_list)==3:
                try:
                    print(fc.list_amount(apartments,command_list[1],command_list[2]))
                except ValueError as error:
                    print(str(error))
            else:
                print("Invalid parameters for command 'list'")
        elif command_list[0]=="filter":
            if command_list[1].isdigit():
                apartments, undo_list = fc.filter_value(apartments,undo_list,command_list[1])
            else:
                try:
                    apartments, undo_list = fc.filter_type(apartments,undo_list,command_list[1])
                except ValueError as error:
                    print(str(error))
        elif command_list[0]=="undo":
            apartments, undo_list = fc.undo(apartments, undo_list)
