#!/usr/bin/python

# Copyright (C) 2010-2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""ProtoRPC message class definitions for TicTicToe API."""


from protorpc import messages


class BoardMessage(messages.Message):
    """ProtoRPC message definition to represent a board."""
    state = messages.StringField(1, required=True)


class ScoresListRequest(messages.Message):
    """ProtoRPC message definition to represent a scores query."""
    limit = messages.IntegerField(1, default=10)
    class Order(messages.Enum):
        WHEN = 1
        TEXT = 2
    order = messages.EnumField(Order, 2, default=Order.WHEN)


class ScoreRequestMessage(messages.Message):
    """ProtoRPC message definition to represent a score to be inserted."""
    outcome = messages.StringField(1, required=True)


class ScoreResponseMessage(messages.Message):
    """ProtoRPC message definition to represent a score that is stored."""
    id = messages.IntegerField(1)
    outcome = messages.StringField(2)
    played = messages.StringField(3)


class ScoresListResponse(messages.Message):
    """ProtoRPC message definition to represent a list of stored scores."""
    items = messages.MessageField(ScoreResponseMessage, 1, repeated=True)
