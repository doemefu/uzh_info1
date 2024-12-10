#!/usr/bin/env python3
from datetime import datetime


class Calendar:

    def __init__(self):
        self._events = {}
        self._event_id_counter = 1

    def _get_next_event_id(self):
        event_id = self._event_id_counter
        self._event_id_counter += 1
        return event_id

    def add_event(self, date_str, start_time, end_time, description):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start = datetime.strptime(start_time, "%H:%M").time()
        end = datetime.strptime(end_time, "%H:%M").time()

        if start >= end:
            raise Exception("Start time must be before end time!")

        if date not in self._events:
            self._events[date] = []

        event_id = self._get_next_event_id()
        self._events[date].append((event_id, start, end, description))
        return event_id

    def get_events(self, date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        if date not in self._events:
            return []

        events = sorted(self._events[date], key=lambda x: x[1])
        return [(event_id, start.strftime('%H:%M'), end.strftime('%H:%M'), description) for
                event_id, start, end, description in events]

    def delete_event(self, event_id):
        for event_date, event_list in self._events.items():
            for event in event_list:
                if event[0] == event_id:
                    event_list.remove(event)
                    if not event_list:
                        del self._events[event_date]
                    return event
        raise Exception(f"Event with ID {event_id} not found!")
