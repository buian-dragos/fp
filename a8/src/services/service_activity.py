from src.domain.activity import Activity


class ServiceActivity:
    def __init__(self, repo):
        self.__repo = repo

    def add_activity(self, date, time, description):
        activity = Activity(len(self.__repo.get_activities()) + 1, date, time, description)
        self.__repo.add_activity(activity)

    def remove_activity(self, activity_id):
        self.__repo.remove_activity_by_id(activity_id)

    def update_activity(self, activity_id, new_date, new_time, new_description):
        self.__repo.update_activity(activity_id, new_date, new_time, new_description)

    def add_person_to_activity(self, activity_id, person_id):
        self.__repo.add_person_to_activity(activity_id, person_id)

    def remove_person_from_activity(self, activity_id, person_id):
        self.__repo.remove_person_from_activity(activity_id, person_id)

    def get_activities(self):
        return self.__repo.get_activities()

    def search_by_date(self,date):
        ac_list = []
        for activity in self.__repo.get_activities():
            if activity.get_date() == date:
                ac_list.append(activity)
        self.sort_by_time(ac_list)
        return ac_list

    def sort_by_time(self, ac_list: list):
        for i in range(len(ac_list)-1):
            for j in range(i+1, len(ac_list)):
                if ac_list[i].get_time() > ac_list[j].get_time():
                    ac_list[i], ac_list[j] = ac_list[j], ac_list[i]


    def search_by_time(self,time):
        ac_list = []
        for activity in self.__repo.get_activities():
            if activity.get_time() == time:
                ac_list.append(activity)
        return ac_list

    def search_by_description(self,desc: str):
        ac_list = []
        for activity in self.__repo.get_activities():
            if desc.lower() in activity.get_description().lower():
                ac_list.append(activity)
        return ac_list

    def get_dates(self):
        date_list = []
        for activity in self.__repo.get_activities():
            if activity.get_date() not in date_list:
                date_list.append(activity.get_date())
        return date_list

    def busiest_day(self):
        busy_days = []
        for date in self.get_dates():
            busy_days.append([date,len(self.search_by_date(date))])
        for i in range(len(busy_days)-1):
            for j in range(i+1, len(busy_days)):
                if busy_days[i][1] < busy_days[j][1]:
                    busy_days[i], busy_days[j] = busy_days[j], busy_days[i]
        string = ""
        for i in range(len(busy_days)):
            string += f"{busy_days[i][0]}\n"
        return string


