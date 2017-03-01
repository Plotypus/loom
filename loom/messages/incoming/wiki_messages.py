from .incoming_message import IncomingMessage
from .field_types import RequiredField, OptionalField


###########################################################################
#
# Create Messages
#
###########################################################################
class CreateWikiIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.title = RequiredField()
        self.summary = RequiredField()

    def dispatch(self):
        return self._dispatcher.create_wiki(self.message_id, self.title, self.summary)


###########################################################################
#
# Add Messages
#
###########################################################################
class AddSegmentIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.title = RequiredField()
        self.parent_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.add_segment(self.message_id, self.title, self.parent_id)


class AddTemplateHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.title = RequiredField()
        self.segment_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.add_template_heading(self.message_id, self.title, self.segment_id)


class AddPageIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.title = RequiredField()
        self.parent_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.add_page(self.message_id, self.title, self.parent_id)


class AddHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.title = RequiredField()
        self.page_id = RequiredField()
        self.index = OptionalField()

    def dispatch(self):
        return self._dispatcher.add_heading(self.message_id, self.title, self.page_id, self.index)


###########################################################################
#
# Edit Messages
#
###########################################################################
class EditWikiIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.wiki_id = RequiredField()
        self.update = RequiredField()

    def dispatch(self):
        return self._dispatcher.edit_wiki(self.message_id, self.wiki_id, self.update)


class EditSegmentIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()
        self.update = RequiredField()

    def dispatch(self):
        return self._dispatcher.edit_segment(self.message_id, self.segment_id, self.update)


class EditTemplateHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()
        self.template_heading_title = RequiredField()
        self.update = RequiredField()

    def dispatch(self):
        return self._dispatcher.edit_template_heading(self.message_id, self.segment_id, self.template_heading_title,
                                                      self.update)


class EditPageIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.page_id = RequiredField()
        self.update = RequiredField()

    def dispatch(self):
        return self._dispatcher.edit_page(self.message_id, self.page_id, self.update)


class EditHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.page_id = RequiredField()
        self.heading_title = RequiredField()
        self.update = RequiredField()

    def dispatch(self):
        return self._dispatcher.edit_heading(self.message_id, self.page_id, self.heading_title, self.update)


###########################################################################
#
# Get Messages
#
###########################################################################
class GetWikiInformationIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.wiki_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_wiki_information(self.message_id, self.wiki_id)


class GetWikiHierarchyIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.wiki_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_wiki_hierarchy(self.message_id, self.wiki_id)


class GetWikiSegmentHierarchyIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_wiki_segment_hierarchy(self.message_id, self.segment_id)


class GetWikiSegmentIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_wiki_segment(self.message_id, self.segment_id)


class GetWikiPageIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.page_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.get_wiki_page(self.message_id, self.page_id)


###########################################################################
#
# Delete Messages
#
###########################################################################
class DeleteWikiIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.wiki_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_wiki(self.message_id, self.wiki_id)


class DeleteSegmentIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_segment(self.message_id, self.segment_id)


class DeleteTemplateHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.segment_id = RequiredField()
        self.template_heading_title = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_template_heading(self.message_id, self.segment_id, self.template_heading_title)


class DeletePageIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.page_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_page(self.message_id, self.page_id)


class DeleteHeadingIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.page_id = RequiredField()
        self.heading_title = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_heading(self.message_id, self.heading_title, self.page_id)


class DeleteAliasIncomingMessage(IncomingMessage):
    def __init__(self):
        super().__init__()
        self.alias_id = RequiredField()

    def dispatch(self):
        return self._dispatcher.delete_alias(self.message_id, self.alias_id)
