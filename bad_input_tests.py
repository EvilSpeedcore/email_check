import unittest
from email_check import check_email


class CheckEmailNegativeInput(unittest.TestCase):
    """Class, which represents tests with bad input."""
    def test_email_without_at(self):
        """Test for no @ in email"""
        """Проверяет отсутствие знака @ в email'e."""
        self.assertFalse(check_email('fantafan95yandex.ru'))

    def test_username_for_characters_limit(self):
        """Test for character limit in username."""
        self.assertFalse(check_email('a' * 129 + '@yandex.ru'))

    def test_domain_name_for_characters_limit(self):
        """Test for character limit in domain name."""
        # Less than 3 characters exclude dot.
        self.assertFalse(check_email('fantafan95@y.r'))
        # More than 256 characters exclude dot.
        self.assertFalse(check_email('fantafan95@y.r' + 'a' * 255))

    def test_domain_name_for_empty_lines(self):
        """Test for empty domain name."""
        self.assertFalse(check_email('fantafan95@'))

    def test_domain_name_for_point_absence(self):
        """Test domain name for point absence."""
        self.assertFalse(check_email('fantafan95@yandexru'))

    def test_username_for_double_dot(self):
        """Test for two dots in a row in username."""
        email = check_email('fant..afan95@yandex.ru')
        self.assertFalse(email, 'В имени не должны допускаться две точки подряд.')

    def test_username_for_single_quotation_mark(self):
        """Test username for single quotation_mark."""
        email = check_email('fan"tafan95@yandex.ru')
        self.assertFalse(email, 'В имени не должна допускаться одинарная кавычка(").')

    def test_username_for_unacceptable_characters(self):
        """Test username for inappropriate characters."""
        self.assertFalse(check_email('fanta!fan95@yandex.ru'))
        self.assertFalse(check_email('fantafan:95@yandex.ru'))
        self.assertFalse(check_email(',fantafan95@yandex.ru'))
        self.assertFalse(check_email('fant@afan95@yandex.ru'))
        self.assertFalse(check_email('fantafan95@yandex.ru-'))
        self.assertFalse(check_email('fantafan95@yandex.ru-'))
        self.assertFalse(check_email('fantafan95@-yandex.ru'))
        self.assertFalse(check_email('fantafan95@-yandex.ru-'))


if __name__ == '__main__':
    unittest.main()