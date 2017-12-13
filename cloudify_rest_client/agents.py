########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from cloudify_rest_client.executions import Execution
from cloudify_rest_client.responses import ListResponse


class AgentsClient(object):

    def __init__(self, api):
        self.api = api

    def upgrade(self, *args, **kwargs):
        response = self.api.get('/agents/upgrade', params=kwargs)
        return ListResponse([Execution(item) for item in response['items']],
                            response['metadata'])
