import unittest
from Polynomial import Polynomial
class PolyTest(unittest.TestCase):
    def test_init_correct_args(self):
        p = Polynomial([3, 1, 4])
        self.assertEqual(p.coeffs, [3, 1, 4])
        self.assertEqual(p.degree, 2)

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [])

    def test_init_senior_values_is_zero(self):
        p = Polynomial([0, 1, 1])
        self.assertEqual(p.coeffs, [1, 1])
        self.assertEqual(p.degree, 1)

    def test_eq_true(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1, 1])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])
        self.assertFalse(p1 == p2)

    def test_eq_other_is_constant(self):
        p1 = Polynomial([2])
        p2 = 2
        self.assertTrue(p1 == p2)

    def test_add_same_poly_size(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2, 4])
        self.assertEqual(p3.degree, 1)

    def test_add_different_poly_size_first_larger(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_different_poly_size_second_larger(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2, 3])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_const(self):
        p1 = 1
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3])
        self.assertEqual(p3.degree, 1)

    def test_add_zero_constant(self):
        p1 = Polynomial([1, 1])
        p2 = 0
        p3 = p1 + p2
        self.assertEqual(p3, p1)
        self.assertEqual(p3.degree, 1)

    def test_mul_same_poly_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 1])
        self.assertEqual(p3.degree, 2)

    def test_mul_different_poly_size(self):
        p1 = Polynomial([1, 1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 2, 1])
        self.assertEqual(p3.degree, 3)

    def test_mul_left_term_is_const(self):
        p1 = 2
        p2 = Polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [2, 4, 6])
        self.assertEqual(p3.degree, 2)

    def test_mul_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_one_value_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, p1.coeffs)
        self.assertEqual(p3.degree, 1)

    def test_mul_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 5
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [5, 10])
        self.assertEqual(p3.degree, 1)

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "1")

    def test_str(self):
        p1 = Polynomial([3, 1])
        self.assertEqual(str(p1), '3x+1')


    def test_str_first_value_is_zero(self):
        p1 = Polynomial([0, 2, 1])
        self.assertEqual(str(p1), '2x+1')

    def test_str_all_values_are_one(self):
        p1 = Polynomial([1, 1, 1])
        self.assertEqual(str(p1), 'x^2+x+1')

    def test_str_last_value_is_zero(self):
        p1 = Polynomial([1, 0])
        self.assertEqual(str(p1), 'x')

    def test_str_one_value_is_minus_zero(self):
        p1 = Polynomial([0, -1, 0])
        self.assertEqual(str(p1), '-x')


if __name__ == "__main__":
    unittest.main()