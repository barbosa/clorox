# !/usr/bin/python
# -*- coding: utf-8 -*-
class Reporter:

    TYPES = {}

    @classmethod
    def from_identifier(cls, identifier):
        return Reporter.TYPES.get(identifier, None)

    def report_start(self):
        pass

    def report(self):
        pass

    def report_end(self):
        pass
