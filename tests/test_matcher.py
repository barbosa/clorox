# !/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from clorox.matcher import Matcher


class MatcherTestCase(unittest.TestCase):

    def test_matcher_with_2_digits_dates(self):
        header = (
            ""
            "//\n"
            "//  MyFile.swift\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright (c) 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_1_digit_month(self):
        header = (
            ""
            "//\n"
            "//  MyFile.swift\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 2/18/15.\n"
            "//  Copyright (c) 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_1_digit_day(self):
        header = (
            ""
            "//\n"
            "//  MyFile.swift\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/1/15.\n"
            "//  Copyright (c) 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_objc_header_file(self):
        header = (
            ""
            "//\n"
            "//  MyFile.h\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright (c) 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_objc_implementation_file(self):
        header = (
            ""
            "//\n"
            "//  MyFile.m\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright (c) 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_special_copyright_character(self):
        header = (
            ""
            "//\n"
            "//  MyFile.m\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright © 2015 MyCompany. All rights reserved.\n"
            "//\n"
        )

        assert Matcher(header).match()

    def test_matcher_with_trim_new_lines_on(self):
        header = (
            ""
            "\n"
            "\n"
            "//\n"
            "//  MyFile.m\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright © 2015 MyCompany. All rights reserved.\n"
            "//\n"
            "\n"
            "\n"
        )

        assert Matcher(header, trim_new_lines=True).match()

    def test_matcher_with_trim_new_lines_off(self):
        header = (
            ""
            "\n"
            "\n"
            "//\n"
            "//  MyFile.m\n"
            "//  MyCompany\n"
            "//\n"
            "//  Created by John Appleseed on 12/18/15.\n"
            "//  Copyright © 2015 MyCompany. All rights reserved.\n"
            "//\n"
            "\n"
            "\n"
        )

        assert not Matcher(header, trim_new_lines=False).match()


if __name__ == '__main__':
    unittest.main()
