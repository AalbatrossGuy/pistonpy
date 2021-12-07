# Coding=UTF8
# !python
# !/usr/bin/env python3

class CodeNotFound(Exception):
    pass

class LanguageNotFound(Exception):
    pass

class CodeFormatNotFound(Exception):
    pass

class NotAFile(Exception):
    pass


class PistonError(Exception):
    pass

class MultipleLanguagesFound(Exception):
    pass
