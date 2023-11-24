from src.services.service_activity import ServiceActivity
from src.services.service_person import PersonService
from src.repository.activity_repository import ActivityRepository
from src.repository.person_repository import PersonRepository
from src.domain.activity import Activity
from src.domain.person import Person
# from src.ui.tests import Tests
from src.ui.ui import Ui

def add_activities(ac_repo):
    ac_repo.add_activity(Activity(1, "13.02", "13.00", "pizza"))
    ac_repo.add_person_to_activity(1, 7)
    ac_repo.add_person_to_activity(1, 6)
    ac_repo.add_activity(Activity(2, "13.02", "12.00", "fotbal"))
    ac_repo.add_person_to_activity(2, 3)
    ac_repo.add_person_to_activity(2, 4)
    ac_repo.add_person_to_activity(2, 1)
    ac_repo.add_activity(Activity(3, "13.02", "11.00", "fotbal"))
    ac_repo.add_person_to_activity(3, 7)
    ac_repo.add_person_to_activity(3, 5)
    ac_repo.add_person_to_activity(3, 8)
    ac_repo.add_activity(Activity(4, "13.02", "10.00", "fotbal"))
    ac_repo.add_person_to_activity(4, 9)
    ac_repo.add_person_to_activity(4, 10)
    ac_repo.add_person_to_activity(4, 7)
    ac_repo.add_person_to_activity(4, 2)
    ac_repo.add_activity(Activity(5, "11.05", "13.00", "film"))
    ac_repo.add_person_to_activity(5, 7)
    ac_repo.add_activity(Activity(6, "22.07", "7.00", "inot"))
    ac_repo.add_person_to_activity(6, 3)
    ac_repo.add_person_to_activity(6, 6)
    ac_repo.add_activity(Activity(7, "11.05", "8.00", "inot"))
    ac_repo.add_person_to_activity(7, 4)
    ac_repo.add_person_to_activity(7, 5)
    ac_repo.add_activity(Activity(8, "10.01", "19.00", "bere"))
    ac_repo.add_person_to_activity(8, 7)
    ac_repo.add_person_to_activity(8, 1)
    ac_repo.add_person_to_activity(8, 4)
    ac_repo.add_activity(Activity(9, "31.01", "18.00", "party"))
    ac_repo.add_person_to_activity(9, 5)
    ac_repo.add_person_to_activity(9, 6)
    ac_repo.add_activity(Activity(10, "10.01", "13.00", "alergat"))
    ac_repo.add_person_to_activity(10, 2)
    ac_repo.add_person_to_activity(10, 4)
    ac_repo.add_person_to_activity(10, 7)

def add_persons(pr_repo):
    pr_repo.add(Person(1, "Ion Besoiu", "0727874412"))
    pr_repo.add(Person(2, "Ion Vasile", "0733374412"))
    pr_repo.add(Person(3, "Mihai Pop", "0721877472"))
    pr_repo.add(Person(4, "Andrei Popescu", "0727554419"))
    pr_repo.add(Person(5, "Rares Teposu", "0755874413"))
    pr_repo.add(Person(6, "Paul Valase", "0766874417"))
    pr_repo.add(Person(7, "Carmen Popescu", "0722874455"))
    pr_repo.add(Person(8, "Andreea Pop", "0727874412"))
    pr_repo.add(Person(9, "Alexia Zaharie", "0722274412"))
    pr_repo.add(Person(10, "Mara Vilau", "0727822787"))

if __name__ == '__main__':
    ac_repo = ActivityRepository()
    pr_repo = PersonRepository()
    add_activities(ac_repo)
    add_persons(pr_repo)
    service = ServiceActivity(ac_repo)
    person = PersonService(pr_repo)
    ui = Ui(service,person)
    ui.run()
