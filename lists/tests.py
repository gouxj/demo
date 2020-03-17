from django.test import TestCase


class SmokeTest(TestCase):
    def test_bad_maths(self):
        print('test_bad_maths ok')
        self.assertEqual(1 + 1, 3)
