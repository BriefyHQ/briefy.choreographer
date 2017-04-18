"""Document briefy.choreographer event and actions."""
from briefy.choreographer.utils import get_event_actions
from briefy.choreographer.utils import get_events
from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.compat import Directive
from sphinx.util.docstrings import prepare_docstring

import docutils


class EventsDirective(Directive):
    """ Events directive.

    Injects sections in the documentation about the Events.
    """
    has_content = True
    option_spec = {}
    domain = 'briefy'
    doc_field_types = []

    def __init__(self, *args, **kwargs):
        """Initialize this Directive."""
        super(EventsDirective, self).__init__(*args, **kwargs)
        self.env = self.state.document.settings.env
        self.events = get_events()
        self.event_actions = get_event_actions(self.events)

    def _rst2node(self, body: str) -> docutils.nodes.paragraph:
        """Process an ReSTructuredTect block and return a paragraph containing it.

        Used, primarily, to process docstrings.
        """
        node = nodes.paragraph()
        result = ViewList(prepare_docstring(body))
        self.state.nested_parse(result, 0, node)
        return node

    def document_events(self) -> docutils.nodes.section:
        """Document events states.

        :returns: A section node containing the doctree for events description.
        """
        events = self.events
        actions = self.event_actions
        event_names = sorted(events.keys())
        node = nodes.section(ids=['events'], classes=['events'])
        node += nodes.title(text='Events')
        for event_name in event_names:
            klass = events.get(event_name)
            description = klass.__doc__
            event_actions = actions.get(event_name)
            event_id = 'events-{event_name}'.format(event_name=event_name)
            event_node = nodes.section(ids=[event_id], classes=['event'])
            event_node += nodes.title(text=event_name)
            event_node += self._rst2node(description)
            if event_actions:
                actions_id = '{event_id}-actions'.format(event_id=event_id)
                actions_node = nodes.section(ids=[actions_id], classes=['actions'])
                actions_node += nodes.title(text='Actions')
                for action_id, action in event_actions.items():
                    action_desc = self._rst2node(action.__doc__)
                    temp = nodes.definition_list_item()
                    temp += nodes.term(text=action_id, ids=[action_id])
                    definition = nodes.definition()
                    definition += action_desc
                    temp += definition
                    actions_node += temp
                event_node += actions_node
            node += event_node
        return node

    def run(self) -> list:
        """Process the directive.

        :returns: List of nodes.
        """
        events = self.document_events()
        return [events, ]


def setup(app):
    """Setup the extension."""
    app.add_directive('events', EventsDirective)
    return {
        'version': '1.0'
    }
