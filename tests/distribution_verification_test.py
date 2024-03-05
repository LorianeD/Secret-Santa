import unittest
from typing import List, Tuple, Dict
from secretsanta.distribution_verification import is_gifts_valid


class TestIsGiftsValid(unittest.TestCase):
    def test_valid_gifts_couples(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = [("Florent", "Jessica"), ("Coline", "Emilien")]
        gifts = {"Florent": "Ambroise", "Ambroise": "Jessica",
                 "Jessica": "Bastien", "Bastien": "Florent"}
        self.assertTrue(is_gifts_valid(people, couples, gifts))

    def test_valid_gifts(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = []
        gifts = {"Florent": "Ambroise", "Ambroise": "Jessica",
                 "Jessica": "Bastien", "Bastien": "Florent"}
        self.assertTrue(is_gifts_valid(people, couples, gifts))

    def test_invalid_number_of_gifts(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = []
        gifts = {"Florent": "Ambroise"}
        self.assertFalse(is_gifts_valid(people, couples, gifts))

    def test_invalid_receivers(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = []
        gifts = {"Florent": "Ambroise", "Ambroise": "Jessica",
                 "Jessica": "Bastien", "Bastien": "Ambroise"}
        self.assertFalse(is_gifts_valid(people, couples, gifts))

    def test_invalid_couple(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = [("Florent", "Jessica"), ("Coline", "Emilien")]
        gifts = {"Florent": "Jessica", "Jessica": "Ambroise",
                 "Ambroise": "Bastien", "Bastien": "Florent"}
        self.assertFalse(is_gifts_valid(people, couples, gifts))

    def test_invalid_reverse(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = []
        gifts = {"Florent": "Bastien", "Ambroise": "Jessica",
                 "Jessica": "Ambroise", "Bastien": "Florent"}
        self.assertFalse(is_gifts_valid(people, couples, gifts))

    def test_self_gift(self):
        people = ["Florent", "Jessica", "Ambroise", "Bastien"]
        couples = []
        gifts = {"Florent": "Florent", "Ambroise": "Ambroise",
                 "Jessica": "Jessica", "Bastien": "Bastien"}
        self.assertFalse(is_gifts_valid(people, couples, gifts))

if __name__ == "__main__":
    unittest.main()
