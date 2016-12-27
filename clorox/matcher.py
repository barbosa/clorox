# !/usr/bin/python
# -*- coding: utf-8 -*-
import re


class Matcher:

    _DEFAULT_HEADER_TEMPLATE = (r""
        "\/\/\n"
        "\/\/.*\..*\n"
        "\/\/.*\n"
        "\/\/\n"
        "\/\/\s{2}Created by\s.*\son\s\d{1,2}\/\d{1,2}\/\d{2}\.\n"
        "\/\/\s{2}Copyright\s(\(c\)|©)\s\d{4}\s.*\.\sAll rights reserved\.\n"
        "\/\/\n"
    )

    def __init__(self, content, trim_new_lines=False):
        self.content = content
        self.trim_new_lines = trim_new_lines

    @property
    def header(self):
        trim_regex = r"\s*" if self.trim_new_lines else r""
        return r"{trim_regex}{core}{trim_regex}".format(
            trim_regex=trim_regex,
            core=self._DEFAULT_HEADER_TEMPLATE
        )

    def match(self):
        result = re.match(self.header, self.content)
        return result.group(0) if result else None
