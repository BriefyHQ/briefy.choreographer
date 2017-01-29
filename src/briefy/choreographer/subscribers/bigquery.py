"""BigQuery handler."""
from briefy.common.config import MOCK_SQS
from briefy.choreographer.config import DATASET
from briefy.choreographer.config import GOOGLE_APPLICATION_CREDENTIALS
from briefy.choreographer.config import TABLE
from briefy.choreographer.events import InternalEvent
from google.cloud import bigquery

import logging

logger = logging.getLogger(__name__)

BQ_CLIENT = None
_dataset = None
_table = None

if GOOGLE_APPLICATION_CREDENTIALS and not MOCK_SQS:
    BQ_CLIENT = bigquery.Client()
    _dataset = BQ_CLIENT.dataset(DATASET)
    _table = _dataset.table(TABLE)
    _table.reload()
    logger.info('Choreographer will use BigQuery backend')


def _write_to_bigquery(event: InternalEvent, table):
    """Write event to BigQuery

    :param event: Internal event
    :param table: BigQuery table
    """
    rows = [
        [
            event.event_name,
            event.actor,
            event.guid,
            event.created_at,
            event.request_id,
        ]
    ]
    errors = table.insert_data(rows)
    if errors:
        logger.exception(
            'An error occurred writing event to bigquery: {exc}'.format(
                exc=str(errors)
            )
        )


def handler(event: InternalEvent):
    """Catch all handler that logs the event to BigQuery.

    :param event: Event
    """
    if _table:
        try:
            _write_to_bigquery(event, _table)
        except Exception as exc:
            logger.exception(
                'An error occurred writing event to bigquery: {exc}'.format(
                    exc=str(exc)
                )
            )
