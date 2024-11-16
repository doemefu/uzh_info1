# Calendar Event Management

This task focuses on designing and implementing a Calendar class that manages events.
You will practice object-oriented programming, time-based logic, and working with the Python standard library (stdlib),
specifically using the datetime module and the sorted() function to effectively manage events in the calendar.
The main focus is on implementing functionality for adding, deleting, and retrieving calendar events.

You are provided with the following method signatures for the Calendar class.
Your task is to complete the implementation according to the descriptions.
1. The **constructor** initializes the class. It should create an empty data structure to store events, and it should keep track of a unique, incrementing event ID.
2. `add_event(date_str, start_time, end_time, description)`: Adds a new event to the calendar. It takes the following parameters:
   - `date_str` (string): The date for the event in `YYYY-MM-DD` format.
   - `start_time` (string): The start time in `HH:MM` format.
   - `end_time` (string): The end time in `HH:MM` format.
   - `description` (string): The description of the event.

If the `start_time` is greater than or equal to `end_time`, the method should raise an `Exception`. To [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions), you simply execute the statement `raise Exception("your desired error message")`, providing an error message to the `Exception` constructor as a string.

Otherwise, assign a unique ID to the event and store it in the calendar data structure.
This ID should start at 1 and increase with each event entry that is being added.
Finally, the assigned ID for the added event gets returned.

3. `get_events(date_str)`: Gets the list of events for a given date. It takes one parameter:
   - `date_str` (string): The date in `YYYY-MM-DD` format.
   
   The method returns an empty list if no events are scheduled for the given date.
Otherwise, it returns a list of tuples, where each tuple contains: `(event_id, start_time, end_time, description)` of the events scheduled for the given date.
Make sure to format it accordingly based on this example: `(1, '21:00', '23:59', 'Sleep')`.
The list of events should be sorted by start_time.

4. `delete_event(event_id)`: Deletes an event from the calendar. It takes one parameter:
   - `event_id` (integer): The unique identifier of the event.
   
   The method raises an `Exception` if the event with the given `event_id` does not exist.
Otherwise, it removes the entry from the calendar data structure.
Finally, the deleted event tuple (event_id, start_time, end_time, description) gets returned.

You can find a usage example at the bottom of the script.py file.

**Note:** All state must be contained within the class. Do not store information
in global variables or in class variables. It has to be possible to use multiple
instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and
functions. Do not change these signatures or the automated grading will fail.

**Hint**: Use the [datetime module][python-datetime] from Python's standard library to work with dates and times for easy comparison and sorting.
You can initially focus on the classes `datetime.date` and `datetime.time`.
**Make sure to use the methods for parsing and formatting dates!**

**Hint**: Use Python's built-in [sorted()][python-sorted] function to order the events by their start_time before returning them.

[python-datetime]: https://docs.python.org/3/library/datetime.html 
[python-sorted]: https://docs.python.org/3/library/functions.html#sorted
