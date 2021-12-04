# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests, json
from typing import Optional
from .exceptions import CodeNotFound, LanguageNotFound, CodeFormatNotFound, NotAFile
from .models import GetOutput

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

    def __repr__(self) -> str:
        return "<pistonpy.PistonApp>"

    @property
    def runtimes(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        data = response.json()
        return { item.pop("language"): item for item in data }


    @property
    def languages(self) -> list:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        data = response.json()
        lang = []
        for language in data:
            lang.append(language['language'])
        return lang

    def run(
        self,
        language: str,
        version: str = "*",
        files: Optional[list] = [],
        code: Optional[str] = "",
        args: Optional[list] = [],
        input: Optional[str] = "",
        compile_timeout: Optional[int] = 10_000,
        run_timeout: Optional[int] = 3_000,
        compile_memory_limit: Optional[int] = -1,
        run_memory_limit: Optional[int] = -1,
    ) -> list:


        """Main Code Execution"""
        main_code = ''
        if not code and not files:
            print('running CodeNotFound')
            raise CodeNotFound("No code provided to run")

        elif code and files:
            print('running CodeFormatNotFound')
            raise CodeFormatNotFound("Cannot choose whether to run raw code or code from file/s")

        else:
            if code:

                main_code = [{"name" : '', "content" : code}]

            if files:
                files_content = []

                for file in files:
                    try:
                        with open(file, mode="r") as f:
                            content = f.read()
                            files_content.append({"name": file, "content": content})
                    except FileNotFoundError:
                        raise NotAFile(f"{file} is not a file object.")
                main_code = files_content


        payload = {
            'language' : language,
            'version' : version,
            'files' : main_code,
            'args' : args,
            'stdin' : input,
            'compile_timeout' : compile_timeout,
            'run_timeout' : run_timeout,
            'compile_memory_limit' : compile_memory_limit,
            'run_memory_limit' : run_memory_limit
        }

        return GetOutput(payload).parse_output()
