Briefy Choreographer
====================

Choreographer is the core of events processing in Briefy *microservices architecture*.

When some *microservice* fire an event to our AWS SQS event queue, like *briefy.leads*,
Choreographer is waiting to:

* read events from SQS queue *events*
* for each event identify event type and dispatch internal event (*zope.events.notify*)
* lookup internal event handlers subscribers to get event data and log handler invocation
* find all multi adapters registered (actions) for a given data type, event name pair
* order and run each action adapter, which in fact do:

  * transform event data to new payload format (transform)
  * send new payload to the queue name defined in the action class
  * log action execution

Choreographer Dancing Events
----------------------------

As choreography in real life, *briefy.choreographer* has to coordinate the flow:

* receive events coming from serialized input queue
* (re)dispatch events internally
* handler subscribers catch internal events
* adapt, execute actions and transform data
* send new events and data to output queues
* log all processing steps


Queue Worker
^^^^^^^^^^^^

Everything begins with a worker runner: *briefy.choreographer.worker.Worker* which is an
specialized version of *briefy.common.worker.QueueWorker*.

The Worker run in infinite loop and:

* at specified interval, call the *process* method
* the *process* method read events from the defined queue (parameter at instantiation time)

Actually, the defined queue is a named Utility *event.queue* that implements IQueue interface and is
registered on *briefy.common.queue.event.EventQueue*.

After get one or more messages from the queue:

* the worker process each message looking for a named Utility that implements IInternalEvent
* the *event_name* attribute received on the body of the message is used to find correct Utility


Internal Events
^^^^^^^^^^^^^^^

The IInternalEvent Utility works as a *event factory class* to create a new internal event and
dispatch it using the *zope.event.notify* function.

When a new IInternalEvent is fired by *zope.event.notify* all subscribed handlers are notified and
executed. For all IInternalEvent notified the *briefy.choreographer.subscribers.logger.handler*
log the information about the fired internal event.

Also, one or more handlers can be registered for specialized IInternalEvent interfaces like:

* briefy.choreographer.events.lead.ILeadEvent
* briefy.choreographer.events.mail.IMailEvent

The registered handler for each specialized IInternalEvent interface are based on a common pattern
derived from *briefy.choreographer.subscribers.BaseHandler*.


Handler Pattern
^^^^^^^^^^^^^^^

This pattern defines that each subclass of BaseHandler must have a DTO class as *_info_class_*
internal attribute which implement *briefy.choreographer.data.IDataTransferObject* interface.

When the a subclass of BaseHandler is called, it lookup all multi adapters registered to
adapt the pair (*IDataTransferObject*, *IInternalEvent*) interfaces to *IAction* interface.
At this point, the *IAction* adapters are ordered by the *weight* attribute (int value), to
define execution order.

Actions
^^^^^^^

Actions are based on *briefy.choreographer.actions.Action* base class, and each subclass must
define a *_queue_name* attribute which is used process the action when called:

* call the *action.transform* to prepare the payload from the *action.data* attribute.
* get the queue named Utility that implements IQueue for the *action._queue_name* attribute
* sent the payload data to the queue calling *action.queue.write_message*.
* log the action performed to register all information processed

These queues used by actions are output queues and are all based on *briefy.common.queue.Queue*
implementation and are AWS SQS queues that will be read from other *microservices* that have workers
listen on then to, at some point, process the message and generate more events or finish the chain.

Code Health
===========
The *breafy.choreography* service codebase is tested using Travis CI

============ ======================================================================================================================== 
Branch       Status
============ ========================================================================================================================
`master`_     .. image:: https://travis-ci.com/BriefyHQ/briefy.choreographer.svg?token=APuRM8itTuPw15pKpJWp&branch=master
                 :target: https://travis-ci.com/BriefyHQ/briefy.choreographer

`develop`_    .. image:: https://travis-ci.com/BriefyHQ/briefy.choreographer.svg?token=APuRM8itTuPw15pKpJWp&branch=develop
                 :target: https://travis-ci.com/BriefyHQ/briefy.choreographer
============ ========================================================================================================================



.. _`master`: https://github.com/BriefyHQ/briefy.choreographer/tree/master
.. _`develop`: https://github.com/BriefyHQ/briefy.choreographer/tree/develop
