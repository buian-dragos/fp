#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#
import ui
import functions as fc
import copy
def test():
    apartments = fc.create_apartments()
    undo_list = []
    initial = copy.deepcopy(apartments)
    try:
        apartments, undo_list = fc.add_transaction(apartments,undo_list,"7","gas","44")
        apartments, undo_list = fc.remove_apartment(apartments,undo_list,"4",0) #sterge la ap 4
        assert fc.total_expense(apartments,3) == 0
        apartments, undo_list = fc.remove_apartment(apartments,undo_list, "8","10") #sterge 8,9,10
        assert fc.total_expense(apartments,7) == 0
        assert fc.total_expense(apartments, 8) == 0
        assert fc.total_expense(apartments, 9) == 0
        apartments, undo_list = fc.remove_type(apartments,undo_list,"gas") #sterge toate gas
        for i in range(4):
            apartments, undo_list = fc.undo(apartments,undo_list)

        assert apartments == initial

        apartments, undo_list = fc.replace(apartments,undo_list,"7","water","42")
        apartments, undo_list = fc.filter_value(apartments,undo_list,"300")
        apartments, filter = fc.filter_type(apartments,undo_list,"other")
        for i in range(3):
            apartments, undo_list = fc.undo(apartments,undo_list)
        assert apartments == initial

    except ValueError as error:
        print(str(error))
if __name__ == '__main__':
    #ui.start_program()
    test()

