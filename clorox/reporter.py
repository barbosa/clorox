# !/usr/bin/python
# -*- coding: utf-8 -*-
class Reporter:

    @classmethod
    def from_identifier(cls, identifier):
        clazz = TYPES.get(identifier, None)
        return clazz() if clazz else None

    def report(self, all_files, modified_files):
        pass


class JSONReporter(Reporter):
    def report(self, all_files, modified_files):
        print {
            'status': 'clean' if len(modified_files) == 0 else 'dirty',
            'files': modified_files
        }

TYPES = {'json': JSONReporter}
