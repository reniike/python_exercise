import unittest

from credit_card_validator import card_confirmation


class TestCreditCardValidator(unittest.TestCase):

    def test_valid_credit_card(self):
        self.assertEqual(card_confirmation("5399834432138592"), "Card is Valid")

    def test_invalid_credit_card(self):
        self.assertEqual(card_confirmation("539983443213859"), "Card is Invalid")
