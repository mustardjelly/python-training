import unittest

from example import Adder

class TestSuite(unittest.TestCase):
    """Will run our tests
    https://docs.python.org/3/library/unittest.html
    """

    def test_adder_works(self):
        """Check that with valid inputs, adder works as expected."""
        # Arrange
        expected_result = 3

        # Act
        result = Adder(1, 2)

        # Assert
        self.assertEqual(result, expected_result, "The result was unexpected.")
        self.assertEqual(type(result), int, "Result is the wrong type")

    def test_adder_option1_is_string_should_fail(self):
        """Check that with an invalid option1 (str type), an expected error is thrown."""
        # Arrange
        invalid_option1 = "someString"

        # Act
        # with wraps indented code and indicates some relationship
        # Capture our exception as a variable.
        with self.assertRaises(AssertionError) as error_context:
            # We use _ when we do not care about the result
            _ = Adder(invalid_option1, 2)

        # Assert
        exception = error_context.exception
        self.assertEqual(str(exception), "option1 is not a integer")

    def test_adder_option2_is_string_should_fail(self):
        """Check that with an invalid option2 (str type), an expected error is thrown."""
        # Arrange
        invalid_option2 = "someString"

        # Act
        # with wraps indented code and indicates some relationship
        # Capture our exception as a variable.
        with self.assertRaises(AssertionError) as error_context:
            # We use _ when we do not care about the result
            _ = Adder(1, invalid_option2)

        # Assert
        exception = error_context.exception
        self.assertEqual(str(exception), "option2 is not a integer")
