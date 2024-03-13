"""
Description:Unit tests for the functions in the chatbot module.
Author:Navjot Kaur
Date:13th March 2024
Usage:These tests verify the behavior and functionality of the chatbot functions, ensuring they perform as expected under different scenarios.
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, VALID_TASKS, ACCOUNTS

class ChatbotTests(unittest.TestCase):
    def test_get_account_valid(self):
        # Arrange
        with patch("builtins.input", return_value="123456"):
            # Act
            account_number = get_account()
        
        # Assert
        self.assertEqual(account_number, 123456)

    def test_get_account_non_numeric(self):
        # Arrange
        with patch("builtins.input", return_value="non_numeric_data"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_not_exist(self):
        # Arrange
        with patch("builtins.input", return_value="112233"):
            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number does not exist.")

if __name__ == '__main__':
    unittest.main()
