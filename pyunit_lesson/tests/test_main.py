import unittest
from app.calculator import Calculator, InvalidInputException
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    @unittest.parameterized.expand([
        (2, 2, 1),
        (8, 2, 3),
        (100, 10, 2),
        # Добавьте другие тестовые случаи
    ])
    def test_log_normal_input(self, a, base, expected_result):
        result = self.calc.log(a, base)
        self.assertEqual(result, expected_result)
    def test_log_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calc.log('a', 0)
    def test_log_invalid_input_exception(self):
        with self.assertRaises(InvalidInputException):
            self.calc.log(0, 0)