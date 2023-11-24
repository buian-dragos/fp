from src.domain.person import Person


class PersonService:
    def __init__(self, person_repository):
        self.__person_repository = person_repository

    def add_person(self, person_id, name, phone_number):
        person = Person(person_id, name, phone_number)
        self.__person_repository.add(person)

    def remove_person(self, person_id):
        self.__person_repository.remove(person_id)

    def update_person(self, person_id, new_name, new_phone_number):
        self.__person_repository.update(person_id, new_name, new_phone_number)

    def get_all_persons(self):
        return self.__person_repository.get_all()

    def get_person_by_id(self, person_id):
        return self.__person_repository.get_person_by_id(person_id)

    def search_persons(self, search: str):
        persons = self.__person_repository.get_all()
        persons_found = []
        for person in persons:
            if search.lower() in person.name.lower():
                persons_found.append(person)
            elif search.lower() in person.phone_number.lower():
                persons_found.append(person)
        return persons_found

    def activities_with_person(self, person, activities: list):
        string = ""
        persons_found = self.search_persons(person)
        for i in range(len(persons_found)):
            string += str(self.__person_repository.get_person_by_id(persons_found[i].get_person_id())) + "\n"
            for activity in activities:
                if persons_found[i].get_person_id() in activity.get_person_id():
                    string += str(activity) + "\n\n"

        return string
