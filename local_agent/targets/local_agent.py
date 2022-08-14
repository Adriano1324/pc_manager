import json

import requests
from core.modules.process import Process

local_agent_key = "acSVPBpfLRspgefKceXrZtuUlUkffAPVZOeuvyqOdoJMDZglaxEJaUjRaFYyDorG"


class LocalAgent(Process):
    def __init__(self, name):
        super().__init__(name)

    def get_configuration(self):
        response = requests.get("http://127.0.0.1:8000/agent", {"key": local_agent_key})
        response = json.loads(response.content)
        return response

    def run(self):
        try:
            configuration = self.get_configuration()
            print(
                f"Hello {configuration['user_username']},"
                + f"I'm {configuration['name']} your local agent,"
                + f"I'm {'active' if configuration['active'] else 'disabled' }"
            )
            while configuration["active"]:
                configuration = self.get_configuration()
        except:
            pass
