# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests, json
from .exceptions import PistonError

__all__  = ("GetOutput",)

class GetOutput:
    def __init__(self, payload: dict) -> None:
        self._endpoint = "https://emkc.org/api/v2/piston/execute"
        self.payload = payload

    def parse_output(self):
        output = requests.request("POST", url=self._endpoint, data = json.dumps(self.payload))
        output = output.json()

        if output.get('message'):
            raise PistonError(output.get('message'))
        else:
            return output
