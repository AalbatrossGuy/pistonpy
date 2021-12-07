# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests, json
from .exceptions import PistonError
from .extensions import lang_extensions as le

__all__  = ("GetOutput", "Extensions",)


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


class Extensions:
    def __init__(self, language: str, payload: list) -> None:
        self.payload = payload
        self.language = language

    @property
    def check_files(self):
        #file_extensions = [i.split('.')[1] for i in files]
        pass
