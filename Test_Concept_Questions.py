from unittest import TestCase, main
from Concept_Questions import is_isogram

class TestIsogramProgram(TestCase):

    # tests the examples for which the function should return true
    def test_true_cases(self):
        self.assertEqual(True, is_isogram("isogram"))
        self.assertEqual(True, is_isogram("uncopyrightable"))
        self.assertEqual(True, is_isogram("ambidextrously"))

    # tests the example cases when the function should return false
    def test_false_cases(self):
        self.assertEqual(False, is_isogram("hello"))
        self.assertEqual(False, is_isogram("bob"))
        self.assertEqual(False, is_isogram("football"))

    # tests for incidences when characters are of varying upper and lower case
    def test_upper_lower_edge_case(self):
        self.assertEqual(False, is_isogram("helLo"))
        self.assertEqual(False, is_isogram("Bob"))


if __name__ == "__main__":
    main()
