"""Customer CustomerUserProfile Events."""
from briefy.choreographer.events.leica.profiles import IUserProfileEvent
from briefy.choreographer.events.leica.profiles import UserProfileEvent
from zope.interface import implementer


class ICustomerUserProfileEvent(IUserProfileEvent):
    """An event of a CustomerUserProfile."""


class ICustomerUserProfileWfEvent(ICustomerUserProfileEvent):
    """A workflow event of a UserProfile."""


class ICustomerUserProfileCreated(ICustomerUserProfileEvent):
    """Interface for customeruserprofile.created."""


class ICustomerUserProfileUpdated(ICustomerUserProfileEvent):
    """Interface for customeruserprofile.updated."""


class ICustomerUserProfileWfActivate(ICustomerUserProfileWfEvent):
    """Interface for customeruserprofile.workflow.activate."""


class ICustomerUserProfileWfDeactivate(ICustomerUserProfileWfEvent):
    """Interface for customeruserprofile.workflow.deactivate."""


class CustomerUserProfileEvent(UserProfileEvent):
    """An event of a UserProfile."""

    entity = 'CustomerUserProfile'


class CustomerUserProfileWfEvent(CustomerUserProfileEvent):
    """A workflow event of a UserProfile."""


@implementer(ICustomerUserProfileCreated)
class CustomerUserProfileCreated(CustomerUserProfileEvent):
    """Implement UserProfileCreated."""

    event_name = 'customeruserprofile.created'


@implementer(ICustomerUserProfileUpdated)
class CustomerUserProfileUpdated(CustomerUserProfileEvent):
    """Implement UserProfileUpdated."""

    event_name = 'customeruserprofile.updated'


@implementer(ICustomerUserProfileWfActivate)
class CustomerUserProfileWfActivate(CustomerUserProfileWfEvent):
    """Implement UserProfileWfActivate."""

    event_name = 'customeruserprofile.workflow.activate'


@implementer(ICustomerUserProfileWfDeactivate)
class CustomerUserProfileWfDeactivate(CustomerUserProfileWfEvent):
    """Implement UserProfileWfDeactivate."""

    event_name = 'customeruserprofile.workflow.deactivate'
