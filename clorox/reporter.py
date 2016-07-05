# !/usr/bin/python
# -*- coding: utf-8 -*-
class Reporter:

    @classmethod
    def from_identifier(cls, identifier):
        clazz = TYPES.get(identifier, None)
        return clazz() if clazz else None

    def report(self):
        pass


class JSONReporter(Reporter):
    def report(self):
        print "JSOOOOONNNNNNNN"

TYPES = {'json': JSONReporter}
