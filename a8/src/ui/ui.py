class Ui:
    def __init__(self, serv, pers):
        self.__activity = serv
        self.__person = pers

    def run(self):
        while True:
            print("1. Manage persons and activities")
            print("2. Add person to activity")
            print("3. Statistics")
            print("0. Exit")

            choice = int(input("Choose: "))
            if choice == 1:
                print("1. Add")
                print("2. Remove")
                print("3. Update")
                print("4. List")
                action = int(input("Choose: "))
                print("1. Person")
                print("2. Activity")
                obj = int(input("Choose: "))
                if obj == 1:
                    if action == 1:
                        pr_id = input("Person ID: ")
                        name = input("Name: ")
                        ph_num = input("Phone number: ")
                        self.__person.add_person(pr_id,name,ph_num)
                    elif action == 2:
                        pr_id = input("Person ID: ")
                        self.__person.remove_person(pr_id)
                    elif action == 3:
                        pr_id = input("Person ID: ")
                        name = input("Name: ")
                        ph_num = input("Phone number: ")
                        self.__person.update_person(pr_id, name, ph_num)
                    elif action == 4:
                        for person in self.__person.get_all_persons():
                            print(str(person) + '\n')
                    else:
                        print("Invalid input")
                elif obj == 2:
                    if action == 1:
                        date = input("Date: ")
                        time = input("Time: ")
                        desc = input("Description: ")
                        self.__activity.add_activity(date, time, desc)
                    elif action == 2:
                        ac_id = input("Activity id: ")
                        self.__activity.remove_activity(ac_id)
                    elif action == 3:
                        ac_id = input("Activity id: ")
                        date = input("Date: ")
                        time = input("Time: ")
                        desc = input("Description: ")
                        self.__activity.update_activity(ac_id, date, time, desc)
                    elif action == 4:
                        for activity in self.__activity.get_activities():
                            print(str(activity) + '\n')
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            elif choice == 2:
                ac_id = int(input("Activity ID: "))
                pr_id = int(input("Person ID: "))
                self.__activity.add_person_to_activity(ac_id, pr_id)
            elif choice == 3:
                print("1. Activities in a given date")
                print("2. Busiest days")
                print("3. Activities with a given person")
                stat = int(input("Choose: "))
                if stat == 1:
                    date = input("Date: ")
                    for activity in self.__activity.search_by_date(date):
                        print(str(activity) + '\n')
                elif stat == 2:
                    print(self.__activity.busiest_day())
                elif stat == 3:
                    person = input("Person: ")
                    print(self.__person.activities_with_person(person, self.__activity.get_activities()))
                else:
                    print("Invalid input")
            elif choice == 0:
                exit()
            else:
                print("Invalid input")