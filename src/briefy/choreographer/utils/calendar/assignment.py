"""Assignment calendar helpers."""
from briefy.choreographer.utils.calendar.schemas import AssignmentEvent
from briefy.choreographer.utils.calendar.schemas import AssignmentEventSchema
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
    """Return the Calendar envelope to be used."""
    cal = Calendar()
    cal.add('prodid', '-//Briefy')
    cal.add('version', '2.0')
    return cal


def _get_alarm(hours: int =1) -> Alarm:
    """Return the alarm object."""
    seconds = hours * 3600 * -1
    alarm = Alarm()
    alarm_time = timedelta(seconds=-seconds)
    alarm.add('trigger', alarm_time)
    alarm.add('action', 'DISPLAY')
    alarm.add('description', 'Reminder')
    return alarm


def _get_organizer() -> vCalAddress:
    """Return information about the Event Organizer."""
    organizer = vCalAddress('site@briefy.co')
    organizer.params['cn'] = vText('Briefy')
    return organizer


def _get_attendees(data: AssignmentEvent) -> t.Sequence[vCalAddress]:
    """Return information about the Event Organizer."""
    attendees = []
    # Contact person at the location
    attendee = vCalAddress(data.contact_email)
    attendee.params['cn'] = vText(data.contact_name)
    attendees.append(attendee)
    return attendees


def _get_event(data: AssignmentEvent) -> Event:
    """Generate event information."""
    now = datetime_utcnow()
    event = Event()
    event['uid'] = data.id
    event.add('status', data.status)
    event.add('summary', f'Shooting for Briefy Assignment {data.slug}')
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


def _generate_calendar(data: AssignmentEvent) -> Calendar:
    """Generate a Calendar object from an AssignmentEvent."""
    cal = _calendar_envelope()
    event = _get_event(data)
    cal.add_component(event)
    return cal


def assignment_to_ical(payload: dict) -> t.ByteString:
    """Generate an iCal file from an Assigment Payload.

    :param payload: Assignment payload, received from the event.
    :return: ICalendar file, encoded in utf-8
    """
    schema = AssignmentEventSchema()
    try:
        payload = schema.deserialize(payload)
    except colander.Invalid:
        ics = b''
    else:
        data = AssignmentEvent(**payload)
        calendar = _generate_calendar(data)
        ics = calendar.to_ical()
    return ics


def assignment_to_ical_attachment(payload: dict) -> t.Optional[dict]:
    """Generate an iCal file from an Assigment Payload.

    :param payload: Assignment payload, received from the event.
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
