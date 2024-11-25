#!/usr/bin/env python3
from unittest import TestCase
from task.script import Calendar


class PublicTestSuite(TestCase):

    def test_example(self):
        cal = Calendar()
        # add events to the calendar
        event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
        event_id_sleep = cal.add_event("2024-12-24", "20:00", "23:59", "Sleep")
        # make sure the calendar instance contains two entries
        self.assertEqual(2, len(cal.get_events("2024-12-24")))
        # delete the first entry
        cal.delete_event(event_id_dinner)
        # make sure the calendar instance now contains only one entry
        self.assertEqual(1, len(cal.get_events("2024-12-24")))
        # delete the first entry
        cal.delete_event(event_id_sleep)
        # make sure the calendar instance is now empty
        self.assertEqual(0, len(cal.get_events("2024-12-24")))

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
