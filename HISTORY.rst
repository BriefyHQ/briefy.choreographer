=======
History
=======


2.0.12 (2017-04-19)
-------------------

* Card #219: Notification to customers when PM leaves a comment on an order (ericof).
* Added import order, string quotes and formatting (ericof).
* Custom JSON class to monkey patch logstash.formater.json module and serialize complex objects (rudaporto).

2.0.11 (2017-04-18)
-------------------

* Fix: check if professional is available before to try do add it to the slack payload (rudaporto).
* Card #142: Support for Leica task events, including Slack notifications (ericof).
* Improve documentation (ericof).

2.0.10 (2017-03-23)
-------------------

* Laure: Register adapters for laure.assignment.ignored_copy (jsbueno).

2.0.9 (2017-03-14)
------------------

* Comment: Action to notify on slack about new comment created (ericof).
* Logger subscriber: Serialize the data payload before sending it to Kibana (ericof).

2.0.8 (2017-02-23)
------------------

* BUG: Reset password email should use code and not id to create the URL (ericof).

2.0.7 (2017-02-22)
------------------

* Laure validation events on Slack use the complete_feedback field, not feedback (ericof).
* Professional: On approval send slack message to Finance (ericof).
* Professional: On validation send slack message to Scouters (ericof).
* Professional: On approval send welcome email to Creative (ericof).
* Comment: On comment from Customer to PM send an email (ericof).
* Order: Set refused from Customer, send an email to PM (ericof).
* Assignment: On set rejected by QA, send message to creative (ericof).
* Assignment: On set rejected by Ms. Laure, send message to creative (ericof).
* Customer User: On user profile activation, send message to user (ericof).
* Add support for Laure's ignored_copy event (jsbueno)

2.0.6 (2017-02-21)
------------------

* Register new slack action adapters for Assignment workflow transitions (rudaporto).

2.0.5 (2017-02-20)
------------------

* Added all missing Assignment transition adapters to post messages on slack (rudaporto).


2.0.4 (2017-02-17)
------------------

* On Laure events add also the validation feedback to the slack action (ericof).


2.0.3 (2017-02-16)
------------------

* Add laure.assignment.ignored event (ericof).
* Report on pending assignments to scouting team channel (ericof).
* Add assignment.workflow.assign_qa_manager subscriber (ericof).
* Fix assignments Slack actions (ericof).
* Update Slack actions for Assignment, Order, Professional (ericof).

2.0.2 (2017-02-15)
------------------

* Fix Comments notification on Slack (ericof).
* Add order.wf.edit_requirements event (ericof).
* Add CustomerUserProfile and BriefyUserProfile events (ericof).
* Add Slack actions to CustomerUserProfile and BriefyUserProfile (ericof).
* Add Slack actions to Professional (ericof).

2.0.1 (2017-02-14)
------------------

* Fix notification to creative being sent to customer (ericof).
* Split Leica notifications, on Slack, to distinct channels (ericof).
* Improve user notifications (ericof).


2.0.0 (2017-02-13)
------------------

* Add support to logging to Google BigQuery (ericof).
* Add support to Leica (ericof).
* Add support to Ms. Laure (jsbueno).
* Improvements in logging and documentation (ericof).


1.0.1 (2016-09-06)
------------------

* Fix mandril template for new Lead action (rudaporto).

1.0.0 (2016-09-02)
------------------

* Implements the Choreographer Worker (ericof)
* Mail action, now, accepts sender email and sender name (ericof)
* BODY-95: Implement forgot password actions (ericof)
