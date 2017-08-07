"""Assignment calendar helpers."""
from briefy.choreographer.utils.calendar.schemas import AssignmentCalendarEvent
from briefy.choreographer.utils.calendar.schemas import AssignmentCalendarEventSchema
from briefy.common.db import datetime_utcnow
from datetime import timedelta
from icalendar import Alarm
from icalendar import Calendar
from icalendar import Event
from icalendar import vCalAddress
from icalendar import vText

import base64
import colander
import typing as t


def _calendar_envelope() -> Calendar:
    """Return the Calendar envelope to be used.

    :return: An icalendar.Calendar object to envelope the event.
    """
    cal = Calendar()
    cal.add('prodid', '-//Briefy')
    cal.add('version', '2.0')
    return cal


def _get_alarm(hours: int =1) -> Alarm:
    """Return the alarm object.

    :param hours: Number of hours before the event to trigger the alarm.
    :return: An instance of icalendar.Alarm.
    """
    seconds = hours * 3600 * -1
    alarm = Alarm()
    alarm_time = timedelta(seconds=-seconds)
    alarm.add('trigger', alarm_time)
    alarm.add('action', 'DISPLAY')
    alarm.add('description', 'Reminder')
    return alarm


def _get_organizer() -> vCalAddress:
    """Return information about the Organizer of this event.

    :return: An instance of icalendar.vCalAddress with the organizer information.
    """
    organizer = vCalAddress('site@briefy.co')
    organizer.params['cn'] = vText('Briefy')
    return organizer


def _get_attendees(data: AssignmentCalendarEvent) -> t.Sequence[vCalAddress]:
    """Extract information about the contact person for the event.

    :param data: An instance of AssignmentCalendarEvent.
    :return: A sequence icalendar.vCalAddress attendees for the event.
    """
    attendees = []
    # Contact person at the location
    attendee = vCalAddress(data.contact_email)
    attendee.params['cn'] = vText(data.contact_name)
    attendees.append(attendee)
    return attendees


def _get_event(data: AssignmentCalendarEvent) -> Event:
    """Generate icalendar.Event from an AssignmentCalendarEvent instance.

    :param data: An instance of AssignmentCalendarEvent.
    :return: An icalendar.Event object from the AssignmentCalendarEvent.
    """
    now = datetime_utcnow()
    event = Event()
    event['uid'] = data.id
    event.add('status', data.status)
    event.add('summary', data.summary)
    event.add('description', data.description)
    event.add('location', data.address)
    event.add('dtstart', data.start)
    event.add('dtstamp', now)
    event.add('dtend', data.end)
    event.add('url', data.url)
    event.add('organizer', _get_organizer())
    event.add('geo', data.geo)
    attendees = _get_attendees(data)
    for attendee in attendees:
        event.add('attendee', attendee)
    event.add_component(_get_alarm(1))
    return event


def _generate_calendar(data: AssignmentCalendarEvent) -> Calendar:
    """Generate a icalendar.Calendar object from an AssignmentCalendarEvent.

    :param data: An instance of AssignmentCalendarEvent
    :return: icalendar.Calendar object.
    """
    cal = _calendar_envelope()
    event = _get_event(data)
    cal.add_component(event)
    return cal


def assignment_to_ical(payload: dict) -> t.ByteString:
    """Generate an iCal file from an Assigment Payload.

    :param payload: Assignment.to_dict payload, received from the queue event.
    :return: ICalendar file, encoded in utf-8
    """
    schema = AssignmentCalendarEventSchema()
    try:
        payload = schema.deserialize(payload)
    except colander.Invalid:
        ics = b''
    else:
        data = AssignmentCalendarEvent(**payload)
        calendar = _generate_calendar(data)
        ics = calendar.to_ical()
    return ics


def assignment_to_ical_attachment(payload: dict) -> t.Optional[dict]:
    """Generate an iCal file from an Assignment Payload.

    :param payload: Assignment.to_dict payload, received from the queue event.
    :return: Dictionary with type, name and content.
    """
    attachment = None
    ics = assignment_to_ical(payload)
    if ics:
        slug = payload['slug']
        encoded = base64.b64encode(ics)
        attachment = {
            'type': 'text/calendar',
            'name': f'{slug}.ics',
            'content': encoded.decode('utf-8')
        }
    return attachment
