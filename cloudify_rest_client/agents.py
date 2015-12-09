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


class Agent(dict):
    """
    Cloudify agent.
    """
    fields = ['validated']

    def __init__(self, agent):
        self.update(agent)

    def __getattr__(self, name):
        if name not in self.fields:
            raise AttributeError()
        return self[name]


class AgentsClient(object):

    def __init__(self, api):
        self.api = api

    def list(self, deployment_id=None, **kwargs):
        params = {}
        if deployment_id:
            params['deployment_id'] = deployment_id

        params.update(kwargs)
        response = self.api.get('/agents',
                                params=params)

        return [Agent(item) for item in response]
