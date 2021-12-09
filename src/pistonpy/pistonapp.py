# Coding=UTF8
# !python
# !/usr/bin/env python3
import requests, json
from typing import Optional
from .exceptions import CodeNotFound, LanguageNotFound, CodeFormatNotFound, NotAFile, MultipleLanguagesFound
from .models import GetOutput, Extensions

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
    def raw(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        data = response.json()
        return data


    @property
    def languages(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        data = response.json()
        language = []
        version = []

        for i in data:
            language.append(i['language'])
            version.append(i['version'])

        dic = dict(zip(language, version))
        return dic

    @property
    def aliases(self) -> dict:
        url = self._endpoint + "/runtimes"
        response = requests.request("GET", url)
        data = response.json()
        language = []
        alias = []

        for i in data:
            language.append(i['language'])
            alias.append(i['aliases'])

        dic = dict(zip(language, alias))
        return dic

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
        formattedfiles = [i.split('.')[0] for i in files]
        file_extensions = [i.split('.')[1] for i in files]
        bool, message = Extensions(language=language, payload=files).check_files

        if files:
            if bool:
                pass
            else:
                raise MultipleLanguagesFound(f"Files of multiple languages found: {message}")

        if not code and not files:
            print('running CodeNotFound')
            raise CodeNotFound("No code provided to run")

        elif code and files:
            print('running CodeFormatNotFound')
            raise CodeFormatNotFound("Cannot choose whether to run raw code or code from file/s")

        else:
            if code:

                main_code = [{"name" : '', "content" : code}]

            if files and len(files) == 1:
                files_content = []

                for file in files:
                    try:
                        with open(file, mode="r") as f:
                            content = f.read()
                            files_content.append({"name": file, "content": content})
                    except FileNotFoundError:
                        raise FileNotFoundError(f"{file} not found.")
                main_code = files_content

            if files and 1 < len(files) < 5 and 'py' in file_extensions:
                files_content = []

                for file in files:
                    files_content.append({"name" : "main.py", "content" : f"import {', '.join(formattedfiles)}"})
                    try:
                        with open(file, mode="r") as f:
                            content = f.read()
                            files_content.append({"name" : file, "content" : content})
                    except FileNotFoundError:
                        raise FileNotFoundError(f"{file} not found.")

                main_code = files_content
                # print(f"main_code = {main_code}")

            if files and 1 < len(files) <= 5:
                files_content = []
                response = []

                for file in files:
                    try:
                        with open(file, mode="r") as f:
                            content = f.read()
                            files_content.append({"name" : file, "content" : content})
                    except FileNotFoundError:
                        raise FileNotFoundError(f"{file} not found.")

                for data in files_content:
                    temp = []
                    temp.append(json.dumps(data))
                    multiple_files = {
                        'language' : language,
                        'version' : version,
                        'files' : json.dumps(temp),
                        'args' : args,
                        'stdin' : input,
                        'compile_timeout' : compile_timeout,
                        'run_timeout' : run_timeout,
                        'compile_memory_limit' : compile_memory_limit,
                        'run_memory_limit' : run_memory_limit
                    }
                    print(f"Multiple Files - {multiple_files}")
                    response.append(GetOutput(multiple_files).parse_output())
                return response

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
