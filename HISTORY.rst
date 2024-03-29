=======
History
=======

2.1.7 (2017-12-20)
------------------

    * Fix slack notification for user login (rudaporto).

2.1.6 (2017-12-05)
------------------

    * Upgrade python3 docker image version 1.4.5 (rudaporto).
    * Upgrade briefy.common to version 2.1.7 (rudaporto).

2.1.5 (2017-11-06)
------------------

    * Add new Rolleiflex events (ericof).
    * Action to send an email when a new user, for the delivery system, is created (ericof).

2.1.4 (2017-10-11)
------------------

    * Card #678: added new IQueue name utility to write messages to briefy.reflex (rudaporto).
    * Card #678: added new action to route order.workflow.accept messages from leica to reflex (rudaporto).
    * Refactor ms.laure queue and actions to be used as generic route queue and route action implementation (rudaporto).

2.1.3 (2017-10-10)
------------------

    * Card #646: New action to route assignment workflow transition read_for_upload event to ms.laure delivery queue (rudaporto).

2.1.2 (2017-10-06)
------------------

    * Fix briefy.leads quote events' handlers (ericof).
    * Add Additional Info and Category to Quote actions (ericof).

2.1.1 (2017-09-05)
------------------

    * Card #608: added new action to notify Creative when assignment is permanently rejected (rudaporto).
    * Card #609: added new action to notify PM when assignment is permanently rejected (rudaporto).
    * Card #609: fixed a typo in AssignmentPMMail.recipients preventing all assignment email notifications do PM (rudaporto).
    * Card #605: added new action to notify Scout team when a new Lead is confirmed (rudaporto).
    * Card #606: added new action to notify PM when a new Lead is confirmed (rudaporto).
    * Card #607: fixed the cancellation mail action to Creative when the Assignment is cancelled (rudaporto).
    * Card #612: fixed failure when trying to get the timezone from a Order.assignment with None value (rudaporto).
    * Card #613: OrderSubmitScoutMail and OrderSubmitCustomerMail now are disabled for Leads (rudaporto).
    * Card #614: added new action to notify PM when assignment have a new comment about scheduling issues (rudaporto).
    * Card #615: added new action to notify PM when order location is updated (rudaporto).
    * Card #616: added new action to notify PM when order requirements is updated (rudaporto).
    * Added location contact info to the Order email payload and improve in the Assignment email payload (rudaporto).
    * Card #617: added an available check to AssignmentApproveCreativeMail to only send email in the first approval (rudaporto).

2.1.0 (2017-08-31)
------------------

* Update notifications to use new roles and actors attributes in the payload (rudaporto).
* Fix: remove method in actions.leica.comment.CommentMail._recipients that was buggy and exists in the parent class (rudaporto).
* Added a logger.warn call to track when there are no recipients in mail actions (rudaporto).
* Fix: InternalEvent needs to implement IInternalEvent (ericof).
* Add Slack notification to leads.PackageOrder creation (ericof).

2.0.21 (2017-08-22)
-------------------

* Fix registered_actions logging (ericof).

2.0.20 (2017-08-22)
-------------------

* Card #552: LeadOrder events not being sent (ericof).
* Improve logging of discarded events (ericof).

2.0.19 (2017-08-07)
-------------------

* Add Assignment title to calendar invitation (ericof).


2.0.18 (2017-08-07)
-------------------

* Add calendar information to emails sent to Creatives (ericof).
* Card #483: Implement late re-submission email (ericof).


2.0.17 (2017-07-19)
-------------------

* Including two new variables in the assignment mail data payload: NUMBER_REQUIRED_ASSETS, REQUIREMENTS (rudaporto).

2.0.16 (2017-07-18)
-------------------

* Created events subscribers and actions for new task events: notify before shooting and notify late submission (rudaporto).

2.0.15 (2017-05-23)
-------------------

* Card #327: Update actions to replace Photographer by Content creator (ericof).


2.0.14 (2017-05-18)
-------------------
* Fix: added missing subscriber registration for assignment.workflow.start_post_process (rudaporto).
* Added events, subscribers config and actions (leica and slack) for ms.laure post processing result events (rudaporto).
* New queue utility to route message directly to ms.laure delivery queue (rudaporto).
* Update laure actions for approve and post processing assignment transition to use the new delivery queue (rudaporto).

2.0.13 (2017-05-11)
-------------------
* Card #291: Added AssignmentWfStartPostProcess subscriber and actions to post on slack and send to ms.laure (rudaporto).
* Added octopus.checkstyle as a dev dependency and update setup.cfg settings. (rudaporto)
* Fix: added missing subscriber registration for assignment.workflow.start_post_process (rudaporto).

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
