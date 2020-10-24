from unittest import TestCase

# Pytest
# def test_do_something():
#    pass
from stack import Stack


# unittest
class TestStackOperations(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack.clear()

    def test_should_new_element_to_stack(self):
        value, expected = 42, 42
        self.stack.push(100)
        self.stack.push(value)

        self.assertEqual(self.stack.peek(), expected)

    def test_should_remove_last_element_from_stack(self):
        element, expected = 42, 42

        self.stack.push(element)

        value = self.stack.pop()

        self.assertEqual(value, expected)
        self.assertEqual(self.stack.size, 0)

    def test_should_show_size_of_stack(self):
        self.stack.push(100)
        self.stack.push(50)
        self.stack.push(80)
        self.stack.push(70)
        self.assertEqual(self.stack.size, 4)

    def test_should_peek_latest_element_in_stack(self):
        element, expected = 42, 42
        self.stack.push(element)
        self.assertEqual(self.stack.peek(), expected)
        self.assertEqual(self.stack.size, 1)

    def test_should_clear_stack(self):
        self.stack.push(42)
        self.stack.push(43)

        self.stack.clear()

        self.assertEqual(self.stack.size, 0)

    def test_should_raise_when_called_pop_on_empty_stack(self):
        self.assertRaises(IOError, self.stack.pop)
