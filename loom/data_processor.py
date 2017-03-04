from loom.dispatchers import DemoDataDispatcher
from loom.messages import IncomingMessage, OutgoingMessage
from loom.messages.incoming.demo import DemoIncomingMessageFactory
from loom.serialize import decode_string_to_bson, encode_bson_to_string

import re

from bson import ObjectId
from typing import Dict

JSON = Dict


class DataProcessor:
    def __init__(self, interface):
        self.dispatcher = DemoDataDispatcher(interface)
        self.message_factory = DemoIncomingMessageFactory()
        self.responses = {}

    async def load_file(self, filename):
        with open(filename) as json_file:
            json_string = json_file.read()
        json = decode_string_to_bson(json_string)
        user_json = json['user']
        wiki_json = json['wiki']
        story_json = json['story']
        user_id = await self.create_user(user_json)
        wiki_id = await self.create_wiki(user_id, wiki_json)
        story_id = await self.create_story(user_id, wiki_id, story_json)
        await self.process_list(json['dispatch_list'], user_id, wiki_id, story_id)

    async def create_user(self, user_json):
        user_id = await self.dispatcher.db_interface.create_user(**user_json)
        return user_id

    async def create_wiki(self, user_id, wiki_json):
        wiki_id = await self.dispatcher.db_interface.create_wiki(user_id, **wiki_json)
        return wiki_id

    async def create_story(self, user_id, wiki_id, story_json):
        story_id = await self.dispatcher.db_interface.create_story(user_id, wiki_id=wiki_id, **story_json)
        return story_id

    async def process_list(self, dispatch_list, user_id, wiki_id, story_id):
        additional_args = {
            'user_id': user_id,
            'wiki_id': wiki_id,
            'story_id': story_id,
        }
        self.responses['user'] = await self.dispatcher.db_interface.get_user_preferences(user_id)
        self.responses['wiki'] = await self.dispatcher.db_interface.get_wiki(wiki_id)
        self.responses['story'] = await self.dispatcher.db_interface.get_story(story_id)
        for dispatch_item in dispatch_list:
            revised: JSON = {k: self.replace_id(v) for k, v in dispatch_item.items()}
            action = revised.pop('action')
            message: IncomingMessage = self.message_factory.build_message(self.dispatcher, action, revised, additional_args)
            response: OutgoingMessage = await message.dispatch()
            if message.message_id is not None:
                self.responses[message.message_id] = response

    id_regex = re.compile(r'\$\{([^}]+)\}')

    # TODO: Fix this! Need to handle new wiki IDs/story IDs.
    def replace_id(self, value):
        if isinstance(value, dict):
            revised = {k: self.replace_id(v) for k, v in value.items()}
            return revised
        if not isinstance(value, str):
            return value
        string_parts = []
        prev_end = 0
        fullmatch = re.fullmatch(self.id_regex, value)
        if fullmatch is not None:
            m_id, keys = fullmatch.group(1).split('.', 1)
            m_id = int(m_id)
            keys = keys.split('.')
            response = vars(self.responses[m_id])
            for key in keys:
                response = response[key]
            return response
        matches = re.finditer(self.id_regex, value)
        for match in matches:
            string_parts.append(value[prev_end:match.start()])
            m_id, keys = match.group(1).split('.', 1)
            m_id = int(m_id)
            keys = keys.split('.')
            response = vars(self.responses[m_id])
            for key in keys:
                response = response[key]
            if isinstance(response, ObjectId):
                # TODO: Update this fix
                # Remove the whitespace in the ObjectId's encoding.
                response = encode_bson_to_string(response).replace(' ', '')
            prev_end = match.end()
            string_parts.append(response)
        string_parts.append(value[prev_end:])
        return ''.join(string_parts)
