# !/usr/bin/python
# -*- coding: utf-8 -*-
import re


class Matcher:

    HEADER_TEMPLATE = (r""
        "\/\/\n"
        "\/\/.*\..*\n"
        "\/\/.*\n"
        "\/\/\n"
        "\/\/\s{2}Created by\s.*\son\s\d{1,2}\/\d{1,2}\/\d{2}\.\n"
        "\/\/\s{2}Copyright\s(\(c\)|©)\s\d{4}\s.*\.\sAll rights reserved\.\n"
        "\/\/\n"
    )

    def __init__(self, header):
        self.header = header

    def matches(self):
        return re.match(self.HEADER_TEMPLATE, self.header) is not None
