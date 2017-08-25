"""Utils to extract user roles inforation from data payloads."""
from briefy.choreographer.events import IInternalEvent
from briefy.choreographer.events import InternalEvent
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface

import typing as t


class IUsersDataExtractor(Interface):
    """Extract user data from the data payload."""

    def users_by_role(role_name: str) -> t.List[dict]:
        """Return users data by role name."""

    def users_by_group(group_name: str) -> t.List[dict]:
        """Return users data by group name."""


@adapter(IInternalEvent)
@implementer(IUsersDataExtractor)
class UsersDataExtractor:
    """Extract users data from internal event payload."""

    group_roles_map = {
        'customer_users': [
            'customer_manager',
            'customer_pm',
            'customer_qa',
            'project_customer_pm',
            'project_customer_qa'
        ],
        'project_managers': [
            'internal_pm'
        ],
        'scout_managers': [
            'internal_scout',
            'assignment_internal_scout'
        ],
        'qa_managers': [
            'internal_qa',
            'assignment_internal_qa'
        ],
        'professional_user': [
            'professional_user'
        ]
    }

    def __init__(self, event: InternalEvent):
        """Receive the event being adapted."""
        self.event = event

    def users_by_role(self, role_name: str) -> t.List[dict]:
        """Return users data by role name."""
        payload = self.event.data
        all_roles = payload.get('_roles', {})
        all_actors = payload.get('_actors', {})
        result = []
        roles = all_roles.get(role_name, [])
        for user_id in roles:
            user_data = all_actors.get(user_id, None)
            if user_data:
                result.append(user_data)
        return result

    def users_by_group(self, group_name: str) -> t.List[dict]:
        """Return users data by group name."""
        user_ids = set()
        result = []
        payload = self.event.data
        all_roles = payload.get('_roles', {})
        all_actors = payload.get('_actors', {})
        for role_name in self.group_roles_map.get(group_name, []):
            user_ids = user_ids.union(set(all_roles.get(role_name, [])))
        for user_id in user_ids:
            user_data = all_actors.get(user_id, None)
            if user_data:
                result.append(user_data)
        return result


def users_data_by_group(
        event: InternalEvent,
        group_name: str,
        check_notification: bool=False) -> t.List[dict]:
    """Return users data by group.

    :param event: internal event instance
    :param group_name: name of the group
    :param check_notification: if true only return users with internal notification enable
    :returns list of user data maps
    """
    extractor = IUsersDataExtractor(event)
    users_data = extractor.users_by_group(group_name)
    if check_notification:
        result = [user for user in users_data if user.get('internal') is True]
    else:
        result = users_data
    return result


def users_data_by_role(
        event: InternalEvent,
        role_name: str,
        check_notification: bool=False) -> t.List[dict]:
    """Return users data by group.

    :param event: internal event instance
    :param role_name: name of the group
    :param check_notification: if true only return users with internal notification enable
    :returns list of user data maps
    """
    extractor = IUsersDataExtractor(event)
    users_data = extractor.users_by_role(role_name)
    if check_notification:
        result = [user for user in users_data if user.get('internal') is True]
    else:
        result = users_data
    return result
