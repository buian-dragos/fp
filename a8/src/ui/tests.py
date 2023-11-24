import unittest
from src.services.service_activity import ServiceActivity
from src.services.service_person import PersonService
from src.repository.person_repository import PersonRepository
from src.repository.activity_repository import ActivityRepository
from src.ui.start import add_activities
from src.ui.start import add_persons


class Test(unittest.TestCase):
    def test_activity_with_person(self):
        pr_repo = PersonRepository()
        ac_repo = ActivityRepository()
        person = PersonService(pr_repo)
        activity = ServiceActivity(ac_repo)

        add_persons(pr_repo)
        add_activities(ac_repo)

        activities_mara = person.activities_with_person("mara",ac_repo.get_activities())
        self.assertEqual(len(activities_mara),148)

    def test_statistics(self):
        pr_repo = PersonRepository()
        ac_repo = ActivityRepository()
        person = PersonService(pr_repo)
        activity = ServiceActivity(ac_repo)

        add_persons(pr_repo)
        add_activities(ac_repo)

        busy = activity.busiest_day()
        self.assertEqual(len(busy),30)

    def test_activities(self):
        pr_repo = PersonRepository()
        ac_repo = ActivityRepository()
        person = PersonService(pr_repo)
        activity = ServiceActivity(ac_repo)

        add_persons(pr_repo)
        add_activities(ac_repo)


        activity.add_activity("13.02","12","pizza")

        list1 = activity.search_by_date("13.02")
        self.assertEqual(len(list1),5)

        activity.update_activity(3,"14.02","11","sleep")

        list2 = activity.search_by_time("11")
        self.assertEqual(len(list2), 1)

        activity.add_person_to_activity(10,3)

        list3 = activity.search_by_description("sleep")
        self.assertEqual(len(list3), 1)

        activity.remove_person_from_activity(10,3)

        ac_repo.get_activity_by_id(11)

        activity.remove_activity(11)

        all_activities = activity.get_activities()
        self.assertEqual(len(all_activities),10)

    def test_persons(self):
        pr_repo = PersonRepository()
        ac_repo = ActivityRepository()
        person = PersonService(pr_repo)
        activity = ServiceActivity(ac_repo)

        add_persons(pr_repo)
        add_activities(ac_repo)

        person.add_person(11,"Ion","077777777")

        all_persons = person.get_all_persons()
        self.assertEqual(len(all_persons),11)

        person.get_person_by_id(11)

        person.update_person(11,"Vasile","77")

        person.remove_person(11)

        all_persons = person.get_all_persons()
        self.assertEqual(len(all_persons), 10)

