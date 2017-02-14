"""Briefy BriefyUserProfile Events."""
from briefy.choreographer.events.leica.profiles import IUserProfileEvent
from briefy.choreographer.events.leica.profiles import UserProfileEvent
from zope.interface import implementer


class IBriefyUserProfileEvent(IUserProfileEvent):
    """An event of a BriefyUserProfile."""


class IBriefyUserProfileWfEvent(IBriefyUserProfileEvent):
    """A workflow event of a UserProfile."""


class IBriefyUserProfileCreated(IBriefyUserProfileEvent):
    """Interface for briefyuserprofile.created."""


class IBriefyUserProfileUpdated(IBriefyUserProfileEvent):
    """Interface for briefyuserprofile.updated."""


class IBriefyUserProfileWfActivate(IBriefyUserProfileWfEvent):
    """Interface for briefyuserprofile.workflow.activate."""


class IBriefyUserProfileWfInactivate(IBriefyUserProfileWfEvent):
    """Interface for briefyuserprofile.workflow.deactivate."""


class BriefyUserProfileEvent(UserProfileEvent):
    """An event of a UserProfile."""

    entity = 'BriefyUserProfile'


class BriefyUserProfileWfEvent(BriefyUserProfileEvent):
    """A workflow event of a UserProfile."""


@implementer(IBriefyUserProfileCreated)
class BriefyUserProfileCreated(BriefyUserProfileEvent):
    """Implement UserProfileCreated."""

    event_name = 'briefyuserprofile.created'


@implementer(IBriefyUserProfileUpdated)
class BriefyUserProfileUpdated(BriefyUserProfileEvent):
    """Implement UserProfileUpdated."""

    event_name = 'briefyuserprofile.updated'


@implementer(IBriefyUserProfileWfActivate)
class BriefyUserProfileWfActivate(BriefyUserProfileWfEvent):
    """Implement UserProfileWfActivate."""

    event_name = 'briefyuserprofile.workflow.activate'


@implementer(IBriefyUserProfileWfInactivate)
class BriefyUserProfileWfInactivate(BriefyUserProfileWfEvent):
    """Implement UserProfileWfInactivate."""

    event_name = 'briefyuserprofile.workflow.deactivate'
