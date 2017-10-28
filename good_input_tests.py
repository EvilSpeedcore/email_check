import unittest
from email_check import check_email


class CheckEmailPositiveInput(unittest.TestCase):
    """Class, which represents tests with good input."""
    def test_email(self):
        """Test correct email."""
        self.assertTrue(check_email('fantafan95@yandex.ru'))

    def test_username_for_pair_quotes(self):
        """Test username for pair quotes."""
        self.assertTrue(check_email('fan""tafan95@yandex.ru'))
        self.assertTrue(check_email('fan"taf"an95@yandex.ru'))
        self.assertTrue(check_email('"fantafan95"@yandex.ru'))

    def test_username_for_characters_between_quotes(self):
        """Test username for characters between quotes."""
        self.assertTrue(check_email('f"a!nta"fan95@yandex.ru'))
        self.assertTrue(check_email('f"a!,:nta"fan95@yandex.ru'))


if __name__ == '__main__':
    unittest.main()
