#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.case import TestCase

from djangorestframework_camel_case.util import camelize, underscoreize


class UnderscoreToCamelTestCase(TestCase):
    def test_under_to_camel(self):
        input = {
            "title_display": 1
        }
        output = {
            "titleDisplay": 1
        }
        self.assertEqual(camelize(input), output)


class CamelToUnderscoreTestCase(TestCase):
    def test_under_to_camel(self):
        input = {
            "titleDisplay": 1
        }
        output = {
            "title_display": 1
        }
        self.assertEqual(underscoreize(input), output)


class CompatibilityTest(TestCase):
    def test_compatibility(self):
        input = {
            "title245a_display": 1
        }
        self.assertEqual(underscoreize(camelize(input)), input)