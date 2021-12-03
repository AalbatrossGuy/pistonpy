# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests

__all__ = ('PistonApp',)

class PistonApp():
    """The base initialization client. An instance of it must be defined to work with this class."""

    def __init__(self, embed: str = 'app') -> None:
        """
        :param embed: cli - work as command-line argument.
        :param embed: app - work as integrated.
            Default is set to app
        :private endpoint: the base url. Do not change.
        """
        self.embed = embed
        self._endpoint = "https://emkc.org/api/v2/piston"

    @property
    def runtimes(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        return response
