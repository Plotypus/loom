from .incoming_message import IncomingMessage
from .field_types import RequiredField


###########################################################################
#
# Get Messages
#
###########################################################################
class GetStoryStatisticsIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.story_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_story_statistics(self.uuid, self.message_id, self.story_id)


class GetSectionStatisticsIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.section_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_section_statistics(self.uuid, self.message_id, self.section_id)


class GetParagraphStatisticsIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.section_id = RequiredField()
        self.paragraph_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_paragraph_statistics(self.uuid, self.message_id, self.section_id, self.paragraph_id)


class GetPageFrequenciesIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.story_id = RequiredField()
        self.wiki_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_page_frequencies(self.uuid, self.message_id, self.story_id, self.wiki_id)
