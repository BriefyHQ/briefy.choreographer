"""Tests for `briefy.choreographer.queues` module."""
from briefy.choreographer.queues.laure import Queue
from conftest import BaseQueueCase

payload = {
    "actor": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
    "created_at": "2017-01-22T21:50:57.763102+00:00",
    "data": {
        "additional_compensation": 0,
        "assignment_date": "2017-01-11T01:44:00+00:00",
        "availability": [
            "2017-02-10T10:00:00+00:00",
            "2017-02-15T10:00:00+00:00"
        ],
        "briefing": "https://files.stg.briefy.co/files/projects/1/briefing/agodabalibriefing.pdf",
        "category": "accommodation",
        "comments": [],
        "created_at": "2016-09-16T00:00:00+00:00",
        "customer": None,
        "customer_order_id": "1179164",
        "description": "",
        "external_id": None,
        "id": "f49a3991-343b-477a-878c-6a91120a491f",
        "location": {
            "additional_phone": None,
            "coordinates": {
                "coordinates": [
                    115.2636872,
                    -8.6954181
                ],
                "type": "Point"
            },
            "country": "ID",
            "email": "travers888@gmail.com",
            "formatted_address": "Jalan Danau Tamblingan, Bali, Indonesia",
            "fullname": "Elizabeth Travers",
            "id": "f99526d2-d6eb-4305-a62e-cd2c65a55600",
            "info": {
                "country": "ID",
                "formatted_address": "Jalan Danau Tamblingan, Bali, Indonesia",
                "postal_code": "",
                "province": "",
                "route": "Jalan Danau Tamblingan",
                "street_number": ""
            },
            "locality": "Bali",
            "mobile": None,
            "timezone": "UTC"
        },
        "number_required_assets": 56,
        "order_id": "bebf0ab5-b0d5-4033-92f6-e737751f20b9",
        "order_slug": "1701-PS4-068",
        "payable": True,
        "payout_currency": "EUR",
        "payout_value": 10000,
        "pool": {
            "country": "ID",
            "created_at": "2017-01-22T18:29:15.144446+00:00",
            "description": "Agoda Bali",
            "id": "009e2b7c-cc61-4f7b-ac34-7ced9a6bc0f5",
            "slug": "009e2b7c-agoda-bali",
            "state": "created",
            "title": "Agoda Bali",
            "updated_at": "2017-01-22T18:29:15.144498+00:00"
        },
        "pool_id": "009e2b7c-cc61-4f7b-ac34-7ced9a6bc0f5",
        "professional": {
            "created_at": "2017-01-22T18:29:27.718741+00:00",
            "description": None,
            "email": "pranayogavisual@gmail.com",
            "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
            "mobile": "+62 817-9788-899",
            "photo_path": None,
            "slug": "f14c1206",
            "state": "active",
            "title": "Agus Putu Pranayoga",
            "type": None,
            "updated_at": "2017-01-22T18:29:27.718753+00:00"
        },
        "professional_id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
        "professional_user": {
            "first_name": "Agus Putu",
            "fullname": "Agus Putu Pranayoga",
            "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
            "last_name": "Pranayoga"
        },
        "project": {
            "created_at": "2017-01-22T18:29:11.438158+00:00",
            "description": "",
            "id": "1dafb433-9431-4295-a349-92c4ad61c59e",
            "slug": "agoda-bali",
            "state": "ongoing",
            "title": "Agoda Bali",
            "updated_at": "2017-01-22T18:47:02.417870+00:00"
        },
        "project_manager": {
            "first_name": "Ariana",
            "fullname": "Ariana Shauh",
            "id": "eb1a8c1f-c9d7-4854-abf6-03ae2aea90de",
            "last_name": "Shauh"
        },
        "qa_manager": None,
        "reason_additional_compensation": "",
        "release_contract": "",
        "requirements": "Total: 56 photos\n\n3 Bedroom Villa - Photos: 5 - Filenames: 1179164_3"
                        "-bedroom-villa_XX.jpg\n\n4 Bedroom Beach Front - Photos: 5 - Filenames: "
                        "1179164_4-bedroom-beach-front_XX.jpg\n\n2 Bedroom Villa - Photos: 5 - "
                        "Filenames: 1179164_2-bedroom-villa_XX.jpg\n\n4 Bedroom Villa - Photos: 5",
        "scheduled_datetime": "2017-01-25T22:50:00+00:00",
        "scout_manager": {
            "first_name": "Job",
            "fullname": "Job Pool",
            "id": "f1233fb7-c482-454f-a12d-8f9305755774",
            "last_name": "Pool"
        },
        "set_type": "returned_photographer",
        "slug": "1701-PS4-068_01",
        "state": "scheduled",
        "state_history": [
            {
                "actor": {
                    "first_name": "Ariana",
                    "fullname": "Ariana Shauh",
                    "id": "eb1a8c1f-c9d7-4854-abf6-03ae2aea90de",
                    "last_name": "Shauh"
                },
                "date": "2016-09-16T00:00:00+00:00",
                "from": "",
                "message": "Created by Fachry Muchamad on Knack database",
                "to": "created",
                "transition": ""
            },
            {
                "actor": {
                    "first_name": "Ariana",
                    "fullname": "Ariana Shauh",
                    "id": "eb1a8c1f-c9d7-4854-abf6-03ae2aea90de",
                    "last_name": "Shauh"
                },
                "date": "2016-09-16T00:00:00+00:00",
                "from": "created",
                "message": "Automatic transition to pending",
                "to": "pending",
                "transition": "submit"
            },
            {
                "actor": {
                    "first_name": "Ponlawit",
                    "fullname": "Ponlawit Wisomka",
                    "id": "69fd7871-a504-43f1-b4c7-6901f9b46557",
                    "last_name": "Wisomka"
                },
                "date": "2016-09-16T00:00:00+00:00",
                "from": "pending",
                "message": "Assignment sent to job pool",
                "to": "published",
                "transition": "publish"
            },
            {
                "actor": {
                    "first_name": "Agus Putu",
                    "fullname": "Agus Putu Pranayoga",
                    "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
                    "last_name": "Pranayoga"
                },
                "date": "2017-01-11T01:44:00+00:00",
                "from": "published",
                "message": "Photographer assigned by 'Job Pool' on the Knack database",
                "to": "assigned",
                "transition": "self_assign"
            },
            {
                "actor": {
                    "first_name": "Agus Putu",
                    "fullname": "Agus Putu Pranayoga",
                    "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
                    "last_name": "Pranayoga"
                },
                "date": "2017-02-10T10:00:00+00:00",
                "from": "assigned",
                "message": "Scheduled by 'Agus Putu Pranayoga' on the Knack database",
                "to": "scheduled",
                "transition": "schedule"
            },
            {
                "actor": {
                    "first_name": "Agus Putu",
                    "fullname": "Agus Putu Pranayoga",
                    "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
                    "last_name": "Pranayoga"
                },
                "date": "2017-01-22T21:46:20.307878+00:00",
                "from": "assigned",
                "message": "ADADADAD",
                "to": "scheduled",
                "transition": "Schedule"
            },
            {
                "actor": {
                    "first_name": "Agus Putu",
                    "fullname": "Agus Putu Pranayoga",
                    "id": "f14c1206-5a75-42fd-bb02-735b885a3fd9",
                    "last_name": "Pranayoga"
                },
                "date": "2017-01-22T21:50:57.723502+00:00",
                "from": "assigned",
                "message": "",
                "to": "scheduled",
                "transition": "Schedule"
            }
        ],
        "submission_path": "",
        "tech_requirements": {
            "dimensions": [
                {
                    "operator": "min",
                    "value": "4150x3100"
                },
                {
                    "operator": "max",
                    "value": "4250x3200"
                }
            ],
            "mimetype": [
                {
                    "operator": "eq",
                    "value": "image/jpeg"
                }
            ],
            "orientation": [
                {
                    "operator": "eq",
                    "value": "landscape"
                }
            ],
            "ratio": [
                {
                    "operator": "eq",
                    "value": 1.3333333333333333
                }
            ]
        },
        "title": "KEJORA VILLAS - SUITES",
        "total_approvable_assets": 0,
        "total_assets": 0,
        "travel_expenses": 0,
        "updated_at": "2017-01-22T21:50:01.809120+00:00"
    },
    "event_name": "assignment.workflow.schedule",
    "guid": "f49a3991-343b-477a-878c-6a91120a491f",
    "id": "a49a3991-343b-477a-878c-6a91120a491f"
}


class TestChoreographerQueue(BaseQueueCase):
    """Tests for Choreographer Ms Laure Queue."""

    queue = Queue
    utility_name = 'laure.queue'

    def get_payload(self):
        """Payload for the Ms. laure queue."""
        return payload

    def test_interfaces(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy.common.queue import IQueue
        queue = self.queue()
        assert IQueue.providedBy(queue)

    def test_utility_lookup(self):
        """Test that this queue provides IQueue interfaces."""
        from briefy.common.queue import IQueue
        from zope.component import getUtility

        queue = getUtility(IQueue, self.utility_name)
        assert isinstance(queue, self.queue)

    def test_get_messages(self):
        """Test get_messages."""
        queue = self._make_one()
        payload = self.get_payload()
        resp = queue.write_message(payload)
        messages = queue.get_messages(num_messages=10)
        assert isinstance(messages, list)
        assert len(messages) == 1
        assert messages[0].message.message_id == resp
        assert messages[0].body['guid'] == payload['guid']
        assert messages[0].body['data']['total_assets'] == payload['data']['total_assets']
