# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests

__all__ = ('PistonCli',)

class PistonCli():
    """The class to use while working with command line programs."""

    def __init__(self, embed: str = 'app') -> None:
        """
        :param embed: cli - work as command-line argument.
            Default is set to cli
        """
        self.embed = embed
        self._endpoint = "https://emkc.org/api/v2/piston"

    def __repr__(self) -> str:
        return "<pistonpy.PistonCli>"

    @property
    def runtimes(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        return response
