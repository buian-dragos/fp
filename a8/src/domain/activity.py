class Activity:
    def __init__(self, activity_id, date, time, description):
        self.__activity_id = activity_id
        self.__person_id = []
        self.__date = date
        self.__time = time
        self.__description = description

    def get_activity_id(self):
        return self.__activity_id

    def get_person_id(self):
        return self.__person_id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    """
    def __repr__(self):
        return f"Activity ID: {self.__activity_id}\nDate: {self.__date}\n" \
               f"Time: {self.__time}\nDescription: {self.__description}\nPerson ID(s): {self.__person_id} "
    """

    def __str__(self):
        return f"Activity ID: {self.__activity_id}\nDate: {self.__date}\n" \
               f"Time: {self.__time}\nDescription: {self.__description}\nPerson ID(s): {self.__person_id} "