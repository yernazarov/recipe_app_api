from django.test import TestCase
from app.calc import add
class CalcTests(TestCase):
    def test_1(self):
        self.assertEqual(add(3,4),7)