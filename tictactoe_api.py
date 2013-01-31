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


"""TicTacToe API implemented using Google Cloud Endpoints."""


import random
import re

from google.appengine.ext import endpoints
from protorpc import remote

from models import Score
from tictactoe_api_messages import BoardMessage
from tictactoe_api_messages import ScoresListRequest
from tictactoe_api_messages import ScoresListResponse
from tictactoe_api_messages import ScoreRequestMessage
from tictactoe_api_messages import ScoreResponseMessage


CLIENT_ID = 'YOUR-CLIENT-ID'


@endpoints.api(name='tictactoe', version='v1',
               description='Tic Tac Toe API',
               allowed_client_ids=[CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID])
class TicTacToeApi(remote.Service):
    """Class which defines tictactoe API v1."""

    @staticmethod
    def add_move_to_board(board_state):
        """Adds a random 'O' to a tictactoe board.

        Args:
            board_state: String; contains only '-', 'X', and 'O' characters.

        Returns:
            A new board with one of the '-' characters converted into an 'O';
            this simulates an artificial intelligence making a move.
        """
        result = list(board_state)  # Need a mutable object

        free_indices = [match.start()
                        for match in re.finditer('-', board_state)]
        random_index = random.choice(free_indices)
        result[random_index] = 'O'

        return ''.join(result)

    @endpoints.method(BoardMessage, BoardMessage,
                      path='board', http_method='POST',
                      name='board.getmove')
    def board_get_move(self, request):
        """Exposes an API endpoint to simulate a computer move in tictactoe.

        Args:
            request: An instance of BoardMessage parsed from the API request.

        Returns:
            An instance of BoardMessage with a single 'O' added to the board
            passed in.
        """
        board_state = request.state
        if not (len(board_state) == 9 and set(board_state) <= set('OX-')):
            raise endpoints.BadRequestException('Invalid board.')
        return BoardMessage(state=self.add_move_to_board(board_state))

    @endpoints.method(ScoresListRequest, ScoresListResponse,
                      path='scores', http_method='GET',
                      name='scores.list')
    def scores_list(self, request):
        """Exposes an API endpoint to query for scores for the current user.

        Args:
            request: An instance of ScoresListRequest parsed from the API
                request.

        Returns:
            An instance of ScoresListResponse containing the scores for the
            current user returned in the query. If the API request specifies an
            order of WHEN (the default), the results are ordered by time from
            most recent to least recent. If the API request specifies an order
            of TEXT, the results are ordered by the string value of the scores.
        """
        query = Score.query_current_user()
        if request.order == ScoresListRequest.Order.TEXT:
            query = query.order(Score.outcome)
        elif request.order == ScoresListRequest.Order.WHEN:
            query = query.order(-Score.played)
        items = [entity.to_message() for entity in query.fetch(request.limit)]
        return ScoresListResponse(items=items)

    @endpoints.method(ScoreRequestMessage, ScoreResponseMessage,
                      path='scores', http_method='POST',
                      name='scores.insert')
    def scores_insert(self, request):
        """Exposes an API endpoint to insert a score for the current user.

        Args:
            request: An instance of ScoreRequestMessage parsed from the API
                request.

        Returns:
            An instance of ScoreResponseMessage containing the score inserted,
            the time the score was inserted and the ID of the score.
        """
        entity = Score.put_from_message(request)
        return entity.to_message()


APPLICATION = endpoints.api_server([TicTacToeApi],
                                   restricted=False)
