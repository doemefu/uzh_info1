#!/usr/bin/env python3
import datetime


# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the List of parameters.
# You may introduce private/protected utility methods though.
class Calendar:

    def __init__(self):
        self.event_id = 0
        self.eventStorage = dict()

    def add_event(self, date_str, start_time, end_time, description):
        if end_time <= start_time:
            raise Exception("end_time <= start_time")

        myDate = datetime.date(int(date_str[0:4]), int(date_str[5:7]), int(date_str[8:10]))
        sTime = datetime.time(int(start_time[0:2]), int(start_time[3:5]))
        eTime = datetime.time(int(end_time[0:2]), int(end_time[3:5]))
        self.event_id += 1
        self.eventStorage[self.event_id] = [myDate, sTime, eTime, description]

        return self.event_id

    def get_events(self, date_str):
        returnList = []
        for myEvent in self.eventStorage.items():
            myDate = datetime.date(int(date_str[0:4]), int(date_str[5:7]), int(date_str[8:10]))

            if myEvent[1][0] == myDate:
                returnList.append((myEvent[0], datetime.time.strftime(myEvent[1][1], "%H:%M"),
                                   datetime.time.strftime(myEvent[1][2], "%H:%M"), myEvent[1][3]))

        return sorted(returnList, key=lambda x: x[1])

    def delete_event(self, event_id):
        if event_id not in self.eventStorage:
            raise Exception("event_id not in eventStorage")

        deletedTuple = self.eventStorage[event_id]

        del self.eventStorage[event_id]

        return deletedTuple


# You can play around with your implementation in the following body.
# The contained statements will be ignored while evaluating your solution.
if __name__ == "__main__":
    cal = Calendar()
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))
