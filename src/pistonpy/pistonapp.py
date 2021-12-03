# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests

__all__ = ('PistonApp',)

class PistonApp():
    """The class to use while working with other code or creating applications or discord bots."""

    def __init__(self, embed: str = 'app') -> None:
        """
        :param embed: app - work as integrated.
            Default is set to app
        """
        self.embed = embed
        self._endpoint = "https://emkc.org/api/v2/piston"

    @property
    def runtimes(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        return response
