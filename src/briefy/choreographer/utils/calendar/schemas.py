"""Helper schemas to deserialize an Assigment payload into an AssignmentEvent."""
from briefy.choreographer.config import PLATFORM_URL
from datetime import datetime
from datetime import timedelta

import colander
import pytz


class GeoPointSchema(colander.TupleSchema):
    """A X, Y GeoPoint representation."""

    lng = colander.SchemaNode(colander.Decimal(), missing=0)
    """Longitude."""

    lat = colander.SchemaNode(colander.Decimal(), missing=0)
    """Latitude."""


class CoordinatesSchema(colander.MappingSchema):
    """GeoJson Coordinates."""

    type = colander.SchemaNode(colander.String(), missing='Point')
    """Type of GeoJson."""

    coordinates = GeoPointSchema()
    """A Geo Point."""


class LocationSchema(colander.MappingSchema):
    """Location schema."""

    fullname = colander.SchemaNode(colander.String(), missing='')
    """Contact name."""

    email = colander.SchemaNode(colander.String(), validator=colander.Email(), missing='')
    """Contact phone number."""

    mobile = colander.SchemaNode(colander.String(), missing='')
    """Contact phone number."""

    additional_phone = colander.SchemaNode(colander.String(), missing=None)
    """Contact additional phone number."""

    formatted_address = colander.SchemaNode(colander.String(), missing='')
    """Location address."""

    coordinates = CoordinatesSchema()
    """GeoJson Coordinates."""


class AssignmentCalendarEventSchema(colander.MappingSchema):
    """An Event definition from an Assignment info."""

    id = colander.SchemaNode(colander.String(), validator=colander.uuid)
    """ID for the event."""

    state = colander.SchemaNode(colander.String())
    """Assignment state."""

    title = colander.SchemaNode(colander.String(), missing='')
    """Assignment name."""

    slug = colander.SchemaNode(colander.String())
    """Assignment slug."""

    scheduled_datetime = colander.SchemaNode(colander.DateTime(), missing=None)
    """Scheduled Datetime."""

    timezone = colander.SchemaNode(colander.String(), missing='UTC')
    """Timezone to be used."""

    duration = colander.SchemaNode(colander.Int(), missing=1)
    """Duration in hours.

    Currently we do not have this information and we default to 1 hour.
    """

    requirements = colander.SchemaNode(colander.String(), missing='')
    """Requirements."""

    location = LocationSchema()
    """Location schema."""


class AssignmentCalendarEvent:
    """Event information from an Assignment."""

    id = ''
    state = ''
    title = ''
    requirements = ''
    contact_name = ''
    contact_email = ''
    contact_phone = ''
    slug = ''
    _start = None
    _end = None
    timezone = 'UTC'
    address = ''
    geo = ()

    def __init__(self, **kwargs):
        """Initialize event."""
        self.id = kwargs['id']
        self.state = kwargs['state']
        self.title = kwargs['title']
        self.requirements = kwargs['requirements']
        self.contact_email = kwargs['location']['email']
        self.contact_name = kwargs['location']['fullname']
        self.contact_phone = kwargs['location']['mobile']
        self.slug = kwargs['slug']
        duration = (kwargs['duration']) * 3600
        self._start = kwargs['scheduled_datetime']
        self._end = self.start + timedelta(seconds=duration)
        self.timezone = kwargs['timezone']
        self.address = kwargs['location']['formatted_address']
        self.geo = kwargs['location']['coordinates']['coordinates']

    @property
    def description(self) -> str:
        """Description of this event.

        It contains the contact information and the requirements for the shoot.
        :return: Description of this event.
        """
        description = (
            f'Briefy assignment {self.slug}.\n{self.title}\nLocation: {self.address}\n'
            f'Contact person: {self.contact_name}\nPhone number {self.contact_phone}'
        )
        if self.requirements:
            description = f'{description}\nRequirements\n------------\n{self.requirements}'
        return description

    @property
    def summary(self) -> str:
        """Summary information about this event.

        :return: A summary for this event.
        """
        return f'Shooting for Briefy Assignment {self.slug}'

    @property
    def start(self) -> datetime:
        """Event Start."""
        start = self._start
        tz = pytz.timezone(self.timezone)
        return start.astimezone(tz)

    @property
    def end(self) -> datetime:
        """Event End."""
        end = self._end
        tz = pytz.timezone(self.timezone)
        return end.astimezone(tz)

    @property
    def status(self) -> str:
        """Event status."""
        return 'CANCELLED' if self.state == 'cancelled' else 'CONFIRMED'

    @property
    def url(self) -> str:
        """Canonical url for this assignment."""
        return f'{PLATFORM_URL}/assignments/{self.id}'
