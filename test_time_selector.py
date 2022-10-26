import unittest
from time_selector import TimeSelector


class TestTimeSelector(unittest.TestCase):

    def test_validate_day_valid(self):
        test_day = "MT"  # also test FS
        self.assertEqual(TimeSelector.validate_day(test_day), 1)

    def test_validate_day_invalid(self):
        test_day = "Monday"
        with self.assertRaises(ValueError):
            TimeSelector.validate_day(test_day)

    def test_convert_to_mins_1(self):
        test_len = "2:14"
        self.assertEqual(TimeSelector.convert_to_mins(test_len), 134)

    def test_convert_to_mins_2(self):
        test_len = "0:55"
        self.assertEqual(TimeSelector.convert_to_mins(test_len), 55)


if __name__ == '__main__':
    unittest.main()
