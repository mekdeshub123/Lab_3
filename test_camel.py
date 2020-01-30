import camel_case
from unittest import TestCase
class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual("spacesBefore", camel_case.camel_case("Spaces Before"))
        self.assertEqual("stringWithNumber",camel_case.camel_case ("string with number"))
        self.assertEqual("uniCodeCharacters",camel_case.camel_case ("uni code characters"))
    def test_camelcase_sentence_char_exception(self):
        with self.assertRaises(ValueError):
            camel_case.camel_case("*&( **&MM")
        with self.assertRaises(ValueError):
            camel_case.camel_case("*()\\")
        with self.assertRaises(ValueError):
            camel_case.camel_case("= % /$ #")