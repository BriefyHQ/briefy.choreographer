"""Slack action for Package Order coming from the website."""
from briefy.choreographer.actions.slack import ISlack
from briefy.choreographer.actions.slack import Slack
from briefy.choreographer.events import lead
from zope.component import adapter
from zope.interface import implementer

import typing as t


class PackageOrderSlack(Slack):
    """Base class used for Slack message sent for Package Orders."""

    entity = 'PackageOrder'
    weight = 100
    _channel = '#briefy-co-quotes'

    @staticmethod
    def filter_add_ons(add_ons: t.Sequence[t.Any]) -> t.Sequence[str]:
        """Filter selected add ons and return a sequence of strings.

        :param add_ons: Sequence of add_ons
        :return: Sequence of strings
        """
        processed = []
        for add_on in add_ons:
            id_ = add_on['id']
            value = add_on['value']
            if not value:
                continue
            if isinstance(value, bool):
                value = 'Selected'
            else:
                value = str(value)
            processed.append(
                f'{id_}: {value}'
            )
        return processed


@adapter(lead.IPackageOrderCreated)
@implementer(ISlack)
class PackageOrderCreated(PackageOrderSlack):
    """After creating a new Quote, post on slack."""

    def transform(self) -> t.List[dict]:
        """Transform data."""
        payload = super().transform()
        data = self.data
        payload_item = payload[0]
        fullname = data['contact_name']
        locations = data['locations']
        total_locations = len(locations)
        locations = ', '.join([l for l in locations])
        add_ons = ', '.join(self.filter_add_ons(data['add_ons']))
        payload_item['title'] = 'New Package ordered!'
        payload_item['text'] = 'A new package was ordered, whoop, whoop!'
        payload_item['username'] = 'Business Developer Internet'
        payload_item['data'] = {
            'fields': [
                {'title': 'Company',
                 'value': data['company_name'],
                 'short': False,
                 },
                {'title': 'Fullname',
                 'value': fullname,
                 'short': True,
                 },
                {'title': 'Email',
                 'value': data['contact_email'],
                 'short': True,
                 },
                {'title': 'Contact Role',
                 'value': data['contact_role'],
                 'short': True,
                 },
                {'title': 'Package',
                 'value': data['package_id'],
                 'short': False,
                 },
                {'title': 'Total shoots',
                 'value': data['orders'],
                 'short': True,
                 },
                {'title': 'Category',
                 'value': data['category'],
                 'short': True,
                 },
                {'title': 'Locations',
                 'value': f'{total_locations}: {locations}',
                 'short': False,
                 },
                {'title': 'Add ons',
                 'value': add_ons,
                 'short': False,
                 },
            ]
        }
        return payload
